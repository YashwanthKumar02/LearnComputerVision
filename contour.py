import cv2 as cv
import numpy as np

#Contours are the boundaries of an object. They are useful in object detection and shape analysis.

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# #canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Thresholding
# ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

#Contours
contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)