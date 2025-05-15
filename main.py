from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Module import Gamble
from pydub import AudioSegment
from pydub.playback import play
import pyperclip
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
try:
  song = AudioSegment.from_mp3("Fallen_Symphony.mp3")
  play(song)
except Exception as e:
  pyperclip.copy(e)
Nb = ttk.Notebook(root, cursor="circle")
s = ttk.Style()
s.configure('Apod_frame.TFrame', background="black") #Change Style() to create bgs for frames
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='Apod_frame.TFrame') #Create a tab in the notebook
#rng = Frame(Nb,height=2000, width=2000,, name="rng")
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
roll = Button(rng_frame, text="Roll", command=lambda: Gamble.Rng(collection, luck), bg="black", fg="white")
roll.pack()
Button(rng_frame, text="View collection", command=lambda: Gamble.placeholder_function(collection), bg="black", fg="white").pack()
rng_frame.pack()
Nb.pack()
root.mainloop()