#!/bin/env python3

import numpy as np
import cv2

# The image is OpenCV logo
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image file into img
img = cv2.imread("opencv-logo-white.png")

# Access a pixel
p = img[150, 110]
print("Pixel [150, 110]'s B: {0}, G: {1}, R: {2}".format(p[0], p[1], p[2]))

# Accessing only the blue pixel
pBlue = img[150, 110, 0]
print("Pixel [150, 110]'s blue: {0}".format(pBlue))

# Modify a pixel
img[150, 110] = [0, 255, 255]
p = img[150, 110]
print("Pixel [150, 110]'s B: {0}, G: {1}, R: {2}".format(p[0], p[1], p[2]))

# Access red value with better method
pRed = img.item(150, 80, 2)
print("Pixel [150, 80]'s red: {0}".format(pRed))

# Modify red value with better method
img.itemset((150, 80, 2), 100)
pRed = img.item(150, 80, 2)
print("Pixel [150, 80]'s red: {0}".format(pRed))

# Show the shape of the image
print("X, Y pixels: {0}, {1}px, channels: {2}".format(img.shape[1], img.shape[0], img.shape[2]))

# Total image size
print("The image has {0} pixels".format(img.size))

# Data-type of each pixel's channel
print("The data type of each pixel's channel: {0}".format(img.dtype))
