#!/bin/env python3

import numpy as np
import cv2

# The image is OpenCV logo and Lenna
# https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png

# Read the image files into img
logo = cv2.imread("opencv-logo-white.png")
lenna = cv2.imread("lenna_std.jpg")

# Create an ROI of the logo which is going to put on Lenna picture
rows, cols, channels = logo.shape
roi = lenna[0:rows, 0:cols]
cv2.imshow("ROI", roi)

# Create the mask and inverse mask of the logo
logo2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
cv2.imshow("BGR to GRAY", logo2gray)
threshold = 10
maxValue = 255
ret, mask = cv2.threshold(logo2gray, threshold, maxValue, cv2.THRESH_BINARY)
cv2.imshow("Mask", mask)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("Inverse Mask", mask_inv)

# Make ROI as background
roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Make logo as foreground
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)

# Merge background and foreground
dst = cv2.add(roi_bg, logo_fg)

# Merge the dst into main Lenna picture
lenna[0:rows, 0:cols] = dst

cv2.imshow("Logo - Lenna", lenna)
cv2.waitKey(0)
cv2.destroyAllWindows()
