import tkinter as tk
from PIL import ImageGrab

class SignaturePad:
    def __init__(self, window):
        self.window = window
        self.drawing = False
        self.last_point = (0, 0)
        self.canvas = tk.Canvas(window, width=500, height=200, bg='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.stop_draw)

    def save_and_close(self):
        self.save_signature("signature.png")
        self.window.destroy()
        self.window.bind('<Return>', self.save_and_close)

    def start_draw(self, event):
        self.drawing = True
        self.last_point = (event.x, event.y)

    def draw(self, event):
        if self.drawing:
            new_point = (event.x, event.y)
            self.canvas.create_line(self.last_point, new_point)
            self.last_point = new_point

    def stop_draw(self, event):
        self.drawing = False

    def save_signature(self, filename):
        x = self.window.winfo_rootx() + self.canvas.winfo_x()
        y = self.window.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

    def save_and_close(self, event=None):
        self.save_signature('signature.png')
        self.window.destroy()
