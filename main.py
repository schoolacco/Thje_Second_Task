from tkinter import *
from PIL import ImageTk, Image
from Module import Gamble
collection = {}
luck = 1
root = Tk()
root.title("TooRNG")
root.configure(bg="black")
root.config(width=1000,height=1000)
root.minsize(100,100)
root.maxsize(5000,5000)
root.geometry("500x500+20+120")
ico = Image.open('dice.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
Label(root, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
roll = Button(root, text="Roll", command=lambda: Gamble.Rng(collection, luck), bg="black", fg="white")
roll.place(relx=0.5, rely=0.5)
Button(root, text="View collection", command=lambda: Gamble.placeholder_function(collection), bg="black", fg="white").pack()
root.mainloop()