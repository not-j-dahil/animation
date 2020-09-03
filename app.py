import tkinter as tk
import random
import time
from PIL import Image, ImageTk

CLOCK_SPEED = 33 #60Hz - Refresh rate

class Graphics(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, highlightthickness=0)

        self.load_assets()
        self.create_objects()

        self.after(CLOCK_SPEED, self.perform_actions) # initiate window
    
    def load_assets(self):
        try:
            self.ball_image = Image.open("./assets/ball.png")
            self.ball_image = self.ball.resize((50, 50), Image.ANTIALIAS)
            self.ball = ImageTk.PhotoImage(self.ball_image)
        except IOError as error:
            print(error)
            root.destroy()

    def perform_actions(self):
        '''Recursive function - Refresh window'''
        self.after(CLOCK_SPEED, self.perform_actions) # Refresh window
    
#create window
root = tk.Tk()
root.title("Graphics and Animations")
root.resizable(False, False)

canvas = Graphics()
canvas.pack()

#start window
root.mainloop()
