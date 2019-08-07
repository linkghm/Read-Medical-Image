# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 17:09
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: dicom-main.py

from pathlib import Path
import SimpleITK as stk
import matplotlib.pyplot as plt
import numpy as np

plt.ion()


class readDICOM():
    def __init__(self, ImagePath):
        '''

        :param ImagePath: string, single DICOM image path.
        '''
        self.ImagePath = ImagePath

    def readDICOM(self):
        reader = stk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(self.ImagePath)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
        # [z, y, x]
        image_numpy = stk.GetArrayFromImage(image)
        origin = image.GetOrigin()  # x, y, z
        spacing = image.GetSpacing()  # x, y, z
        # [z,y,x]
        image_origin = np.array(list(reversed(origin)))
        # [z,y,x]
        image_spacing = np.array(list(reversed(spacing)))
        return image_numpy, image_origin, image_spacing

    def showDICOM(self):
        reader = stk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(self.ImagePath)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
        # [z, y, x]
        image_numpy = stk.GetArrayFromImage(image)
        print(f"The shape of the current DICOM image is {image_numpy.shape}")
        if len(image_numpy.shape) == 3:
            slice_size = image_numpy.shape[0]
            for slice in range(slice_size):
                plt.imshow(image_numpy[slice, :, :], cmap='gray')
                plt.pause(pow(0.1, 8))
                plt.ioff()
                plt.show()
        if len(image_numpy.shape) == 4:
            Image_tmp = image_numpy.squeeze()
            self.showDICOM(Image_tmp)


if __name__ == '__main__':
    ImagePath = str(Path('D:/DICOM'))
    readDICOM = readDICOM(ImagePath)
    image_numpy, image_origin, image_spacing = readDICOM.readDICOM()
    readDICOM.showDICOM()