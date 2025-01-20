import cv2
import numpy as np
img = cv2.imread("kopek.jpg")

cv2.line(img,(0,0),(300,300),(0,0,255),5)
cv2.rectangle(img,(0,0),(300,300),(0,0,255),5)
cv2.circle(img,(150,150),150,(0,255,0),5)
cv2.putText(img,"OpenCV",(0,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5)

cv2.imshow("kopek2", img)

cv2.waitKey(0)
cv2.destroyAllWindows()