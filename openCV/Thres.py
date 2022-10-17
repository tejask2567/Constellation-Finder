from turtle import width
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/Sample6.tif')

def rescaleframe(frame, scale=.135):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)