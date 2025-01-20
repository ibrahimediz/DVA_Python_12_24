import cv2
import numpy as np
import serial 
cap = cv2.VideoCapture(0)
ser = serial.Serial("COM3",600,timeout=3)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    ser.write(frame.tobytes())


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break