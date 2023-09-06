import cv2
import numpy as np

img = cv2.imread('./Assets/car.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
canvas = np.zeros(img.shape, np.uint8)

height, width, channel = img.shape

# SmallerImg
smallImg = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Conversion
GrayImg = cv2.cvtColor(smallImg, cv2.COLOR_BGR2GRAY)
LabImg = cv2.cvtColor(smallImg, cv2.COLOR_BGR2LAB)
HSVImg = cv2.cvtColor(smallImg, cv2.COLOR_BGR2HSV)

canvas[ :height//2, :width//2 ] = smallImg
# canvas[ :height//2, width//2: ] = GrayImg
canvas[ height//2: , :width//2] = LabImg
canvas[ height//2:, width//2: ] = HSVImg

cv2.imshow('Demo', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()