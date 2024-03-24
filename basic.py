import cv2 as cv

img = cv.imread('Photos/cat.jpg') #this is a 3-channel BGR image
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #this is a 1-channel grayscale image
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175) #canny edge detection
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated', dilated)

#Eroding
eroding = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('Eroded', eroding)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]

cv.waitKey(0)