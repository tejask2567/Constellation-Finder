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


# joining prefix str and added value
pattern = re.compile('\d+')
string = 'img at 0'
imge = True
while imge:  # replace your loop condition here
    match = re.search(pattern, string)
    if match:
        match = int(match.group())
        if match > 300:  # arbitrary condition just to break the loop
            imge = False
        else:
            match += 60
            rotated = rotate(img, match)
            string = re.sub(pattern, str(match), string)

    cv.imwrite(string+'.jpg', rotated)
    print(string)
cv.waitKey(0)
