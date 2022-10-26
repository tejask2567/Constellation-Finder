from imutils import contours
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
import imutils

img = cv.imread('Images\Leo.tif')
img_new = cv.imread('Images/leo2.jpg')


def rescaleframe(frame, scale=.18):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def rotate(img, angle, rotPoint=None):

    (height, width) = img.shape[:2]
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

for label in np.unique(labels):

    if label == 0:
        continue

    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv.countNonZero(labelMask)

    if numPixels > 300:
        mask = cv.add(mask, labelMask)


cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
                       cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = contours.sort_contours(cnts)[0]

lst = []
lst2 = []


for (i, c) in enumerate(cnts):

    (x, y, w, h) = cv.boundingRect(c)
    ((cX, cY), radius) = cv.minEnclosingCircle(c)
    cv.circle(img, (int(cX), int(cY)), int(radius),
              (0, 0, 255), 5)
    cv.putText(img, "#{}".format(i + 1), (x, y - 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    lst.append(int(cX))
    lst2.append(int(cY))

mat_cX = np.asarray(lst)
mat_cY = np.asarray(lst2)
matf = np.column_stack((mat_cX, mat_cY))

for index, item in enumerate(matf):
    if index == len(matf) - 1:
        break
    cv.line(img, item, matf[index + 1], [0, 255, 0], 5)
cv.line(img, matf[0], matf[len(matf)-1], [0, 255, 0], 5)

gray_new = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('img at .jpg', gray_new)


cv.waitKey(0)
