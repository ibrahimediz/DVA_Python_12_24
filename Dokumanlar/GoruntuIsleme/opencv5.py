import cv2
import numpy as np

img = cv2.imread("bookpage.jpeg")
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY_INV)
retval3, threshold3 = cv2.threshold(img, 12, 255, cv2.THRESH_TRUNC)
retval4, threshold4 = cv2.threshold(img, 12, 255, cv2.THRESH_TOZERO)
retval5, threshold5 = cv2.threshold(img, 12, 255, cv2.THRESH_TOZERO_INV)
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(gri, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)

cv2.imshow("img", img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("threshold3", threshold3)
cv2.imshow("threshold4", threshold4)
cv2.imshow("threshold5", threshold5)
cv2.imshow("gri", gri)
cv2.imshow("th", th)

cv2.waitKey(0)
cv2.destroyAllWindows()