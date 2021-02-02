import cv2
import numpy as np

#           Color detection

def empty(a):
    pass
img = cv2.imread('resources/lambo.png')
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # as such the range of HSV is 0-360 but its 0-179 in Open CV
cv2.imshow('original', img)
cv2.imshow('HSV', imgHSV)
cv2.waitKey(0)