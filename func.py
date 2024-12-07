#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

import cv2
import numpy as np


# 计算两张图片的灰度差值
def _count_gray_difference(image1, image2):

    # 转换为灰度图
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 将灰度图像转换为 NumPy 数组
    gray1 = gray1.astype(np.int32)
    gray2 = gray2.astype(np.int32)

    # 计算灰度条件
    condition = (
            (gray1 > 1.975 * gray2) &
            (gray1 < 2.025 * gray2) &
            (np.abs(gray1 - 2 * gray2) <= 2)
    )

    # 统计满足条件的像素数量
    count = np.sum(condition)

    # # 初始化计数器
    # count = 0
    #
    # # 获取图像的尺寸
    # height, width = gray1.shape
    #
    # # 手动遍历每个像素
    # for i in range(height):
    #     for j in range(width):
    #         # 获取两个图像对应像素的灰度值
    #         value1 = int(gray1[i, j])
    #         value2 = int(gray2[i, j])
    #         # 检查条件：图像一中的某个点的灰度值是否是图像二中对应点的1.9倍
    #         if value1 > 1.975 * value2 and value1 < 2.025 * value2 and abs(value1 - 2 * value2) <= 2:
    #             count += 1

    return count


def _count_color_difference(image1, image2):
    # 提取蓝色通道（索引为0）
    blue1 = image1[:, :, 0].astype(np.int32)
    blue2 = image2[:, :, 0].astype(np.int32)

    # 计算满足条件的布尔矩阵
    condition = (blue1 > 1.6 * blue2) & (blue1 < 2.5 * blue2)

    # 统计满足条件的像素数量
    count = np.sum(condition)

    return count

    # # 初始化计数器
    # count = 0
    #
    # # 获取图像的尺寸
    # height, width, _ = image1.shape
    #
    # # 手动遍历每个像素
    # for i in range(height):
    #     for j in range(width):
    #         # 获取两个图像对应像素的颜色通道值
    #         blue1 = int(image1[i, j, 0])  # 蓝色通道的索引为0
    #
    #         blue2 = int(image2[i, j, 0])
    #
    #         # 检查条件：图像一中的某个点的蓝色通道值是否是图像二中对应点的1.9倍 and abs(blue1 - 2 * blue2) <= 10
    #         if blue1 > 1.6 * blue2 and blue1 < 2.5 * blue2:
    #             count += 1
    #
    # return count


# 返回图片的一个区域
def _extract_region(image, top_left, size):
    # 确定区域
    x, y = top_left
    width, height = size

    # 提取区域
    region = image[y:y + height, x:x + width]

    return region


def identify_length(img_path):
    # 示例使用
    top_left = (12, 90)  # 替换为你希望提取区域的左上角坐标
    size = (76, 150)  # 替换为你希望提取区域的大小
    image = cv2.imread(img_path)

    length_pixel = 258  # 横向平移像素长度
    original_img = _extract_region(image, top_left, size)

    diff_count = 0

    length = 0

    for i in range(length_pixel):
        # print(1)
        top_left_diff = (top_left[0] + i, top_left[1])

        # 提取指定区域
        region = _extract_region(image, top_left_diff, size)
        count = _count_gray_difference(original_img, region)
        if count > diff_count:
            diff_count = count
            length = i
    if diff_count < 150:
        for i in range(length_pixel):
            # print(1)
            top_left_diff = (top_left[0] + i, top_left[1])

            # 提取指定区域
            region = _extract_region(image, top_left_diff, size)
            count = _count_color_difference(original_img, region)
            if count > diff_count:
                diff_count = count
                length = i

    if diff_count < 150:
        length = -1
    return length, diff_count


if __name__ == "__main__":
    print(identify_length("outimg/3.png"))
