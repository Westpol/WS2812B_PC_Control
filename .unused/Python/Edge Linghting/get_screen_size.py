from screeninfo import get_monitors

for m in get_monitors():
    print(m.width, m.height)
