#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import os
import cv2
from func import identify_length


# 识别所有图片,将结果保存到文件中
def identify_images_in_directory(directory):
    results = {}

    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(directory, filename)

            # 调用图像识别函数识别图片
            result = identify_length(image_path)
            results[filename] = result
            image = cv2.imread(image_path)

            # # 绘制矩形框
            # cv2.rectangle(image, (46, 299 - 20), (46 + result[0], 299 + 20), (0, 255, 0), 2)
            # 绘制箭头
            cv2.arrowedLine(image, (46, 299), (46 + result[0], 299), (0, 0, 255), thickness=4, line_type=3)

            # 显示结果图像
            cv2.imshow(f"{filename}", image)
            cv2.moveWindow(f"{filename}", 100, 100)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    # 将结果写入文件
    with open("detect_result.txt", "w") as f:
        for filename, result in results.items():
            f.write(f"{filename}: {result}\n")


if __name__ == '__main__':
    # 识别指定目录下的图片
    identify_images_in_directory("test_img")
