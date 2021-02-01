import cv2
import numpy as np
#           shapes and texts

# shapes
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# img[:] = 255, 0, 0      # BGR
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 5)    # img, start point, end point, color, thickness
cv2.rectangle(img, (10, 10), (100, 100), (255, 0, 0), cv2.FILLED)       # same as above
cv2.circle(img, (300, 200), 30, (0, 0, 255), 10)       #img, center, radius, color, thickness


# text
cv2.putText(img, "Shrey", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 50, 200), 3) # img, text, point, font family, scale, color, width
cv2.imshow('image', img)
cv2.waitKey(0)