from tkinter import * # For the GUIs as always
from tkinter import ttk # Specifically for the notebook tabs
from Module import * # My module
from pydub import AudioSegment # Convert the music into useful data
import simpleaudio as sa # Play the music
import threading # Asynchio but simple, essentially runs programs within the program
import time # Force stops the program for a period of time, compatible with threads
import sys
# This program is a little complex
'''----------Initialisation----------'''
sys.set_int_max_str_digits(int(2147483647))
biome_song = {"Normal": "Clair_de_Lune.wav", "Paradiso": "Ascension_to_Heaven.wav", "HIS Domain": "In_the_House,_in_a_Heartbeat.wav", "MAINFRAME": "Your_Friend_Equals_false.wav", "MAINFRAME//FALLEN": "Fallen_Symphony.wav"}
admin = False # This just sets the global variables
current_biome = "Normal"
God_Roll_req = 20000
God_roll = 0
threshold = 0
speed = 1
def close(collection, God_roll, God_Roll_req, root):
   SaveLoad.Save(collection, God_roll, God_Roll_req)
   root.destroy()
def set_threshold(amount):
   global threshold
   try:
     amount = float(amount)
     amount = int(amount)
     threshold = amount
   except ValueError:
      threshold = 0
      pass
def equip(gear):
   global luck, fin_luck, speed, collection
   luck = fin_luck = speed = 1
   if not gear.check_requirements(collection):
      return
   try:
     luck *= gear.luck_boost
   except AttributeError:
      luck = 1
   try:
     speed /= gear.speed_boost
   except AttributeError:
      speed = 1
   try:
     fin_luck *= gear.fin_luck
   except AttributeError:
      fin_luck = 1
