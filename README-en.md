**[简体中文](README.md)** | **English**
OpenCV + NumPy detect TikTok slider

## All files

func.py: Functional function

main.py：Test app

test_img：Test img

detect_result.txt：Test result

## Steps

Calculate the number of pixels meet the specified gray value conditions

```python
## ./func.py

# Calculate the grayscale difference
def _count_gray_difference(image1, image2):
    # Convert to grayscale images
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Convert grayscale images to NumPy arrays
    gray1 = gray1.astype(np.int32)
    gray2 = gray2.astype(np.int32)

    # Calculate the grayscale condition
    condition = (
            (gray1 > 1.975 * gray2) &
            (gray1 < 2.025 * gray2) &
            (np.abs(gray1 - 2 * gray2) <= 2)
    )

    # Count the number of pixels that satisfy the condition
    count = np.sum(condition)

    return count

```

Calculate the number of pixels meet the specified color value conditions

```python
## ./func.py

# Calculate the color difference
def _count_color_difference(image1, image2):
    # Extract the blue channel (index 0)
    blue1 = image1[:, :, 0].astype(np.int32)
    blue2 = image2[:, :, 0].astype(np.int32)

    # Calculate the boolean matrix that satisfies the condition
    condition = (blue1 > 1.6 * blue2) & (blue1 < 2.5 * blue2)

    # Count the number of pixels that satisfy the condition
    count = np.sum(condition)

    return count

```

