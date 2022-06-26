import time
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)
num_leds = 78
time.sleep(2)

while 1:
    led_value_r = [99] * num_leds
    led_value_g = [99] * num_leds
    led_value_b = [99] * num_leds
    timme = time.time()
    sent = ""
    for l in range(9):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "a", 'utf-8'))
    while arduino.readline() != b'a\r\n':
        pass
    sent = ""
    for l in range(9, 19):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "b", 'utf-8'))
    while arduino.readline() != b'b\r\n':
        pass
    sent = ""
    for l in range(19, 29):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "c", 'utf-8'))
    while arduino.readline() != b'c\r\n':
        pass
    sent = ""
    for l in range(29, 39):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "d", 'utf-8'))
    while arduino.readline() != b'd\r\n':
        pass
    sent = ""
    for l in range(39, 49):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "e", 'utf-8'))
    while arduino.readline() != b'e\r\n':
        pass
    sent = ""
    for l in range(49, 59):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "f", 'utf-8'))
    while arduino.readline() != b'f\r\n':
        pass
    sent = ""
    for l in range(59, 69):
        sent += "{0}${1}${2}$".format(int(led_value_r[l]), int(led_value_g[l]), int(led_value_b[l]))
    arduino.write(bytes(sent + "g", 'utf-8'))
    while arduino.readline() != b'g\r\n':
        pass
    while arduino.readline() != b'l\r\n':
        pass
    print("Current FPS: {0}".format(1 / (time.time() - timme)))
