import pyscreenshot
from screeninfo import get_monitors
import time
import serial

arduino = serial.Serial(port='COM3', baudrate=230400, timeout=.001)

num_leds_right = 21
num_leds_top = 36
num_leds_left = 21
num_leds = 78
led_value_r = [0] * num_leds
led_value_g = [0] * num_leds
led_value_b = [0] * num_leds
addition = 0
hsteps = 7
vsteps = 10
startup = True

width, height = get_monitors()[0].width, get_monitors()[0].height

time.sleep(3)

while 1:
    timme = time.time()

    """img = pyscreenshot.grab(bbox=(0, 0, width, height), backend="mss", childprocess=False)
    for f in range(num_leds_right, num_leds_right + num_leds_top):
        for i in range(0, 150, hsteps):
            for k in range((f - num_leds_right) * int(width / num_leds_top),
                           ((f - num_leds_right) + 1) * int(width / num_leds_top), vsteps):
                pixelVal = img.getpixel((k, i))
                led_value_r[f] += pixelVal[0]
                led_value_g[f] += pixelVal[1]
                led_value_b[f] += pixelVal[2]
                addition += 1

        led_value_r[f] /= addition
        led_value_g[f] /= addition
        led_value_b[f] /= addition
        addition = 0"""

    sent = ""
    for l in range(0, 10):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "a", 'utf-8'))
    while arduino.readline() != b'a\r\n':
        pass
    sent = ""
    for l in range(10, 20):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "b", 'utf-8'))
    while arduino.readline() != b'b\r\n':
        pass
    sent = ""
    for l in range(20, 30):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "c", 'utf-8'))
    while arduino.readline() != b'c\r\n':
        pass
    sent = ""
    for l in range(30, 40):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "d", 'utf-8'))
    while arduino.readline() != b'd\r\n':
        pass
    sent = ""
    for l in range(40, 50):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "e", 'utf-8'))
    while arduino.readline() != b'e\r\n':
        pass
    sent = ""
    for l in range(60, 70):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "f", 'utf-8'))
    while arduino.readline() != b'f\r\n':
        pass
    sent = ""
    for l in range(70, 78):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "g", 'utf-8'))
    while arduino.readline() != b'l\r\n':
        pass
    led_value_r = [100] * num_leds
    led_value_g = [100] * num_leds
    led_value_b = [100] * num_leds
    print("Current FPS: " + str(1 / (time.time() - timme)))
