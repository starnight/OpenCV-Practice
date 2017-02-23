#!/bin/env python3

import numpy as np
import cv2
from matplotlib import pyplot as plt

x = np.uint8([250])
y = np.uint8([10])

# OpenCV add would be saturated: 250 + 10 = 260 => 255
print("cv2.add: {0} + {1} => {2}".format(x, y, cv2.add(x, y)))

# General add would be overflow: 250 + 10 = 260 => 4
print("General add: {0} + {1} => {2}".format(x, y, x+y))


# The image is OpenCV logo and Lenna
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image files into img
logo = cv2.imread("opencv-logo-white.png")
lenna = cv2.imread("lenna_std.jpg")[20:242, 50:230, :]

# Blending: dst = alpha x logo + beta x lenna + gamma
alpha = 0.3
beta = 0.7
gamma = 0
dst = cv2.addWeighted(logo, alpha, lenna, beta, gamma)

# Show images
plt.subplot(131), plt.imshow(logo), plt.title("OpenCV Logo")
plt.axis("off")
plt.subplot(132), plt.imshow(lenna), plt.title("Lenna")
plt.axis("off")
plt.subplot(133), plt.imshow(dst), plt.title("Blended")
plt.axis("off")

plt.show()
