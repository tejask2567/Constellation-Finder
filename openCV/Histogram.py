from turtle import width
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/Sample6.tif')
blank = np.zeros(img.shape[:2], dtype='uint8')


def rescaleframe(frame, scale=.135):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', rescaleframe(gray))
cv.imshow('Star', rescaleframe(img))

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


cv.line(img, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', rescaleframe(img))


threshold, thresh = cv.threshold(
    gray, 254.9, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', rescaleframe(thresh))

cv.waitKey(0)
