import cv2
import numpy as np

#           Contours / shape detection
img = cv2.imread('resources/shapes.png')
cv2.imshow('original', img)
cv2.waitKey(0)
