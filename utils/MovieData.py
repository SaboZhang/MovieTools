#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# @Author: 张涛
# @Date: 2020-10-10 18:36:56
# @LastEditTime: 2020-11-17 17:46:10
# @LastEditors: 张涛
# @Description: 一句话描述
# @FilePath: \utils\MovieData.py
# @世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
# ----------------------------------------
import os
import re
from pathlib import Path


class MovieData():
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
                get_video_name(videoPath)
            else:
                print(videoPath)
                # 拆分出视频名
                fullName = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])", "", names)
                videoName = re.split('[. ]', fullName)[0]
                print(videoName)
                video_name[videoName] = fullName
        return video_name

# # 影片名称拆分
# str = '[#机器人总动员].Wall.E.2008.UHD.2160p.x265.10bit.HDR.DDP5.1.国粤台英四语.内封特效中英-FFans@leon'

# # 名称匹配正则，过滤掉特殊字符 未过滤#跟@
# # 匹配中文字符、大小英文字符、数字、空格 . 以及#@ 返回字符串以 Unicode 格式 进行编码
# sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\s.#@])","",str)
# print(sub_str)

# # 根据指定字符拆解 .跟空格获取到名字
# print(re.split('[. ]',sub_str)[0])
