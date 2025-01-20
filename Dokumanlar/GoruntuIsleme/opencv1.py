import cv2
import numpy as np
img = cv2.imread("kopek.jpg")
# img[100:200,100:200] = [0,0,0]
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)
# print(img[100:200,100:200])
cv2.imshow("kopek", gri)
cv2.imshow("kopek2", img)

cv2.waitKey(0)
cv2.destroyAllWindows()