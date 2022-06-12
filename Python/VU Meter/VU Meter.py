import numpy as np
import sounddevice as sd
import time
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)

duration = 3600   # in seconds
num_leds_right = 21
num_leds_top = 36
num_leds_left = 21
num_leds = 57
timme = 0
maxVal = 0
half_sec = 0


def send_vals(noise):
    global timme, maxVal, half_sec
    if time.time() >= half_sec:
        maxVal -= 1
        half_sec = time.time() + .1
    if int(noise * 10) > maxVal:
        maxVal = int(noise * 10)
    arduino.write(bytes(str(maxVal) + "$", 'utf_8'))
    print("Current FPS: " + str(1/(time.time() - timme)))
    timme = time.time()


def audio_callback(indata, frames, time, status):
   #volume_norm = np.linalg.norm(indata) * 10
   #print("|" * int(volume_norm))
   send_vals(np.linalg.norm(indata))


stream = sd.InputStream(callback=audio_callback)
with stream:
   sd.sleep(duration * 1000)
