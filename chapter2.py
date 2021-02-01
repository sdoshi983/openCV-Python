import cv2
import numpy as np

#                   Basic Functions :

# Original to Gray image
img = cv2.imread('resources/images.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # cvtColor function stands for convertColor
# cv2.imshow('Gray Image', imgGray)

# Bluring the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)      # kSize parameter should be (odd,odd) only. For eg, (3,3), (5,5), (7,7)
# cv2.imshow('Blur Image', imgBlur)

# detecting only edges in the original image
imgCanny = cv2.Canny(img, 100, 100)     # Canny function is used to detect edges in our image
# cv2.imshow('Canny Image', imgCanny)

# Dilation: while creating canny images, sometimes the lines are broken because of the less width of the edges
kernel = np.ones((5,5), np.uint8)       # kernel is a matrix. (5,5) is the size of the matrix and unit8(unsigned int of 8 bit(0,255) ) is the type of the object
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)        # iterations equals how many times we want the kernel to iterate, i.e. it affects the thinkness of the edges
cv2.imshow('Dilation Image', imgDilation)

# Erosion: it is opposite of dilation, i.e. it thinners the edges
imgErosion = cv2.erode(imgCanny, kernel, iterations=1)
cv2.imshow('Erosion image', imgErosion)
cv2.waitKey(0)