#!/bin/env python3

import numpy as np
import cv2

# The image is OpenCV logo
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image file into img
img = cv2.imread("opencv-logo-white.png")

# Show original image
cv2.imshow("Image Splitting & Merging - Original", img)

# Use split method to have RGB channels seperatly (Costly)
b, g, r = cv2.split(img)

# Merge the splitted channels
img = cv2.merge((r, b, g))

# Show the shifted color image
cv2.imshow("Image Splitting & Merging - Shifted", img)

# Use numpy indexing for more efficient
img[:, :, 2] = 127

# Show the modified color image
cv2.imshow("Image Splitting & Merging - Modified", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
