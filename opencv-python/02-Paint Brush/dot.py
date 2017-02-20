#!/bin/env python3

import numpy as np
import cv2

# List the events in cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# The image
img = 0

# Mouse callback function
def draw_circle(event, x, y, flags, param):
	global img

	if event == cv2.EVENT_LBUTTONDBLCLK:
		center = (x, y)
		radius = 100
		color = (255, 0, 0)
		thickness = -1
		cv2.circle(img, center, radius, color, thickness)

if __name__ == '__main__':
	# Create a black image, a window and bind the function to window
	img_size = (512,	# X size
				512,	# Y size
				3)		# 3 bytes for RGB color domain
	bits = np.uint8		# Bits for each pixel
	img = np.zeros(img_size, bits)
	window_name = 'Paint Brush'
	cv2.namedWindow(window_name)
	cv2.setMouseCallback(window_name, draw_circle)

	# Detect the mouse double click event and draw a blue circle
	while(1):
		cv2.imshow(window_name, img)
		if cv2.waitKey(20) & 0xFF == 27:
			break

	cv2.destroyAllWindows()
