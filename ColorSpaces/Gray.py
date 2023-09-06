import cv2
import numpy as np

img = cv2.imread('./Assets/car.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Demo', GrayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()