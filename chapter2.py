import cv2

img = cv2.imread('resources/images.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # cvtColor function stands for convertColor
cv2.imshow('Gray Image', imgGray)
cv2.waitKey(0)