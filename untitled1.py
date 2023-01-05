# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 22:38:50 2023

@author: khale
"""

# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(('CARDS\D.png')))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()