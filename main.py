from tkinter import * # For the GUIs as always
from tkinter import ttk # Specifically for the notebook tabs
from PIL import ImageTk, Image # Just so I can change the window icon
from Module import Gamble, Gear, SaveLoad, Biome # My module
from pydub import AudioSegment # Convert the music into useful data
import simpleaudio as sa # Play the music
import threading # Asynchio but simple, essentially runs programs within the program
import time # Force stops the program for a period of time, compatible with threads
# This program is a little complex
'''----------Initialisation----------'''
biome_song = {"Normal": "Clair_de_Lune.wav", "MAINFRAME//FALLEN": "Fallen_Symphony.wav"}
admin = False # This just sets the global variables
current_biome = "Normal"
def load_collection():
   '''This accesses your save file using the load function, and updates your collection to reflect it'''
   data = SaveLoad.Load()
   if data: # If the data exists
      collection.clear() # Empty dictionary
      collection.update(data) # Fill dictionary with json data
      Refresh() # Update collection tab
def Hide():
   global admin
   admin = False
   Nb.forget(admin_frame)
def ADMIN():
   '''This function simply checks the username and password from the ??? tab, and if correct adds the admin tab'''
   global admin
   Pass = password_entry.get() # Get password
   User = user_entry.get() # Get username
   if Pass == '*? DATA = NULL !"' and User == "ADMIN" and not admin: # not admin is to prevent duplication
      admin_frame.pack()
      Nb.add(admin_frame, text="ADMIN")
      admin = True
auto_roll_var = threading.Event() # Set this to an event
collection = {}
luck = 1
root = Tk() # Basic set up stuff
root.title("TooRNG")
root.configure(bg="black")
root.config(width=1000,height=1000)
root.minsize(100,100)
root.maxsize(5000,5000)
root.geometry("500x500+20+120")
ico = Image.open('dice.png') # Change iconphoto
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo) 
Nb = ttk.Notebook(root, cursor="circle") # Insert notebook and change cursor
s = ttk.Style()
s.configure('TFrame', background="black") #Change Style() to create bgs for frames
'''----------RNG----------'''
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame') #Create a tab in the notebook
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
roll = Button(rng_frame, text="Roll", command=lambda: Roll(collection, luck, root, current_biome), bg="black", fg="white") # Create a button which runs the rng command
roll.pack()
biome_stat = Label(rng_frame, text="Biome: Normal", bg="black", fg="white")
biome_stat.pack()
rng_frame.pack()
Nb.add(rng_frame, text="RNG")
'''----------Collection----------'''
collection_frame = ttk.Frame(Nb,width=2000, height=2000, style='TFrame')
List = Listbox(collection_frame, listvariable=collection, selectmode=SINGLE) # Initiates the listbox, kinda useless
List.pack()
def Refresh():
  '''Updates the listbox, doesn't destroy it this time, how nice, also really confusing list syntax that I stole online and somehow managed to understand and edit'''
  listvar = Variable(value=[f"{k}: {v}" for k,v in collection.items()]) #Create a list with the display of: item name: amount, use variable to turn it into something the Listbox is compatible with.
  List.configure(listvariable=listvar) # A bit nicer then destroying it right?
Button(collection_frame, text="Refresh List", bg="black", fg="white", command=lambda: Refresh()).pack()
collection_frame.pack()
Nb.add(collection_frame, text='Collection')
'''----------Crafting----------'''
gear_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Gear1 = Gear(name="Gear1", requirements={"Item1": 100, "Item3": 10}, luck_boost=2) # Create a gear
Button(gear_frame, text="Equip Gear1", bg="black", fg="white", command=lambda: Gear.equip(Gear1, luck, collection)).pack() # Unequiping will be inserted in future
gear_frame.pack()
Nb.add(gear_frame, text="Crafting")

