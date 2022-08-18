from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
state = False


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


def on_clicked(icon, item):
    global state
    state = not item.checked
    print(state)

# Update the state in `on_clicked` and return the new state in
# a `checked` callable
icon('test', create_image(64, 64, 'black', 'white'), menu=menu(
    item(
        'Checkable',
        on_clicked,
        checked=lambda item: state))).run()
