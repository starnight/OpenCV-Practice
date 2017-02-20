#!/bin/env python3

import numpy as np
import cv2

# The image
img = 0

drawing = False # True if mouse is pressed
mode = True # Draw a rectangle, if it is true.  Press 'm' to toggle to curve
ix, iy = -1, -1

# Mouse callback function
def draw_circle(event, x, y, flags, param):
	global img, ix, iy, drawing, mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				top_left = (ix, iy)
				down_right = (x, y)
				color = (0, 255, 0)
				thickness = -1
				cv2.rectangle(img, top_left, down_right, color, thickness)
			else:
				center = (x, y)
				radius = 5
				color = (0, 0, 255)
				thickness = -1
				cv2.circle(img, center, radius, color, thickness)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False

if __name__ == '__main__':
	# Create a black image, a window and bind the function to window
	img = np.zeros((512,512,3), np.uint8)
	window_name = 'Paint Brush'
	cv2.namedWindow(window_name)
	cv2.setMouseCallback(window_name, draw_circle)

	# Detect the mouse events and draw
	while(1):
		cv2.imshow(window_name, img)
		k = cv2.waitKey(20) & 0xFF
		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break

	cv2.destroyAllWindows()
