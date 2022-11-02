import cv2

img = cv2.imread('1.jpeg')
print(img.shape)
img = cv2.resize(img,(500,800))

cv2.imshow('1',img)
cv2.waitKey(0)