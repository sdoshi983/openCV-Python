import cv2
import numpy as np

#       Joining images

img = cv2.imread('resources/images.jpg')
imgHorizontal = np.hstack((img, img))   # hstack stands for horizontal stack and it accepts a tuple and the elements of tuples are children of stack which are placed horizontally
cv2.imshow('horizontal', imgHorizontal)

imgVertical = np.vstack((img, img))
cv2.imshow('vertical', imgVertical)     # here, the elements are stacked vertically
cv2.waitKey(0)