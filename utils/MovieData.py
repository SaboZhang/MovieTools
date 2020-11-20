#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# @Author: 张涛
# @Date: 2020-10-10 18:36:56
# @LastEditTime: 2020-11-20 17:27:09
# @LastEditors: 张涛
# @Description: 一句话描述
# @FilePath: \utils\MovieData.py
# @世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
# ----------------------------------------
import os
import re
from moviepy.editor import VideoFileClip
import xml.etree.ElementTree as ET


class MovieData(object):

    def get_video_times(self, filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time

    # 单位换算
    def timeConvert(self, size):
        M, H = 60, 60**2
        if size < M:
            return str(size)+u'秒'
        if size < H:
            return u'%s分钟%s秒' % (int(size/M), int(size % M))
        else:
            hour = int(size/H)
            mine = int(size % H/M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt

    # 读取本地视频文件
    def get_video_name(self, filePath):
        fileNames = os.listdir(filePath)
        video_name = {}
        for names in fileNames:
            if names == "$RECYCLE.BIN" or names == "System Volume Information":
                continue
            videoPath = os.path.join(filePath, names)
            if os.path.isdir(videoPath):
                # 递归
                self.get_video_name(videoPath)
            elif names.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso')):
                print(videoPath)
                # 拆分出视频名
                fullName = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])", "", names)
                ext = os.path.splitext(videoPath)[-1]
                shortName = re.split('[. ]', fullName)[0]
                print(shortName)
                video_name[shortName] = [fullName, ext, videoPath]
            # 判断是否允许读取已存在的.nfo文件
            elif names.endswith('.nfo'):
                self.nfo_parse(videoPath)
        return video_name

    def nfo_parse(self, filePath):
        """
        解析nfo文件中的内容,直接存储信息
        """
        tree = ET.parse(filePath)
        root = tree.getroot()
        nfo = {}
        for element in root.iter('movie'):
            # 根节点信息
            nfo['plot'] = element.findtext('plot')
            # 添加日期
            nfo['add_date'] = element.findtext('dateadded')
            nfo['title'] = element.findtext('title')
            nfo['org_title'] = element.findtext('originaltitle')
            nfo['director'] = element.findtext('director')
            nfo['rating'] = element.findtext('rating')
            nfo['year'] = element.findtext('year')
            nfo['imdb_id'] = element.findtext('imdbid')
            nfo['tmdb_id'] = element.findtext('tmdbid')
            nfo['premiered'] = element.findtext('premiered')
            nfo['releasedate'] = element.findtext('releasedate')
            # 烂番茄评分
            nfo['criticrating'] = element.findtext('criticrating')
            nfo['runtime'] = element.findtext('runtime')
            country = []
            genre = []
            studio = []
            for v, k in enumerate(element):
                if k.tag == 'country':
                    country.append('{0}'.format(element[v].text))
                elif k.tag == 'genre':
                    genre.append('{0}'.format(element[v].text))
                elif k.tag == 'studio':
                    studio.append('{0}'.format(element[v].text))
            nfo['country'] = country
            nfo['genre'] = genre
            nfo['studio'] = studio
            for actor in element.iter('actor'):
                for info in actor.iter('actor'):
                    info.findtext('name')
                    info.findtext('role')
                    info.findtext('type')

# # 影片名称拆分
# str = '[#机器人总动员].Wall.E.2008.UHD.2160p.x265.10bit.HDR.DDP5.1.国粤台英四语.内封特效中英-FFans@leon'

# # 名称匹配正则，过滤掉特殊字符 未过滤#跟@
# # 匹配中文字符、大小英文字符、数字、空格 . 以及#@ 返回字符串以 Unicode 格式 进行编码
# sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])","",str)
# print(sub_str)

# # 根据指定字符拆解 .跟空格获取到名字
# print(re.split('[. ]',sub_str)[0])
