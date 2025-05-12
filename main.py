import random
import asyncio
from tkinter import *
from PIL import Image, ImageTk
# I'll merge this eventually
root = Tk()
ico = Image.open('dice.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.mainloop()