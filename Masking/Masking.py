import cv2
import numpy as np

img = cv2.imread('./Assets/car.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([105, 50,100])
upper_blue = np.array([170,255,255])


mask = cv2.inRange(hsvimg, lower_blue, upper_blue)
result = cv2.bitwise_and(img,img, mask= mask)


cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Masked Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()