def load_collection():
   '''This accesses your save file using the load function, and updates your collection to reflect it'''
   global God_roll, God_Roll_req, GButton, collection
   data = SaveLoad.Load()
   if data: # If the data exists
      try:
        God_roll = data["God Roll"]
        del data["God Roll"]
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, fin_luck, root, current_biome, speed, threshold))
        if God_roll > 0:
           GButton.pack()
      except KeyError:
         pass
      try:
         God_Roll_req = data["God Roll Requirement"]
         del data["God Roll Requirement"]
         Req_Label.config(text=f"Rolls until next God Roll: {God_Roll_req}")
      except KeyError:
         pass
      collection.clear() # Empty dictionary
      try:
        for k, v in data.items():
          data[k] = int(v)
      except ValueError:
         print("Nice try with trying to edit the json, get better at doing that.")
         data = {}
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
fin_luck = 1
root = Tk() # Basic set up stuff
root.title("TooRNG")
root.configure(bg="black")
root.config(width=1000,height=1000)
root.minsize(100,100)
root.maxsize(5000,5000)
root.geometry("500x500+20+120")
photo = PhotoImage(file="dice.png")
root.wm_iconphoto(False, photo) 
Nb = ttk.Notebook(root, cursor="circle") # Insert notebook and change cursor
s = ttk.Style()
s.configure('TFrame', background="black") #Change Style() to create bgs for frames
'''----------RNG----------'''
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame') #Create a tab in the notebook
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
roll = Button(rng_frame, text="Roll", command=lambda: Roll(collection, luck, root, current_biome, fin_luck, speed, threshold), bg="black", fg="white") # Create a button which runs the rng command
roll.pack()
biome_stat = Label(rng_frame, text="Biome: Normal", bg="black", fg="white")
biome_stat.pack()
Req_Label = Label(rng_frame, text=f"Rolls till next God Roll: {God_Roll_req}", bg="black", fg="white")
Req_Label.pack()
rng_frame.pack()
Nb.add(rng_frame, text="RNG")
'''----------Collection----------'''
collection_frame = ttk.Frame(Nb,width=2000, height=2000, style='TFrame')
scrollbar = Scrollbar(collection_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
List = Listbox(collection_frame, listvariable=collection, selectmode=SINGLE) # Initiates the listbox, kinda useless
List.pack()
def Refresh():
  '''Updates the listbox, doesn't destroy it this time, how nice, also really confusing list syntax that I stole online and somehow managed to understand and edit'''
  listvar = Variable(value=[f"{k}: {v}" for k,v in collection.items()]) #Create a list with the display of: item name: amount, use variable to turn it into something the Listbox is compatible with.
  List.configure(listvariable=listvar) # A bit nicer then destroying it right?
  List.configure(yscrollcommand= scrollbar.set)
  scrollbar.configure(command= List.yview)
collection_frame.pack()
Nb.add(collection_frame, text='Collection')
'''----------Crafting----------'''
gear_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Gear1 = Gear(name="Gear1", requirements={"Item1": 100, "Item3": 10}, luck_boost=2) # Create a gear
Button(gear_frame, text="Equip Gear1", bg="black", fg="white", command=lambda: equip(Gear1)).pack() # Unequiping will be inserted in future
Deus = Late_Gear(name="Deus Ex Machina", requirements={"HIM": 666, "MAINFRAME": 1e5, "Apex Predator": 1e4, "The Figure": 777, "Wizard10989": 1}, luck_boost=1e6, speed_boost=1e3, fin_luck_boost=100)
Button(gear_frame, text="Equip Deus Ex Machina", bg="black", fg="white", command=lambda: equip(Deus)).pack()
gear_frame.pack()
Nb.add(gear_frame, text="Crafting")
'''----------Save/Load----------'''
save_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Button(save_frame, text="Save", bg="black", fg="white", command=lambda: SaveLoad.Save(collection, God_roll, God_Roll_req)).pack() # Create a button to save your data 
Label(save_frame, bg="black", fg="white", text=
      '''Potential Questions:
      Why can't I load my data manually?
      Because it'd let you cheat by using a God Roll and reloading the data to use it again until you get a satisfactory result.
      Does my data save if I close the window?
      Yes, it does so automatically.
      How is the data saved?
      Json.
      Can I edit my save file?
      If you have a basic understanding of json, sure, but if you mess up that's on you.''').pack()
save_frame.pack()
Nb.add(save_frame, text="Save")
'''----------Settings----------'''
settings_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Label(settings_frame, text="Cutscene Threshold:", bg="black", fg="white").pack()
cut_entry = Entry(settings_frame)
cut_entry.pack()
Button(settings_frame, text="Set Cutscene Threshold", bg="black", fg="white", command= lambda: set_threshold(cut_entry.get())).pack()
settings_frame.pack()
Nb.add(settings_frame, text="Settings")
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
Label(admin_frame,text="God Rolls", bg="black", fg="white").pack()
Roll_entry = Entry(admin_frame)
Roll_entry.pack()
Button(admin_frame, text="Debug", bg="black", fg="white", command=lambda: print(luck, fin_luck, speed, collection, God_roll, God_Roll_req)).pack()
def Luck():
   '''Set luck to a value for debugging or cheating'''
   global luck
   try:
      luck = float(Luck_entry.get())
   except ValueError:
      pass
def Fin_Luck():
   global fin_luck
   try:
      fin_luck = float(FinLuck_entry.get())
   except ValueError:
      pass
def Set_God_Roll():
   '''Set the amount of God rolls for debugging or cheating'''
   global God_roll, GButton, fin_luck
   try:
      God_roll = int(Roll_entry.get())
      try:
        if God_roll < 0 and GButton.winfo_exists() == False:
          GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, fin_luck, root, current_biome, speed))
          GButton.pack()
        else:
          GButton.configure(text=f"God Roll: {God_roll}")
      except:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, fin_luck, root, current_biome, speed))
        GButton.pack()
   except ValueError:
      pass
def Set_Speed():
   global speed
   try:
      speed = (1/float(speed_entry.get()))

   except ValueError:
      speed = 0
      pass
Button(admin_frame, text="Set Luck", bg="black", fg="white", command=lambda:Luck()).pack() # Set the luck
Label(admin_frame, text="Final Luck", bg="black", fg="white").pack()
FinLuck_entry = Entry(admin_frame)
FinLuck_entry.pack()
Button(admin_frame, text="Set Final Luck", bg="black", fg="white", command=lambda: Fin_Luck()).pack()
Label(admin_frame, text="Set Biome", bg="black", fg="white").pack()
Biome_entry = Entry(admin_frame)
Biome_entry.pack()
Label(admin_frame, text="Set Speed", bg="black", fg="white").pack()
speed_entry = Entry(admin_frame)
speed_entry.pack()
Button(admin_frame, text= "Set Speed", bg="black", fg="white", command= lambda: Set_Speed()).pack()
Button(admin_frame, text="Set Biome", bg="black", fg="white", command= lambda: set_biome(biome_stat, Biome_entry)).pack()
Button(admin_frame, text="Set God Rolls", bg="black", fg="white", command=lambda: Set_God_Roll()).pack()
Button(admin_frame, text="Auto Roll", bg="black", fg="white", command=lambda: auto_roll_stat()).pack() # Change the status of the auto roll
Button(admin_frame, text="Hide The Evidence", bg="black", fg="white", command=lambda: Hide()).pack() # What ADMIN frame? You're imagining things
'''----------Music----------'''

