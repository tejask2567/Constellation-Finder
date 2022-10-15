from turtle import width
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Images/Sample6.tif')

blank = np.zeros(img.shape[:2], dtype='uint8')


def rescaleframe(frame, scale=0.135):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_rescale = rescaleframe(img)
cv.imshow('Star', img_rescale)


plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
