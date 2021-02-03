import cv2
import numpy as np

#           Contours / shape detection

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

                if len(imgArray[x][y].shape) == 2:      # if it is a gray image then converting it to BGR
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)     # creating a matrix with all zeros
        horizontal = [imageBlank] * rows
        for x in range(0, rows):
            horizontal[x] = np.hstack(imgArray[x])      # stacking images horizontally
        vertical = np.vstack(horizontal)        # stacking all the horizontally stacked images (rows) to vertically (columns)
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


img = cv2.imread('resources/shapes.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgStack = stackImages(0.6, ([img, imgGray, imgBlur]))
cv2.imshow('stack', imgStack)
cv2.waitKey(0)
