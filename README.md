**简体中文** | **[English](README-en.md)**
使用OpenCV处理图像，NumPy加速的抖音验证码破解

## 文件结构

func.py：功能函数

main.py：实现测试用例

test_img：测试图片

detect_result.txt：测试结果

## 实现步骤

计算原始图像区域与目标区域满足指定灰度值条件的像素数量

```python
## ./func.py

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
```

计算原始图像区域与目标区域满足指定颜色值条件的像素数量

```python
## ./func.py

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
```

