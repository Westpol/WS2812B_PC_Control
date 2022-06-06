import pyscreenshot
from screeninfo import get_monitors
import time


pixel = []

width, height = get_monitors()[0].width, get_monitors()[0].height

while 1:
    timme = time.time()

    img = pyscreenshot.grab(bbox=(0, 0, width, height), backend="mss", childprocess=False)

    for i in range(100):
        for k in range(width):
            pixel.append(img.getpixel((k, i)))

    print(time.time() - timme)
    pixel.clear()
