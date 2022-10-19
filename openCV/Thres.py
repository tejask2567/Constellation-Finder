from imutils import contours
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
import imutils
import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image file")
args = vars(ap.parse_args())

img = cv.imread(args["image"])


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


test_str = '0'
reg = re.compile(r'[ 0 - 9]')
mtch = reg.findall(test_str)

num = ''.join(mtch[-3:])
i = 0
add_val = 0
# joining prefix str and added value

for (i, c) in enumerate(img):
    if (i <= 300 and add_val <= 300):
        pre_str = test_str.replace(num, '')
        res = pre_str + str(add_val)
        rotated = rotate(img, i)
        cv.imwrite('img at ' + str(res) + '.jpg', rotated)
        add_val = int(num) + 60
        i += 90
    else:
        break
cv.waitKey(0)
