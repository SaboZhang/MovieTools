#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# @Author: 张涛
# @Date: 2020-11-18 12:09:53
# @LastEditTime: 2020-11-20 18:06:49
# @LastEditors: 张涛
# @Description: 一句话描述
# @FilePath: \test1.py
# @世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
# ----------------------------------------
import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET


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
        # root = iterparse(filePath, ('start', 'end'))
        for element in root.iter('movie'):
            # 根节点信息
            element.findtext('plot')
            # 添加日期
            element.findtext('dateadded')
            element.findtext('title')
            element.findtext('originaltitle')
            element.findtext('director')
            element.findtext('rating')
            element.findtext('year')
            element.findtext('imdbid')
            element.findtext('tmdbid')
            element.findtext('premiered')
            element.findtext('releasedate')
            # 烂番茄评分
            element.findtext('criticrating')
            element.findtext('runtime')
            for v, k in enumerate(element):
                if k.tag == 'country':
                    print('{0}'.format(element[v].text))
                elif k.tag == 'genre':
                    print('{0}'.format(element[v].text))
                elif k.tag == 'studio':
                    print('{0}'.format(element[v].text))
            for actor in element.iter('actor'):
                for info in actor.iter('actor'):
                    info.findtext('name')
                    info.findtext('role')
                    info.findtext('type')


if __name__ == "__main__":
    # video_name = get_video_name(r'E:\Documents')
    # for k, v in video_name.items():
    # if element.attrib() == 'country':
    #     print('Key是', k)
    #     print('value', v)
    # file = r'E:\Downloads\请用心听.不要.说话.雅乐传媒.mp3'
    # print(os.path.splitext(file)[-1])
    nfo_parse('E:\Downloads\Mulan 2020 Disney+ 4K WEBRip HDR10+ x265 10bit DD+ 5.1 Atmos -LMovHD.nfo')
    # test_dict = {}
    # for i in range(5):
    #     test_list = [].append(i)
    # print(test_list)
   
