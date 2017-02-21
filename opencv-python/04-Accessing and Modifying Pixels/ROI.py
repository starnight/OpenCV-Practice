#!/bin/env python3

import numpy as np
import cv2

# The image is OpenCV logo
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image file into img
img = cv2.imread("opencv-logo-white.png")

# Show original image
cv2.imshow('Image ROI - Original', img)

# Have a small region of the image
reg = img[130:170, 90:120]

# Copy the small region into other region
img[0:40, 0:30] = reg

# Show the modify image
cv2.imshow('Image ROI - Modified', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
