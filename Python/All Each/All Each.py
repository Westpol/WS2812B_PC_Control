import pyscreenshot
from screeninfo import get_monitors
import time
import serial

arduino = serial.Serial(port='COM3', baudrate=230400, timeout=.001)
num_leds = 78

num_leds_right = 21
num_leds_top = 36
num_leds_left = 21

addition = 0
hsteps = 7
vsteps = 10
hdist = 100
vdist = 100

width, height = get_monitors()[0].width, get_monitors()[0].height

time.sleep(2)

while 1:

    timme = time.time()
    led_value_r = [0] * num_leds
    led_value_g = [0] * num_leds
    led_value_b = [0] * num_leds

    img = pyscreenshot.grab(bbox=(0, 0, width, height), backend="mss", childprocess=False)
    for f in range(num_leds_right, num_leds_right + num_leds_top):
        for i in range(0, hdist, hsteps):
            for k in range(int(width / num_leds_top) * ((num_leds_right + num_leds_top) - (f + 1)), int(width /
                    num_leds_top) * ((num_leds_right + num_leds_top) - f), vsteps):
               pixelVal = img.getpixel((k, i))
               led_value_r[f] += pixelVal[0]
               led_value_g[f] += pixelVal[1]
               led_value_b[f] += pixelVal[2]
               addition += 1

        led_value_r[f] /= addition
        led_value_g[f] /= addition
        led_value_b[f] /= addition
        addition = 0

    for f in range(0, num_leds_right):
        for i in range(width - vdist, width, vsteps):
            for k in range(int(height / num_leds_right) * (num_leds_right - (f + 1)), int(height / num_leds_right) * (num_leds_right - f), hsteps):
                pixelVal = img.getpixel((i, k))
                led_value_r[f] += pixelVal[0]
                led_value_g[f] += pixelVal[1]
                led_value_b[f] += pixelVal[2]
                addition += 1

        led_value_r[f] /= addition
        led_value_g[f] /= addition
        led_value_b[f] /= addition
        addition = 0

    sent = ""
    for l in range(10):
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
    for l in range(50, 60):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "f", 'utf-8'))
    while arduino.readline() != b'f\r\n':
        pass
    sent = ""
    for l in range(60, 70):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "g", 'utf-8'))
    while arduino.readline() != b'l\r\n':
        pass
    print("Current FPS: {0}".format(1 / (time.time() - timme)))
