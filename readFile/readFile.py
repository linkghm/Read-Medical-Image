# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 23:56
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: readFile.py

from pathlib import Path
import os

FileList = []


def readFile(FilePath):
    '''
    Read files of selected folder, return a list of paths of files.
    Path format will change according to OS.
    FilePath should be like './example_path1/example_path2'
    :param FilePath: string, the path of folder including some files you want to read
    :return: a list of paths of files
    '''
    filelist = os.listdir(FilePath)
    for filename in filelist:
        filepath = os.path.join(FilePath, filename)
        if os.path.isdir(filepath):
            readFile(filepath)
        else:
            FileList.append(Path(filepath))
    return FileList


if __name__ == '__main__':
    root = Path(r'D:/tianchi')
    print(readFile(root)[0])
    pass
