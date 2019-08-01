# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 0:06
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: Resample.py

import numpy as np
from scipy.ndimage import zoom


def Resample(imgs, spacing, new_spacing, order=2):
    '''
    Resample the image with specific resolution.
    :param imgs: ndarray, image.
    :param spacing: spacing of the image.
    :param new_spacing: new resolution, e.g. [1,1,1].
    :param order: order of interpolation.
    :return: new image and spacing after resampling.
    '''
    if len(imgs.shape) == 3:
        new_shape = np.round(imgs.shape * spacing / new_spacing)
        true_spacing = spacing * imgs.shape / new_shape
        resize_factor = new_shape / imgs.shape
        imgs = zoom(imgs, resize_factor, mode='nearest', order=order)
        return imgs, true_spacing
    elif len(imgs.shape) == 4:
        n = imgs.shape[-1]
        newimg = []
        for i in range(n):
            slice = imgs[:, :, :, i]
            newslice, true_spacing = Resample(slice, spacing, new_spacing)
            newimg.append(newslice)
        newimg = np.transpose(np.array(newimg), [1, 2, 3, 0])
        return newimg, true_spacing
