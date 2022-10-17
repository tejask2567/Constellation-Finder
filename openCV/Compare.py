from imutils import contours
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
import imutils

img = cv.imread('Images/Sample6.tif')

blank = np.zeros(img.shape, dtype='uint8')


def rescaleframe(frame, scale=.18):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


(height, width) = img.shape[:2]


def rotate(img, angle, rotPoint=None):

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


ret, thresh = cv.threshold(gray, 253, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', rescaleframe(thresh))

thresh = cv.erode(thresh, None, iterations=2)
thresh = cv.dilate(thresh, None, iterations=4)

labels = measure.label(thresh, connectivity=2, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
# loop over the unique components
for label in np.unique(labels):
    # if this is the background label, ignore it
    if label == 0:
        continue
    # otherwise, construct the label mask and count the
    # number of pixels
    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv.countNonZero(labelMask)
    # if the number of pixels in the component is sufficiently
    # large, then add it to our mask of "large blobs"
    if numPixels > 300:
        mask = cv.add(mask, labelMask)

# find the contours in the mask, then sort them from left to
# right
cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
                       cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = contours.sort_contours(cnts)[0]
# loop over the contours
for (i, c) in enumerate(cnts):
    # draw the bright spot on the image
    (x, y, w, h) = cv.boundingRect(c)
    ((cX, cY), radius) = cv.minEnclosingCircle(c)
    cv.circle(img, (int(cX), int(cY)), int(radius),
              (0, 0, 255), 3)
    cv.putText(img, "#{}".format(i + 1), (x, y - 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    print(int(cX), int(cY))
    cv.line(img, int(cX), int(cY), (255, 0, 0), thickness=3)

# show the output image
""" cv.imshow("Image", rescaleframe(img))
for (i,c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)
    cv.line(img, int(cX), (300,400), (255,255,255), thickness=3) """

cv.imshow("Image", rescaleframe(img))
cv.line(img, (720, 2635), (1855, 2587), (255, 0, 0), thickness=3)
cv.imshow("Image with line", rescaleframe(img))
cv.waitKey(0)
