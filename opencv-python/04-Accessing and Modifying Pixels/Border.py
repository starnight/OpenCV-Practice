#!/bin/env python3

import numpy as np
import cv2
from matplotlib import pyplot as plt

# The image is OpenCV logo
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image file into img
img = cv2.imread("opencv-logo-white.png")

# The color of pyplot is [R, G, B]
border_color = [255, 0, 0]

# Make different borders
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=border_color)

# Show images with borders
plt.subplot(231), plt.imshow(img, "gray"), plt.title("ORIGINAL")
plt.subplot(232), plt.imshow(replicate, "gray"), plt.title("REPLICATE")
plt.subplot(233), plt.imshow(reflect, "gray"), plt.title("REFLECT")
plt.subplot(234), plt.imshow(reflect101, "gray"), plt.title("REFLECT 101")
plt.subplot(235), plt.imshow(wrap, "gray"), plt.title("WRAP")
plt.subplot(236), plt.imshow(constant, "gray"), plt.title("CONSTANT")

plt.show()
