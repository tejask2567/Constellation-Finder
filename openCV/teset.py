import cv2
import numpy as np


def rescaleframe(frame, scale=.135):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


# read image as grayscale
img = cv2.imread('Images/Sample6.tif')
hh, ww = img.shape[:2]

# shave off white region on right side
img = img[0:hh, 0:ww-2]

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# median filter
median = cv2.medianBlur(gray, 3)

# do canny edge detection
canny = cv2.Canny(median, 254, 250)
# transpose canny image to compensate for following numpy points as y,x
canny_t = cv2.transpose(canny)

# get canny points
# numpy points are (y,x)
points = np.argwhere(canny_t > 0)

# fit ellipse and get ellipse center, minor and major diameters and angle in degree
ellipse = cv2.fitEllipse(points)
(x, y), (d1, d2), angle = ellipse
print('center: (', x, y, ')', 'diameters: (', d1, d2, ')')

# draw ellipse
result = img.copy()
cv2.ellipse(result, (int(x), int(y)), (int(d1/2), int(d2/2)),
            angle, 0, 360, (0, 0, 0), 1)

# draw circle on copy of input of radius = half average of diameters = (d1+d2)/4
rad = int((d1+d2)/4)
xc = int(x)
yc = int(y)
print('center: (', xc, yc, ')', 'radius:', rad)
cv2.circle(result, (xc, yc), rad, (0, 255, 0), 1)

# write results
cv2.imwrite("sunset_canny_ellipse.jpg", canny)
cv2.imwrite("sunset_ellipse_circle.jpg", result)

# show results
cv2.imshow("median", rescaleframe(median))
cv2.imshow("canny", rescaleframe(canny))
cv2.imshow("result", rescaleframe(result))
cv2.waitKey(0)
