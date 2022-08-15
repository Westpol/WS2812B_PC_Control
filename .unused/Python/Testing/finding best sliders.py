import PySimpleGUI as sg
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.001)

layout = [
    [sg.Frame('RGB Values', [[sg.Slider(range=(0, 255), orientation='v', key='-START-'), sg.Slider(range=(0, 255), orientation='v', key='-END-'), sg.Slider(range=(0, 255), orientation='v', key='-END-')]])],
]

window = sg.Window(title="RGB slider", layout=layout)

while True:
    event, values = window.read(timeout=1000)

    if event == sg.WIN_CLOSED:
        break
    print(values)
    arduino.write(bytes("{0}${1}${2}$".format(values['-START-'], values['-START-'], values['-START-']), 'utf-8'))


window.close()