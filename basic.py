import cv2 as cv

img = cv.imread('Photos/cat.jpg') #this is a 3-channel BGR image
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #this is a 1-channel grayscale image
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)