#In this we'll learn how to split and merge color channels in opencv
import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg') #Image in BGR
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# channels_merged = cv.merge([blue,green,red])
# cv.imshow('Merged image', img)


# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)

cv.waitKey(0)