from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Module import Gamble
from pydub import AudioSegment
import simpleaudio as sa
import threading
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
Nb = ttk.Notebook(root, cursor="circle")
s = ttk.Style()
s.configure('TFrame', background="black") #Change Style() to create bgs for frames
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame') #Create a tab in the notebook
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
roll = Button(rng_frame, text="Roll", command=lambda: Gamble.Rng(collection, luck), bg="black", fg="white")
roll.pack()
Button(rng_frame, text="View collection", command=lambda: Gamble.placeholder_function(collection), bg="black", fg="white").pack()
rng_frame.pack()
Nb.add(rng_frame, text="RNG")
collection_frame = ttk.Frame(Nb,width=2000, height=2000, style='TFrame')
List = Listbox(collection_frame, listvariable=collection, selectmode=SINGLE)
List.pack()
def Refresh():
  global List, collection
  List.destroy()
  List = Listbox(master=collection_frame, listvariable=collection, selectmode=SINGLE) #Destroy the list to update it
  List.pack()
Button(collection_frame, text="Refresh List", bg="black", fg="white", command=lambda: Refresh()).pack()
collection_frame.pack()
Nb.add(collection_frame, text='Collection')
Nb.pack(fill=BOTH, expand=TRUE)

song = AudioSegment.from_wav("Fallen_Symphony.wav")

def play_music():
    # Export to raw data
    playback = sa.play_buffer(
        song.raw_data,
        num_channels=song.channels,
        bytes_per_sample=song.sample_width,
        sample_rate=song.frame_rate
    )
    playback.wait_done()  # optional — blocks the thread only, not GUI

# Run in a thread
threading.Thread(target=play_music, daemon=True).start()

root.mainloop()
