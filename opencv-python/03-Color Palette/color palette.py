#!/bin/env python3

import numpy as np
import cv2

# A dummy function
def nothing(x):
	pass

# Create a window
window_name = 'Color Pallete'
cv2.namedWindow(window_name)

# Create a black image
img_size = (300,	# X size
			512,	# Y size
			3)		# 3 bytes for RGB color domain
bits = np.uint8		# Bits for each pixel
img = np.zeros(img_size, bits)

# Create trackbars for color change
cv2.createTrackbar('R', window_name, 0, 255, nothing)
cv2.createTrackbar('G', window_name, 0, 255, nothing)
cv2.createTrackbar('B', window_name, 0, 255, nothing)

# Create a switch for ON/OFF functionality
cv2.createTrackbar('0: OFF\n1: ON', window_name, 0, 1, nothing)

while(1):
	cv2.imshow(window_name, img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	# Get current position of 4 trackbars
	r = cv2.getTrackbarPos('R', window_name)
	g = cv2.getTrackbarPos('G', window_name)
	b = cv2.getTrackbarPos('B', window_name)
	s = cv2.getTrackbarPos('0: OFF\n1: ON', window_name)

	# Fill the image with the color
	if s == 0:
		img[:] = 0
	else:
		img[:] = [b, g, r]

cv2.destroyAllWindows()
