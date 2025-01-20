import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = frame[100:300,100:300]
    kernel = np.ones((16,16))/25
    img2 = cv2.filter2D(frame, -1, kernel)
    cv2.imshow('frame2', img2)
    cv2.blur(frame, (16,16), frame)
    frame2 = frame.copy()
    frame3 = frame.copy()
    cv2.GaussianBlur(frame, (15,15),1.0, frame2)
    cv2.medianBlur(frame, 15, frame3)
    cv2.imshow('frame', frame)
    cv2.imshow('frame3', frame2)
    cv2.imshow('frame4', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 0xFF
# 0o77
# 0b111