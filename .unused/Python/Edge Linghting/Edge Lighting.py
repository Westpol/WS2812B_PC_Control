import pyscreenshot
from screeninfo import get_monitors
import time
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)

num_leds_right = 21
num_leds_top = 36
num_leds_left = 21
num_leds = 57
led_value_r = [0]*num_leds
led_value_g = [0]*num_leds
led_value_b = [0]*num_leds
addition = 0
hsteps = 7
vsteps = 10
startup = True

width, height = get_monitors()[0].width, get_monitors()[0].height

while 1:
    timme = time.time()

    img = pyscreenshot.grab(bbox=(0, 0, width, height), backend="mss", childprocess=False)
    for f in range(21, num_leds):
        for i in range(0, 150, hsteps):
            for k in range((f-num_leds_right) * int(width / num_leds_top), ((f-num_leds_right) + 1) * int(width / num_leds_top), vsteps):
                pixelVal = img.getpixel((k, i))
                led_value_r[f] += pixelVal[0]
                led_value_g[f] += pixelVal[1]
                led_value_b[f] += pixelVal[2]
                addition += 1

        led_value_r[f] /= addition
        led_value_g[f] /= addition
        led_value_b[f] /= addition
        addition = 0

    sent = ""
    for l in range(num_leds_right):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    for l in reversed(range(num_leds_right, num_leds_top + num_leds_right)):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    if startup:
        for d in range(5):
            arduino.write(bytes(sent + "&", 'utf-8'))
            time.sleep(0.1)
        startup = False
    else:
        arduino.write(bytes(sent + "&", 'utf-8'))
    while arduino.readline() != b'done\r\n':
        pass
    led_value_r = [0]*num_leds
    led_value_g = [0]*num_leds
    led_value_b = [0]*num_leds
    print("Current FPS: " + str(1/(time.time() - timme)))
