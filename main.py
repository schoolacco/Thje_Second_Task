import random
import asyncio
import time
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
ico = Image.open('dice.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.mainloop()