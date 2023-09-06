import cv2

# BGR color channel
# -1 =cv2.IMREAD_COLOR
# 0 = cv2.IMREAD_GRAYSCALE
# 1 =cv2.IMREAD_UNCHANGED

img = cv2.imread('Assets/car.png', 0)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('Render/car_new.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()