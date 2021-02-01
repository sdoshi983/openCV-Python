import cv2
import numpy as np

#       Resizing and cropping:

img = cv2.imread('resources/images.jpg')
print(img.shape)    # while printing, it will be in the form (height, width, bgr index)
cv2.imshow('image', img)

# resizing
resizedImg = cv2.resize(img, (200, 175))    # whereas here, it will be in the form (width, height)
print(resizedImg.shape)
cv2.imshow('resized', resizedImg)

#cropping
croppedImg = img[100:150, 100:200]      # No need of any openCV function. Here, it will be in the form [height, width]
cv2.imshow('cropped', croppedImg)
cv2.waitKey(0)

# NOTE: In CV, the form will be width, height but it will be opposite in python(i.e in print function and while cropping)