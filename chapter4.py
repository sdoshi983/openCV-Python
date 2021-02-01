import cv2
import numpy as np
#           shapes and texts

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# img[:] = 255, 0, 0      # BGR
cv2.line(img, (50, 0), (50, 500), (0, 255, 0))
cv2.imshow('image', img)
cv2.waitKey(0)
