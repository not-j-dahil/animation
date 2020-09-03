import tkinter as tk
import random
import time
from PIL import Image, ImageTk

CLOCK_SPEED = 33 #60Hz - Refresh rate
BOUNCE_STRENGTH = 20

class Graphics(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, highlightthickness=0)

        self.ball_position = (300, 500)
        global BOUNCE_STRENGTH
        self.y_vel = 0

        self.load_assets()
        self.create_objects()

        self.after(CLOCK_SPEED, self.perform_actions) # initiate window
    
    def load_assets(self):
        try:
            self.ball_image = Image.open("./assets/ball.png")
            self.ball_image = self.ball_image.resize((50, 50), Image.ANTIALIAS)
            self.ball = ImageTk.PhotoImage(self.ball_image)
        except IOError as error:
            print(error)
            root.destroy()
    
    def create_objects(self):
        self.create_image(*self.ball_position, image=self.ball, tag="ball")
        self.create_rectangle(7,7,593,613, outline="#999999") # border

    def perform_actions(self):
        '''Recursive function - Refresh window'''
        self.move_ball()
        self.after(CLOCK_SPEED, self.perform_actions) # Refresh window
    
    def move_ball(self):
        x_pos, y_pos = self.ball_position
        if(y_pos >= 500):
            #checks if next pos is below or on y:500
            self.bounce_ball()
        
        self.ball_position = (x_pos, y_pos - self.y_vel)
        self.y_vel -= 1

        self.coords(self.find_withtag("ball"), self.ball_position)


    def bounce_ball(self):
        global BOUNCE_STRENGTH
        self.y_vel = BOUNCE_STRENGTH

#create window
root = tk.Tk()
root.title("Graphics and Animations")
root.resizable(False, False)

canvas = Graphics()
canvas.pack()

#start window
root.mainloop()
