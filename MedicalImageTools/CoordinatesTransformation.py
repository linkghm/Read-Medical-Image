# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 0:31
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: CoordinatesTransformation.py
import numpy as np


def WorldToVoxelCoord(worldCoord, origin, spacing):
    '''
    The format of coordinates in CT image is Voxel, however, many situations offer the World format,
    the function converts the World coordinates to the Voxel coordinates.
    :param worldCoord: World coordinates, the format should be [z,y,x].
    :param origin: [z,y,x], coordinates of the pixel/voxel with index (0,0,0) in physical units (i.e. mm).
    :param spacing: [z,y,x], distance between adjacent pixels/voxels in each dimension given in physical units.
    :return: Voxel coordinates, numpy array.
    '''
    # origin [z,y,x]
    # spacing [z,y,x]
    stretchedVoxelCoord = np.absolute(worldCoord - origin)
    voxelCoord = stretchedVoxelCoord / spacing
    return voxelCoord


def VoxelToWorldCoord(voxelCoord, origin, spacing):
    '''
    The format of coordinates in CT image is Voxel, however, many situations offer the World format,
    the function converts the Voxel coordinates to the World coordinates.
    :param voxelCoord: Voxel coordinates, the format should be [z,y,x], or [x,y,z].
    :param origin: [z,y,x], coordinates of the pixel/voxel with index (0,0,0) in physical units (i.e. mm).
    :param spacing: [z,y,x], distance between adjacent pixels/voxels in each dimension given in physical units.
    :return: World coordinates, numpy array.
    '''
    # origin [z,y,x]
    # spacing [z,y,x]
    stretchedWorldCoord = voxelCoord * spacing
    worldCoord = stretchedWorldCoord + origin
    return worldCoord
