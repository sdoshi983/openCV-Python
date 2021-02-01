import cv2
import numpy as np

#       warp perspective / bird view

img = cv2.imread('resources/cards.jpg')
width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])     # four points that we want as a final output
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width,  height]])  # the size of the final output image
matrix = cv2.getPerspectiveTransform(pts1, pts2)    # getting the matrix of the image with the help of points and size
imgOutput = cv2.warpPerspective(img, matrix, (width, height))   # img, image matrix, size
cv2.imshow('image', imgOutput)
cv2.waitKey(0)