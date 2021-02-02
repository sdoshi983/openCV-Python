import cv2
import numpy as np

#       Joining images

img = cv2.imread('resources/images.jpg')
imgHorizontal = np.hstack((img, img))   # hstack stands for horizontal stack and it accepts a tuple and the elements of tuples are children of stack which are placed horizontally
# cv2.imshow('horizontal', imgHorizontal)

imgVertical = np.vstack((img, img))
# cv2.imshow('vertical', imgVertical) # here, the elements are stacked vertically


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
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == img[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)

                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        horizontal = [imageBlank] * rows
        for x in range(0, rows):
            horizontal[x] = np.hstack(imgArray[x])
        vertical = np.vstack(horizontal)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        horizontal = np.hstack(imgArray)
        vertical = horizontal
    return vertical


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))
cv2.imshow('image', img)
cv2.imshow('stack', imgStack)
cv2.waitKey(0)