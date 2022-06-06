import tkinter as tk
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)


def show_values():
    print(w1.get(), w2.get(), w3.get())


def printstuff():
    r, g, b, rgbb = w1.get(), w2.get(), w3.get(), w4.get()
    return r, g, b, rgbb


master = tk.Tk()
w1 = tk.Scale(master, from_=255, to=0)
w1.pack(side=tk.RIGHT)
w2 = tk.Scale(master, from_=255, to=0)
w2.pack(side=tk.RIGHT)
w3 = tk.Scale(master, from_=255, to=0)
w3.pack(side=tk.RIGHT)
w4 = tk.Scale(master, from_=255, to=0)
w4.pack()
tk.Button(master, text='Show', command=show_values).pack()

while 1:
    brightness, red, green, blue = printstuff()
    arduino.write(bytes("{2}${1}${0}${3}$".format(str(red), str(green), str(blue), str(brightness)), 'utf-8'))
    print(bytes("{0}${1}${2}${3}$".format(str(red), str(green), str(blue), str(brightness)), 'utf-8'))
    time.sleep(0.001)
    master.update()
