#Color spaces in OpenCV
#color spaces are a way to represent the color channels of an image.
#Types of color spaces are: RGB, HSV, CMYK, LAB, GRAY etc.
#RGB: Red, Green, Blue
#HSV: Hue, Saturation, Value
#CMYK: Cyan, Magenta, Yellow, Black
#LAB: Lightness, A, B
#GRAY: Gray
#In OpenCV, we can convert images to different color spaces using cvtColor() function.
#cv2.cvtColor(image, flag)
#flag is the color space conversion code.
#For example, to convert an image to grayscale, we can use cv2.COLOR_BGR2GRAY.
#To convert an image to HSV, we can use cv2.COLOR_BGR2HSV.
#To convert an image to LAB, we can use cv2.COLOR_BGR2LAB.
#To convert an image to RGB, we can use cv2.COLOR_BGR2RGB.
#To convert an image to CMYK, we can use cv2.COLOR_BGR2CMYK.
#To convert an image to Gray, we can use cv2.COLOR_BGR2GRAY.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

#Gray
#gray scale images basically show you the distribution of pixels intensities at particular location of your image.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# plt.imshow(rgb)
# plt.show()

#we cannot convert gray scale image to hsv directly. We can do it by Gray -> BGR and BGR -> HSV

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV2BGR', hsv_bgr)




cv.waitKey(0)
