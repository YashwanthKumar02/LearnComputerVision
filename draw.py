import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')



#1. paint the image a certain color
blank[200:300, 300:400] = 255,255,0


#2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)


#3. Draw a circle
cv.circle(blank, (250,250), 100, (255,0,0), thickness=cv.FILLED)


#4. Draw a line
cv.line(blank, (0,0), (250,250), (255,0,0), thickness=2)

#5. write text on an image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)

cv.imshow('Line', blank)

cv.waitKey(0)