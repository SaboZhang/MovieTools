#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# @Author: 张涛
# @Date: 2020-11-18 12:09:53
# @LastEditTime: 2020-11-18 17:54:57
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
        for element in root.iter('movie'):
            print(element.findtext('plot'))
            print(element[0].findtext('country'))
            print(element[1].findtext('country'))
            # print(element.findtext('actor'))
            for ac in element.iter('actor'):
                for u in ac.iter('actor'):
                    print(u.findtext('name'))
                    print(u.findtext('role'))
                    print(u.findtext('type'))
            out = {}
            for n in range(len(element)):
                out.append('{0}'.format(element[n].text))
            print(out)


if __name__ == "__main__":
    # video_name = get_video_name(r'E:\Documents')
    # for k, v in video_name.items():
    #     print('Key是', k)
    #     print('value', v)
    # file = r'E:\Downloads\请用心听.不要.说话.雅乐传媒.mp3'
    # print(os.path.splitext(file)[-1])
    nfo_parse('E:\Downloads\Mulan 2020 Disney+ 4K WEBRip HDR10+ x265 10bit DD+ 5.1 Atmos -LMovHD.nfo')
