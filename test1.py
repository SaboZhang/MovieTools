#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: 张涛
@Date: 2020-11-18 12:09:53
@LastEditTime: 2020-11-25 14:58:58
@LastEditors: 张涛
@Description: 一句话描述
@FilePath: /test1.py
@世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
"""
import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET
import time


def get_video_name(filePath):
        fileNames = os.listdir(filePath)
        video_name = {}
        for names in fileNames:
            if names == "$RECYCLE.BIN" or names == "System Volume Information":
                continue
            videoPath = os.path.join(filePath, names)
            if os.path.isdir(videoPath):
                # 递归
                get_video_name(videoPath)
            elif names.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso')):
                print(videoPath)
                # 拆分出视频名
                fullName = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])", "", names)
                videoName = re.split('[. ]', fullName)[0]
                print(videoName)
                video_name[videoName] = [fullName, videoPath]
        return video_name


def nfo_parse(filePath):
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
            actor_num = 0
            for actor in element.iter('actor'):
                actor_num += 1
                for info in actor.iter('actor'):
                    name = info.findtext('name')
                    role = info.findtext('role')
                    occupation = info.findtext('type')
                    nfo['actor%s' % actor_num] = [name, role, occupation]
            print(nfo)

if __name__ == "__main__":
    # video_name = get_video_name(r'E:\Documents')
    # for k, v in video_name.items():
    # if element.attrib() == 'country':
    #     print('Key是', k)
    #     print('value', v)
    # file = r'E:\Downloads\请用心听.不要.说话.雅乐传媒.mp3'
    # print(os.path.splitext(file)[-1])
    # nfo_parse(r'E:\Downloads\Mulan 2020 Disney+ 4K WEBRip HDR10+ x265 10bit DD+ 5.1 Atmos -LMovHD.nfo')
    # time.sleep(60)
    # test_dict = {}
    # for i in range(5):
    #     test_list = [].append(i)
    # print(test_list)
    # [终结者6：黑暗命运].Terminator.Dark.Fate.2019.UHD.2160p.x265.10bit.HDR.DDP5.1.English.内封特效中英-FFans@leon
    # # # 影片名称拆分
    str = '[终结者6：黑暗命运].Terminator.Dark.Fate.2019.UHD.2160p.x265.10bit.HDR.DDP5.1.English.内封特效中英-FFans@leon'

    # 名称匹配正则，过滤掉特殊字符 未过滤#跟@
    # 匹配中文字符、大小英文字符、数字、空格 . 以及#@ 返回字符串以 Unicode 格式 进行编码
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])","",str)
    print(sub_str)

    # 根据指定字符拆解 .跟空格获取到名字
    print(re.split('[. ]',sub_str)[0])  
