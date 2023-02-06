import tkinter as tk

class GAMEPAD_WIDGET:
    canvas = None
    IMAGE_CANVAS_WIDTH = 180
    IMAGE_CANVAS_HEIGHT = 80
    CIRCLE_SIZE = 10
    CIRCLES_WIDTH = 2

    buttons = {
        "A": {"position": (0.8, 0.7), "type": "circle"},
        "B": {"position": (0.85, 0.6), "type": "circle"},
        "X": {"position": (0.75, 0.6), "type": "circle"},
        "Y": {"position": (0.8, 0.5), "type": "circle"},
        "DPAD_UP": {"position": (0.2, 0.5), "type": "square"},
        "DPAD_DOWN": {"position": (0.2, 0.7), "type": "square"},
        "DPAD_LEFT": {"position": (0.15, 0.6), "type": "square"},
        "DPAD_RIGHT": {"position": (0.25, 0.6), "type": "square"},
        "START": {"position": (0.55, 0.5), "type": "circle"},
        "BACK": {"position": (0.45, 0.5), "type": "circle"},
        "LEFT_THUMB": {"position": (0.4, 0.7), "type": "circle"},
        "RIGHT_THUMB": {"position": (0.6, 0.7), "type": "circle"},
        "LEFT_SHOULDER": {"position": (0.3, 0.35), "type": "square"},
        "RIGHT_SHOULDER": {"position": (0.7, 0.35), "type": "square"},
        "LEFT_TRIGGER": {"position": (0.2, 0.2), "type": "square"},
        "RIGHT_TRIGGER": {"position": (0.8, 0.2), "type": "square"},
    }

    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=self.IMAGE_CANVAS_WIDTH, height=self.IMAGE_CANVAS_HEIGHT)
        self.canvas.pack(side="right")
        self.canvas.create_rectangle(10, 10, self.IMAGE_CANVAS_WIDTH, self.IMAGE_CANVAS_HEIGHT, fill="", outline="#fcba03", width=self.CIRCLES_WIDTH)

    def trigger_button(self, button, enable):
        if enable:
            print(button)

        if self.buttons[button]:
            x, y = self.buttons[button]["position"]
            type = self.buttons[button]["type"]
            x = x * self.IMAGE_CANVAS_WIDTH
            y = y * self.IMAGE_CANVAS_HEIGHT
            outline = "#fcba03" if enable else "gray"

            if type == "square":
                self.canvas.create_rectangle(x, y, x + self.CIRCLE_SIZE, y + self.CIRCLE_SIZE, fill="", outline=outline, width=self.CIRCLES_WIDTH)

            elif type == "circle":
                self.canvas.create_oval(x, y, x + self.CIRCLE_SIZE, y + self.CIRCLE_SIZE, fill="", outline=outline, width=self.CIRCLES_WIDTH)


    def turn_off_buttons(self):
        for button in self.buttons:
            self.trigger_button(button, False)
            