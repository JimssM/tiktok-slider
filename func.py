#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import cv2
import numpy as np


# 计算灰度差值
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

    return count


# 计算颜色差值
def _count_color_difference(image1, image2):
    # 提取蓝色通道（索引为0）
    blue1 = image1[:, :, 0].astype(np.int32)
    blue2 = image2[:, :, 0].astype(np.int32)

    # 计算满足条件的布尔矩阵
    condition = (blue1 > 1.6 * blue2) & (blue1 < 2.5 * blue2)

    # 统计满足条件的像素数量
    count = np.sum(condition)

    return count


# 返回图片的一个区域
def _extract_region(image, top_left, size):
    # 确定区域
    x, y = top_left
    width, height = size

    # 提取区域
    region = image[y:y + height, x:x + width]

    return region


# 计算目标区域的长度
def identify_length(img_path):
    # 示例使用
    top_left = (12, 90)  # 提取区域的左上角坐标
    size = (76, 150)  # 提取区域的大小
    image = cv2.imread(img_path)

    length_pixel = 258  # 横向平移像素长度
    original_img = _extract_region(image, top_left, size)

    diff_count = 0

    length = 0

    for i in range(length_pixel):
        top_left_diff = (top_left[0] + i, top_left[1])

        # 提取指定区域
        region = _extract_region(image, top_left_diff, size)
        count = _count_gray_difference(original_img, region)
        if count > diff_count:
            diff_count = count
            length = i
    if diff_count < 150:
        for i in range(length_pixel):
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
