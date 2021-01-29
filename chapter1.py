import cv2

# FOR IMAGES
# img = cv2.imread('resources/images.jpg')
# cv2.imshow('Output',img)
# cv2.waitKey(0)

#       -----------------------------

# FOR VIDEOS
# cap = cv2.VideoCapture("resources/video.mp4")
#
# while True:
#     success, img = cap.read()    # read function returns the frame and boolean value if the frame was successfully returned. Hence this both are stored in img and success variable respectively
#     print(success)
#     if success:
#         cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):     #the video will be stopped on pressing 'q'
#         break

#       -----------------------------


# FOR WEBCAM
cap = cv2.VideoCapture(0)
cap.set(3, 640) # 3 is the id for width
cap.set(4, 480) # 4 is the id for height
cap.set(10, 100) # 10 is the id for brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
