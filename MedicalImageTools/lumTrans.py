# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 18:06
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: lumTrans.py
import numpy as np


def lumTrans(img):
    '''
    肺窗调整
    :param img: numpy image.
    :return: 肺窗调整后的新图，[0,255]
    '''
    lungwin = np.array([-1200., 600.])
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])
    newimg[newimg < 0] = 0
    newimg[newimg > 1] = 1
    newimg = (newimg * 255).astype('uint8')
    return newimg
