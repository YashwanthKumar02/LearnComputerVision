import cv2 as cv
import numpy as np

# Reading Images
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#translation function
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)



cv.waitKey(0)