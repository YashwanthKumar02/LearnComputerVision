#we generally smooth an image to reduce noise. We can do this using a technique called blurring. Noise is caused by the camera sensor, and can be reduced by blurring the image.
#There are many types of blurring techniques, such as Gaussian blur, median blur, and bilateral blur. We'll look at Gaussian blur in this example.
#Gaussian blur is a type of image-blurring technique that uses a Gaussian function to blur the image. The Gaussian function is a bell-shaped curve that represents the distribution of values in the image.
#The Gaussian function is defined as:

import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#the average of kernel pixels is calculated and the center pixel is replaced with this average value. This is done for all pixels in the image.

#Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#each surrounding pixel is multiplied by a weight and the center pixel is replaced with the sum of these weighted values. This is done for all pixels in the image.

#Gaussian Blur (less blurring than avergaing method, but guassian is more natural)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#each surrounding pixel is sorted and the center pixel is replaced with the median value. This is done for all pixels in the image.

#Median Blur (More effective in reducing noise in an image as compared avergaing and even guassian blur)
median = cv.medianBlur(img, 3) #assumes as (7,7) as kernel size automatically
cv.imshow('Median Blur', median) #median blurring is not meant to be used for reducing noise in an image, but rather for reducing the sharpness of edges in an image.
#median blurring is not meant to be used for high kernel sizes, as it can cause the image to become too blurry. as 5 and 7

#each surrounding pixel is multiplied by a weight and the center pixel is replaced with the sum of these weighted values. The weights are calculated based on the difference between the center pixel and the surrounding pixels. This is done for all pixels in the image.

#Bilateral Blur (More effective in reducing noise in an image as compared avergaing and even guassian blur, used in advance image processing)
#Bilateral blurring blurs the image but retains the edges in the image. This is done by using two Gaussian functions: one for the spatial domain and one for the intensity domain. The spatial domain Gaussian function is used to blur the image, while the intensity domain Gaussian function is used to retain the edges in the image.
bilateral = cv.bilateralFilter(img, 10, 35, 25) #higher sigma color value, more color will be considered within the pixel neighborhood
#high sigma space value, pixels farther out from the center pixel will influence the blurring
#d is the diameter of each pixel neighborhood
cv.imshow('Bilateral Blur', bilateral)



cv.waitKey(0)