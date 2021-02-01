import cv2
import numpy as np

#       Resizing and cropping:
img = cv2.imread('resources/images.jpg')
print(img.shape)
cv2.imshow('image',img)

resizedImg = cv2.resize(img, (200, 175))
print(resizedImg.shape)
cv2.imshow('resized', resizedImg)

cv2.waitKey(0)