def play_music():
    '''This constantly loops background music'''
    # Export to raw data
    while True:
      try:
        song = AudioSegment.from_wav(biome_song.get(current_biome, "Clair_de_Lune.wav")) # Background music
      except KeyError:
         song = AudioSegment.from_wav("Clair_de_Lune.wav")
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

def auto_roll(collection, luck, fin_luck, speed, threshold):
    '''Simple code for a future feature, automatically runs the roll function in the background'''
    while auto_roll_var.is_set():
       Roll(collection, luck, root, current_biome, fin_luck, speed, threshold)
def auto_roll_stat():
  if auto_roll_var.is_set(): # If the auto roll is on
     auto_roll_var.clear() # Disable it
  else:
    auto_roll_var.set()
    threading.Thread(target= lambda: auto_roll(collection, luck, fin_luck, speed, threshold), daemon=True).start() # Start autorolling with freezing the GUI
# auto_roll_var.set() to enable, auto_roll_var.clear() to disable
def biome_change(Label):
   '''Changes the biome, who would've guessed?'''
   global current_biome
   while True:
     time.sleep(600)
     current_biome = Biome.biome_change() # Run the function to change the biome, and set the current biome to it.
     Label.configure(text=f"Biome: {current_biome}") # Sets a label so the user can see
     sa.stop_all()
def Roll(collection, luck, GUI, current_biome, fin_luck, speed, threshold):
   '''Just triggers both RNG functions to roll'''
   global God_Roll_req, God_roll, Req_Label, GButton
   luck *= fin_luck
   Biome.Rng(collection, luck, GUI, current_biome, threshold)
   root.after(int(speed*1000))
   Refresh()
   God_Roll_req -= 1
   Req_Label.configure(text=f"Rolls till next God Roll: {God_Roll_req}")
   if God_Roll_req <= 0:
      God_roll += 1
      God_Roll_req = 20000
      if God_roll == 1:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, fin_luck, GUI, current_biome, speed, threshold))
        GButton.pack()
      else:
        GButton.configure(text=f"God Roll: {God_roll}")
def god_roll(collection, fin_luck, GUI, current_biome, speed, threshold):
   global God_Roll_req, God_roll, luck, GButton, Req_Label, GButton
   God_roll -= 1
   luck *= fin_luck
   stat = God_Roll.Rng(collection, fin_luck, GUI, current_biome)
   if stat != "Success":
      stat = Biome.Rng(collection, luck=(luck*50000), GUI=GUI, current_biome=current_biome, threshold=threshold)
   root.after(int(speed*1000))
   Refresh()
   God_Roll_req -= 1
   Req_Label.configure(text=f"Rolls till next God Roll: {God_Roll_req}")
   if God_Roll_req <= 0:
      God_roll += 1
      God_Roll_req = 20000
      if God_roll == 1:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, fin_luck, GUI, current_biome, speed, threshold))
        GButton.pack()
   GButton.configure(text=f"God Roll: {God_roll}")
   if God_roll == 0 and GButton.winfo_exists():
      GButton.destroy()

def set_biome(Label, Entry):
   '''Debug method to set the biome'''
   global current_biome
   current_biome = Entry.get()
   Label.configure(text=f"Biome: {current_biome}")
   sa.stop_all()
threading.Thread(target=lambda: biome_change(biome_stat), daemon=True).start() # Constantly runs the biome changing functions

'''----------Running the program----------'''
Nb.pack(fill=BOTH, expand=TRUE) # The options make sure it fills the whole window
if __name__ == "__main__": # I have no idea what this does, but people do it
  load_collection() # Load the collection as the program starts, no cheating >:)
  root.protocol("WM_DELETE_WINDOW", lambda: close(collection, God_roll, God_Roll_req, root)) # Save once the window is closed,  no cheating >:(
  root.mainloop()