'''----------Save/Load----------'''
save_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Button(save_frame, text="Save", bg="black", fg="white", command=lambda: SaveLoad.Save(collection)).pack() # Create a button to save your data 
Button(save_frame, text="Load", bg="black", fg="white", command=lambda: load_collection()).pack() # Create a button to load your data
save_frame.pack()
Nb.add(save_frame, text="Save/Load")
'''----------Admin----------'''
unknown_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
user_entry = Entry(unknown_frame)
user_entry.pack()
password_entry = Entry(unknown_frame, show="*") # Censorship
password_entry.pack()
Button(unknown_frame, text="???", bg="black", fg="white", command=lambda: ADMIN()).pack() # ???
unknown_frame.pack()
Nb.add(unknown_frame, text="???")
admin_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Label(admin_frame, text="Luck", bg="black", fg="white").pack()
Luck_entry = Entry(admin_frame)
Luck_entry.pack()
def Luck():
   '''Set luck to a value for debugging or cheating'''
   global luck
   try:
      luck = float(Luck_entry.get())
   except ValueError:
      pass
Button(admin_frame, text="Set Luck", bg="black", fg="white", command=lambda:Luck()).pack() # Set the luck
Label(admin_frame, text="Set Biome", bg="black", fg="white").pack()
Biome_entry = Entry(admin_frame)
Biome_entry.pack()
Button(admin_frame, text="Set Biome", bg="black", fg="white", command= lambda: set_biome(biome_stat, Biome_entry)).pack()
Button(admin_frame, text="Auto Roll", bg="black", fg="white", command=lambda: auto_roll_stat()).pack() # Change the status of the auto roll
Button(admin_frame, text="Hide The Evidence", bg="black", fg="white", command=lambda: Hide()).pack() # What ADMIN frame? You're imagining things
'''----------Music----------'''

def play_music():
    '''This constantly loops background music'''
    # Export to raw data
    while True:
      song = AudioSegment.from_wav(biome_song[current_biome]) # Background music
      playback = sa.play_buffer( #I'm not going to act like I understand what these are used for
          song.raw_data,
          num_channels=song.channels,
          bytes_per_sample=song.sample_width,
          sample_rate=song.frame_rate
      )
      playback.wait_done() # This waits until the song is finished before continuing

# Run in a thread
threading.Thread(target=play_music, daemon=True).start() # Asynchio but not complicated, begins running the play_music function seperately to not freeze the GUI

'''----------Rolling----------'''

def auto_roll(collection, luck):
    '''Simple code for a future feature, automatically runs the roll function in the background'''
    while auto_roll_var.is_set():
       Gamble.Rng(collection,luck, root)
       Biome.Rng(collection, luck, root, current_biome)
       time.sleep(0.1) # The time will become a variable in future
def auto_roll_stat():
  if auto_roll_var.is_set(): # If the auto roll is on
     auto_roll_var.clear() # Disable it
  else:
    auto_roll_var.set()
    threading.Thread(target= lambda: auto_roll(collection, luck), daemon=True).start() # Start autorolling with freezing the GUI
# auto_roll_var.set() to enable, auto_roll_var.clear() to disable
def biome_change(Label):
   '''Changes the biome, who would've guessed?'''
   global current_biome
   while True:
     time.sleep(600)
     current_biome = Biome.biome_change() # Run the function to change the biome, and set the current biome to it.
     Label.configure(text=f"Biome: {current_biome}") # Sets a label so the user can see
     sa.stop_all()
def Roll(collection, luck, GUI, current_biome):
   '''Just triggers both RNG functions to roll'''
   Gamble.Rng(collection, luck, GUI)
   Biome.Rng(collection, luck, GUI, current_biome)
def set_biome(Label, Entry):
   '''Debug method to set the biome'''
   global current_biome
   current_biome = Entry.get()
   Label.configure(text=f"Biome {current_biome}")
   sa.stop_all()
threading.Thread(target=lambda: biome_change(biome_stat), daemon=True).start() # Constantly runs the biome changing functions (maybe)

'''----------Running the program----------'''
Nb.pack(fill=BOTH, expand=TRUE) # The options make sure it fills the whole window
if __name__ == "__main__": # I have no idea what this does, but people do it
  root.mainloop()
