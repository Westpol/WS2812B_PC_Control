import pyscreenshot
from screeninfo import get_monitors
import time
import serial

arduino = serial.Serial(port='COM16', baudrate=921600, timeout=.001)
num_leds = 78

num_leds_right = 21
num_leds_top = 36
num_leds_left = 21

addition = 0
hsteps = 5
vsteps = 5
hdist = 75
vdist = 75

width, height = get_monitors()[0].width, get_monitors()[0].height

last_led_value_r = [0] * num_leds
last_led_value_g = [0] * num_leds
last_led_value_b = [0] * num_leds

alphabet = "abcdefghijklmnopqrstuvwxyz"

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

    '''for i in range(num_leds):
        if -1 > (led_value_r[i] - last_led_value_r[i]) or (led_value_r[i] - last_led_value_r[i]) < 1:
            if (led_value_r[i] - last_led_value_r[i]) > 1:
                led_value_r[i] = last_led_value_r[i] + 1
            else:
                led_value_r[i] = last_led_value_r[i] - 1
        if -1 > (led_value_g[i] - last_led_value_g[i]) or (led_value_g[i] - last_led_value_g[i]) < 1:
            if (led_value_g[i] - last_led_value_g[i]) > 1:
                led_value_g[i] = last_led_value_g[i] + 1
            else:
                led_value_g[i] = last_led_value_g[i] - 1
        if -1 > (led_value_b[i] - last_led_value_b[i]) or (led_value_b[i] - last_led_value_b[i]) < 1:
            if (led_value_b[i] - last_led_value_b[i]) > 1:
                led_value_b[i] = last_led_value_b[i] + 1
            else:
                led_value_b[i] = last_led_value_b[i] - 1
        last_led_value_r[i] = led_value_r[i]
        last_led_value_g[i] = led_value_g[i]
        last_led_value_b[i] = led_value_b[i]'''

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

    for i in range(0, 7):
        sent = ""
        for l in range(i * 10, (i + 1) * 10):
            sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
        arduino.write(bytes(sent + alphabet[i], 'utf-8'))
        while 1:
            serialIn = arduino.readline()
            if serialIn == b'l\r\n' or serialIn == bytes(alphabet[i] + "\r\n", 'utf-8'):
                break
    print("Current FPS: {0}".format(1 / (time.time() - timme)))
