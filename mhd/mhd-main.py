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


class ReadMHD():
    def __init__(self, ImagePath):
        '''

        :param ImagePath: string, single MHD image path.
        '''
        self.ImagePath = ImagePath

    def readMHD(self):
        '''
        Read single MHD image.
        :param ImagePath: string, single MHD image path.
        :return: image array, vector of origin [x,y,z], vector of spacing [x,y,z].
        '''
        with open(self.ImagePath) as f:
            contents = f.readlines()
            line = [k for k in contents if k.startswith('TransformMatrix')][0]
            transformM = np.array(line.split(' = ')[1].split(' ')).astype('float')
            transformM = np.round(transformM)
            if np.any(transformM != np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])):
                isflip = True
            else:
                isflip = False
        image_stk = stk.ReadImage(self.ImagePath)
        # [z,y,x]
        image_numpy = stk.GetArrayFromImage(image_stk)
        # [z,y,x]
        image_origin = np.array(list(reversed(image_stk.GetOrigin())))
        # [z,y,x]
        image_spacing = np.array(list(reversed(image_stk.GetSpacing())))
        return image_numpy, image_origin, image_spacing, isflip

    def showMHD(self):
        '''
        Show MHD image.
        '''
        image_stk = stk.ReadImage(self.ImagePath)
        # [z,y,x]
        image_numpy = stk.GetArrayFromImage(image_stk)
        print(f"The shape of the current MHD image is {image_numpy.shape}")
        if len(image_numpy.shape) == 3:
            slice_size = image_numpy.shape[0]
            for slice in range(slice_size):
                plt.imshow(image_numpy[slice, :, :], cmap='gray')
                plt.pause(pow(0.1, 8))
                plt.ioff()
                plt.show()
        if len(image_numpy.shape) == 4:
            Image_tmp = image_numpy.squeeze()
            self.showMHD(Image_tmp)


if __name__ == '__main__':
    from MedicalImageTools.CoordinatesTransformation import VoxelToWorldCoord
    from MedicalImageTools.Resample import Resample

    image_path = str(Path(r'D:/tianchi/chestCT_round1_testA/testA/322782.mhd'))
    ReadMHD = ReadMHD(image_path)
    image, origin, spacing, isflip = ReadMHD.readMHD()
    worldCoord = VoxelToWorldCoord(voxelCoord=[2, 3, 4], origin=origin, spacing=spacing)
    new_image, _ = Resample(image, spacing, [1, 1, 1])
    pass
