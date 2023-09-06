import cv2
import random

img = cv2.imread('Assets/Car.png',1)
img = cv2.resize(img, (0,0), fx= 0.5 , fy=0.5)
tag = img[0:201, 0:201]
img[300:501, 300:501] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
