import cv2 as cv

# Reading Images
img = cv.imread('Photos/cat_large.jpg')

# Rescale Function
def rescaleFrame(frame, scale=0.2): #this works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#resizing image
# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# cv.waitKey(0)

#resizing videos
def changeRes(width, height): #this works for only videos
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()