import cv2

img = cv2.imread('resources/images.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # cvtColor function stands for convertColor
# cv2.imshow('Gray Image', imgGray)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)      # kSize parameter should be (odd,odd) only. For eg, (3,3), (5,5), (7,7)
# cv2.imshow('Blur Image', imgBlur)


imgCanny = cv2.Canny(img, 100, 100)     # Canny function is used to detect edges in our image
cv2.imshow('Canny Image', imgCanny)
cv2.waitKey(0)