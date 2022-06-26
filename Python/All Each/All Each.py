import time
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)
num_leds = 78
time.sleep(2)

while 1:
    led_value_r = [255] * num_leds
    led_value_g = [255] * num_leds
    led_value_b = [255] * num_leds
    sent = ""
    for l in range(9):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    print(sent)
    arduino.write(bytes(sent + "a", 'utf-8'))
    while arduino.readline() != b'a\r\n':
        pass
