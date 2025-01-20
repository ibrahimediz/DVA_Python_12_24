import serial
import time

ser = serial.Serial('COM3',9600,timeout=1)


if ser.is_open:
    print("Port Açık")
else:
    ser.open()

while True:
    sensor_data = read_sensor()
    ser.write(sensor_data.encode('utf-8'))
            
    if ser.in_waiting > 0:
        gelen_veri = ser.read(ser.in_waiting.decode('utf-8'))
        print(gelen_veri)
    time.sleep(1)
