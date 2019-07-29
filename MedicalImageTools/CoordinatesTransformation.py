# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 0:31
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: CoordinatesTransformation.py
import numpy as np


def WorldToVoxelCoord(worldCoord, origin, spacing, ZYX=True):
    '''
    The format of coordinates in CT image is Voxel, however, many situations offer the World format,
    the function converts the World coordinates to the Voxel coordinates.
    :param worldCoord: World coordinates, the format should be [z,y,x], or [x,y,z].
    :param origin: [x,y,z], coordinates of the pixel/voxel with index (0,0,0) in physical units (i.e. mm).
    :param spacing: [x,y,z], distance between adjacent pixels/voxels in each dimension given in physical units.
    :param ZYX: ZYX=True means the input coordinates are arranged in [z,y,x] order,
                if not, the input coordinates should be [x,y,z].
    :return: Voxel coordinates, numpy array.
    '''
    if ZYX:
        # origin [x,y,z] --> [z,y,x]
        # spacing [x,y,z] --> [z,y,x]
        origin_numpy = np.array(list(reversed(origin)))
        spacing_numpy = np.array(list(reversed(spacing)))
        stretchedVoxelCoord = np.absolute(worldCoord - origin_numpy)
        voxelCoord = stretchedVoxelCoord / spacing_numpy
    else:
        # origin [x,y,z]
        # spacing [x,y,z]
        origin_numpy = np.array(list(origin))
        spacing_numpy = np.array(list(spacing))
        stretchedVoxelCoord = np.absolute(worldCoord - origin_numpy)
        voxelCoord = stretchedVoxelCoord / spacing_numpy
    return voxelCoord


def VoxelToWorldCoord(voxelCoord, origin, spacing, ZYX=True):
    '''
    The format of coordinates in CT image is Voxel, however, many situations offer the World format,
    the function converts the Voxel coordinates to the World coordinates.
    :param voxelCoord: Voxel coordinates, the format should be [z,y,x], or [x,y,z].
    :param origin: [x,y,z], coordinates of the pixel/voxel with index (0,0,0) in physical units (i.e. mm).
    :param spacing: [x,y,z], distance between adjacent pixels/voxels in each dimension given in physical units.
    :param ZYX: ZYX=True means the input coordinates are arranged in [z,y,x] order,
                if not, the input coordinates should be [x,y,z].
    :return: World coordinates, numpy array.
    '''
    if ZYX:
        # origin [x,y,z] --> [z,y,x]
        # spacing [x,y,z] --> [z,y,x]
        origin_numpy = np.array(list(reversed(origin)))
        spacing_numpy = np.array(list(reversed(spacing)))
        stretchedWorldCoord = voxelCoord * spacing_numpy
        worldCoord = stretchedWorldCoord + origin_numpy
    else:
        # origin [x,y,z]
        # spacing [x,y,z]
        origin_numpy = np.array(list(origin))
        spacing_numpy = np.array(list(spacing))
        stretchedWorldCoord = voxelCoord * spacing_numpy
        worldCoord = stretchedWorldCoord + origin_numpy
    return worldCoord
