import cv2
import numpy as np

#       Joining images

img = cv2.imread('resources/images.jpg')
imgHorizontal = np.hstack((img, img))   # hstack stands for horizontal stack and it accepts a tuple and the elements of tuples are children of stack which are placed horizontally
cv2.imshow('horizontal', imgHorizontal)

imgVertical = np.vstack((img, img))
cv2.imshow('vertical', imgVertical) # here, the elements are stacked vertically
cv2.waitKey(0)

# NOTE:
#   - the issue with the above method is that all the elements of the tuple should have same BGR else it will not work
#   - the images cannot be resized. If we want to stack multiple elements then we can't assign them our specific size. The size will be taken by default

# the solution to above two points is:

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)   # isinstance returns true is imgArray[0] is a type of list, else returns false
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]


