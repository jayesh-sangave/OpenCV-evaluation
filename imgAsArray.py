import cv2

img = cv2.imread('Assets/car.png', 1)
print(img.shape)
# Resize
img2 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
print(img2.shape)
