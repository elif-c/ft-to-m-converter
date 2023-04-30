import PySimpleGUI

import converter
from converter import convert

PySimpleGUI.theme("Black")

feet_text = PySimpleGUI.Text("Enter feet:")
feet_input = PySimpleGUI.InputText(0, key="feet_input")

inches_text = PySimpleGUI.Text("Enter inches:")
inches_input = PySimpleGUI.InputText(0, key="inches_input")

convert_button = PySimpleGUI.Button("Convert", key="convert",
                                    button_color="orange")
exit_button = PySimpleGUI.Button("Exit")
result = PySimpleGUI.Text(key="result")

window = PySimpleGUI.Window("Converter",
                            font=("Roboto", 12),
                            layout=[[feet_text, PySimpleGUI.Push(), feet_input],
                                    [inches_text, inches_input],
                                    [convert_button, result, PySimpleGUI.Push(), exit_button]])
while True:
    event_key, value = window.read()
    match event_key:
        case "convert":
            feet = int(value["feet_input"])
            inches = int(value["inches_input"])
            if feet == 0 and inches == 0:
                PySimpleGUI.popup("Please enter values", font=("Roboto", 12))
                continue
            result = converter.convert(feet, inches)
            result = round(result, 2)
            window["result"].update(result)
        case "Exit":
            break
        case PySimpleGUI.WINDOW_CLOSED:
            break
window.close()
