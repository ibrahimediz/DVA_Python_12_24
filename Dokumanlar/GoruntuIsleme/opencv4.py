import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
