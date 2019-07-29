# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 23:55
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: mhd-main.py
import SimpleITK as stk
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

from readFile import readFile


def readMHD(ImagePath):
    '''
    Read single MHD image.
    :param ImagePath: string, single MHD image path.
    :return: image array, vector of origin [x,y,z], vector of spacing [x,y,z].
    '''
    with open(ImagePath) as f:
        contents = f.readlines()
        line = [k for k in contents if k.startswith('TransformMatrix')][0]
        transformM = np.array(line.split(' = ')[1].split(' ')).astype('float')
        transformM = np.round(transformM)
        if np.any(transformM != np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])):
            isflip = True
        else:
            isflip = False
    image_stk = stk.ReadImage(ImagePath)
    # [z,y,x]
    image_numpy = stk.GetArrayFromImage(image_stk)
    # [x,y,z]
    image_origin = image_stk.GetOrigin()
    # [x,y,z]
    image_spacing = image_stk.GetSpacing()
    return image_numpy, image_origin, image_spacing, isflip


def showMHD(Image):
    '''
    Show MHD image.
    :param Image: string, path of MHD image.
    '''
    print(f"The shape of the current MHD image is {Image.shape}")
    if len(Image.shape) == 3:
        slice_num = Image.shape[0]
        for slice in range(slice_num):
            plt.imshow(Image[slice, :, :], cmap='gray')
            plt.pause(pow(0.1, 8))
            plt.ioff()
            plt.show()
    if len(Image.shape) == 4:
        Image_tmp = Image.squeeze()
        showMHD(Image_tmp)


if __name__ == '__main__':
    Image = str(Path(r'D:/tianchi/chestCT_round1_testA/testA/322782.mhd'))
    image, origin, spacing, _ = readMHD(Image)
    showMHD(image[np.newaxis])

    pass
