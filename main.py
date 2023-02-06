import tkinter as tk
from gamepad_events import listen_gamepads
from gamepad_widget import GAMEPAD_WIDGET

root = tk.Tk()
root.title("Gamepad Controller")
root.geometry("500x500")
gpad_widget = GAMEPAD_WIDGET(root)

gamepads = []

while True:
    root.update_idletasks()
    root.update()

    gamepads = listen_gamepads()

    gpad_widget.turn_off_buttons()
    for gamepad in gamepads:
        for button in gamepad:
            gpad_widget.trigger_button(button, True)
            
