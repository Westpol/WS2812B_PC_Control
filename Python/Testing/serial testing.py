import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)


def write_read(x):
    arduino.write(bytes("{0}${1}${2}$".format("255", "255", "255"), 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(str(value))
