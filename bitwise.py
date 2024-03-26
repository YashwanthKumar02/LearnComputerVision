import cv2 as cv
import numpy as np

#bitwise operations are used to combine two images using a logical operator. The logical operator can be AND, OR, XOR, or NOT.


blank = np.zeros((400,400), dtype='uint8')
cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) #-1 to fill the rectangle
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND
#This operation takes two images as input and outputs an image where the pixel values are set to 255 if both input images have a pixel value of 255 at that location. Otherwise, the pixel value is set to 0.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#bitwise OR
#This operation takes two images as input and outputs an image where the pixel values are set to 255 if either input image has a pixel value of 255 at that location. Otherwise, the pixel value is set to 0.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR
#This operation takes two images as input and outputs an image where the pixel values are set to 255 if only one of the input images has a pixel value of 255 at that location. Otherwise, the pixel value is set to 0.
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise NOT
#This operation takes a single image as input and outputs an image where the pixel values are inverted. That is, if the input image has a pixel value of 255 at a location, the output image will have a pixel value of 0 at that location, and vice versa.
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)



cv.waitKey(0)