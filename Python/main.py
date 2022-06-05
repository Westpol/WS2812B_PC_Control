import tkinter as tk
import pygame
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)


def write_read(x):
    #arduino.write(bytes(x, 'utf-8'))
    data = arduino.readline()
    return data


while True:
    value = write_read(None)
    if value is not b'':
        value = value.decode('utf-8')
        print(value)
