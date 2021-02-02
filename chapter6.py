import cv2
import numpy as np

img = cv2.imread('resources/images.jpg')
imgHorizontal = np.hstack((img, img))
cv2.imshow('horizontal', imgHorizontal)
cv2.waitKey(0)