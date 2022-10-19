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

# important
""" gray_new = cv.cvtColor(img_new, cv.COLOR_BGR2GRAY)
ret_new, thresh_new = cv.threshold(gray_new, 253, 255, cv.THRESH_BINARY)
contous, hierarchy = cv.findContours(thresh_new, cv.RETR_EXTERNAL,
                                     cv.CHAIN_APPROX_SIMPLE)

gray_new_2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret_new_2, thresh_new_2 = cv.threshold(gray_new_2, 253, 255, cv.THRESH_BINARY)
contous_2, hierarchy_2 = cv.findContours(thresh_new_2, cv.RETR_EXTERNAL,
                                         cv.CHAIN_APPROX_SIMPLE)
comt_diff = cv.matchShapes(contous[0], contous_2[0], cv.CONTOURS_MATCH_I1,0)
print(comt_diff) """


cv.waitKey(0)
