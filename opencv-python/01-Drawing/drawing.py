#!/bin/env python3

import numpy as np
import cv2

# Create a black image
img_size = (512,	# X size
			512,	# Y size
			3)		# 3 bytes for RGB color domain
bits = np.uint8		# Bits for each pixel
img = np.zeros(img_size, bits)

# Draw a diagonal blue line with thickness of 5px
start = (0, 0)		# Line starts at
end = (511, 511)	# Line ends at
color = (255, 0, 0)	# Color of the line
thickness = 5		# Thickness with pixels
img = cv2.line(img, start, end, color, thickness)

# Draw a green rectangle with thickness of 3px
top_left = (384, 0)		# Top-left corner
down_right = (510, 128)	# Down-right corner
color = (0, 255, 0)		# Color of the rectangle
thickness = 5			# Thickness with pixels
img = cv2.rectangle(img, top_left, down_right, color, thickness)

# Draw a red circle
center = (447, 65)		# Center
radius = 63				# Radius
color = (0, 0, 255)		# Color of the circle
thickness = 3			# Thickness with pixels
img = cv2.circle(img, center, radius, color, thickness)

# Draw a blue-green ellipse
center = (256, 256)		# Center
axes = (100,50)			# Ellipse's X and Y axes' length
rotation = 0			# Ratation angle of the ellipse
start_angle = 0			# Ellipse arc's start angle
end_angle = 180			# Ellipse arc's end angle
color = (255, 255, 0)	# Color of the ellipse
thickness = -1			# Thickness with pixels. If it is negtive, then it will be filled
img = cv2.ellipse(img, center, axes, rotation, start_angle, end_angle, color, thickness)

# Draw a yellow polygon
vertexes = [[10, 5],	# Vertexes of the polygon
			[20, 30],
			[70, 20],
			[50, 10]]
flag = True				# 0: not closed polygon, 1: closed polygon
color = (0,255,255)		# Color of the polygon
pts = np.array(vertexes, np.int32)
img = cv2.polylines(img, [pts], flag, color)

# Put a white text
string = 'OpenCV'		# Text string
position = (10,500)		# Position of the text
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 3				# Scale size of the text
color = (255,255,255)	# Color of the text
thickness = 2			# Thickness with pixels
line_type = cv2.LINE_AA	# Line type of the text
cv2.putText(img, string, position, font, scale, color, thickness, line_type)

# Display the drawing example
cv2.imshow('01-Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
