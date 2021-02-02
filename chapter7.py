import cv2
import numpy as np

#           Color detection


img = cv2.imread('resources/lambo.png')

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # as such the range of HSV is 0-360 but its 0-179 in Open CV
cv2.imshow('original', img)
cv2.imshow('HSV', imgHSV)
cv2.waitKey(0)