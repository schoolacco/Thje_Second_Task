from tkinter import * # For the GUIs as always
from tkinter import ttk # Specifically for the notebook tabs
from Module import * # My module
from pydub import AudioSegment # Convert the music into useful data
import simpleaudio as sa # Play the music
import threading # Asynchio but simple, essentially runs programs within the program
import time # Force stops the program for a period of time, compatible with threads
import sys
import math
# This program is a little complex
'''----------Initialisation----------'''
sys.set_int_max_str_digits(int(2147483647)) # Mostly to prevent runtime errors from messing around
biome_song = {"Normal": "Clair_de_Lune.wav", "Shardscapes": "Slow_Down.wav", "Precipice of Eternity" : "Darkness_Falls.wav", "Paradiso": "Ascension_to_Heaven.wav", "HIS Domain": "Black_Knife.wav", "Duck Pond": "Duckstep.wav", "MAINFRAME": "Your_Friend_Equals_false.wav", "MAINFRAME//FALLEN": "Fallen_Symphony.wav", "R34L1TY": "Aleph-0.wav"}
admin = False # This just sets the global variables
current_biome = "Normal"
God_Roll_req = 20000
God_roll = 0
threshold = 0
speed = 1
cutscene = True
terminate = threading.Event()
auto_roll_var_plus = threading.Event()
terminate.set()
def get_info(event):
   '''Grab the information from the list and from it edit corresponding information'''
   global List, desc, rarity # Due to event bindings seemingly not allowing lambda, this seems almost required although it stands against optimisation
   try:
     content = List.get(List.curselection()).split(":") # Grab the currently selected listbox item and split it by the : to specifically get the name
     item = Item.find(content[0])
     desc.config(text=f"Description: {item.desc}")
     rarity.config(text=f"Rarity: {item.rdesc}")
   except TclError: #For when the tab is switched
      pass
def get_gear(event):
   global Gear_List, current_gear, req_label, desc_label, luck_label, speed_label, fin_label
   '''Get information from list and edit corresponding information'''
   try:
     content = Gear_List.get(Gear_List.curselection())
     current_gear = Gear.find(content.strip())
     thing = ', '.join([f"{k}: {v}" for k,v in current_gear.requirements.items()])
     req_label.configure(text=f"Requirements: {thing}")
     desc_label.configure(text=f"Description: {current_gear.desc}")
     luck_label.config(text=f"Luck Boost: {current_gear.luck_boost}")
     speed_label.config(text=f"Speed Boost: {current_gear.speed_boost}")
     try:
      fin_label.config(text=f"Final Luck Boost: {current_gear.fin_luck}")
     except AttributeError:
      fin_label.config(text="Final Luck Boost: None")
     return
   except TclError:
      pass
def biome_info(event):
   '''Get information from list and edit corresponding information'''
   global biome_desc, biome_rarity, biome_song_credit, biomes, Biome_List
   try:
     content = Biome_List.get(Biome_List.curselection())
     content = biomes.get(content, "Normal")
     biome_desc.config(text=f"Description: {content['Description']}")
     biome_rarity.config(text=f"Rarity: 1/{content['Rarity']}")
     biome_song_credit.config(text=f"Song: {content['Song']}")
   except TclError:
      pass
def close(collection, God_roll, God_Roll_req, root, cutscene, threshold, gear):
   '''Function for what happens when program closes'''
   SaveLoad.Save(collection, God_roll, God_Roll_req, cutscene, threshold, gear)
   root.destroy()
def disable():
   global threshold, cutscene
   if cutscene:
     threshold = 1e102
     cutscene = False
   else:
     threshold = 0
     cutscene = True
def set_threshold(amount):
   '''Function for setting the threshold'''
   global threshold, cut_entry
   try:
     amount = float(amount) # For e notation
     if amount != math.inf:
       amount = int(amount) # Converts to float for convenience
     else:
       cut_entry.insert(END, "Too Large")
       amount = 0
     threshold = amount
   except ValueError:
      threshold = 0 # For invalid inputs
      pass
def equip(gear, collection, label):
   '''Changes luck, final luck and speed'''
   global luck, fin_luck, speed # Required for editing of variables when using tkinter buttons
   luck = fin_luck = speed = 1
   try:
     try:
        luck, speed, fin_luck = gear.equip(luck, speed, collection, fin_luck)
     except ValueError:
        luck, speed = gear.equip(luck, speed, collection)
        fin_luck = 1
     label.configure(text=f"Current Gear Equipped: {current_gear.name}")
   except AttributeError:
      pass
def load_collection():
   '''This accesses your save file using the load function, and updates your collection to reflect it'''
   global God_roll, God_Roll_req, GButton, collection, wiz, cutscene, threshold, cut_entry, current_gear
   data = SaveLoad.Load()
   if data: # If the data exists
      try:
        God_roll = data["God Roll"]
        del data["God Roll"]
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, root, current_biome, speed, threshold))
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
      try:
         cutscene = data["Cutscene"]
         del data["Cutscene"]
      except KeyError:
         pass
      try:
         threshold = data["threshold"]
         del data["threshold"]
         cut_entry.insert(END, threshold)
      except KeyError:
         pass
      try:
        gear = data["Gear"]
        del data["Gear"]
      except KeyError:
        gear = None
      collection.clear() # Empty dictionary
      try:
        for k, v in data.items():
          data[k] = int(v)
      except ValueError:
         print("Nice try with trying to edit the json, get better at doing that.")
         data = {}
      collection.update(data) # Fill dictionary with json data
      if len(Item.get_instances()) <= len(collection) + 1:
         wiz.req = True
      Refresh() # Update collection tab
      if gear:
       current_gear = Gear.find(gear)
       equip(current_gear, collection, gear_label)
def Hide():
   '''Hides the admin frame'''
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
      Nb.add(admin_frame, text="DEBUG")
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
'''----------Item Intialisation----------'''
Item("Item1", 1, "Desc", "1/1") # I'm aware early game sucks, and I'm not fixing it SUFFER
Item("Duck", (("Duck Pond", 2),("R34L1TY", 2)), "Quack", "1/2 Duck Pond Exclusive")
Item("D.U.C.K.", (("Duck Pond", 1e8), ("MAINFRAME", 5e7), ("MAINFRAME", 5e6)), "Some kind of anti-cheat system that was meant to prevent failure... somehow was taught to only cause failure instead.", "I/100,000,000 Duck Pond Exclusive")
Item("Item3", 10, "Desc", "1/10")
Item("Item2", 100, "Desc", "1/100")
Item("Human", 1000, "Clearly the lesser race.", "1/1000")
Item("Black Shard", (("Shardscapes", 1000), ("MAINFRAME", 100), ("MAINFRAME//FALLEN", 50)), "Some kind of shard, it resonates with unknown energy", "1/1000 Shardscapes Exclusive")
Item("Essence", 5000, "Some kind of unknown substance with potentially magical properties.", "1/5000")
Item("Seraphim", (("Paradiso", 1e6), ("MAINFRAME", 5e5), ("MAINFRAME//FALLEN", 1e3)), 'The true form of an "angel", near godly power.', "1/1,000,000 Paradiso Exclusive")
Item("NullData", (("MAINFRAME", 100), ("MAINFRAME//FALLEN", 10)), "The rendition of empty data, or data with the value of 'None', it lacks any properties and tends to corrupt that which interacts with it, it is believed to contain some level of information relating to it's former data.", "1/100, MAINFRAME exclusive")
Item("MAINFRAME", (("MAINFRAME", 5e8), ("MAINFRAME//FALLEN", 1e6)), "A mere fraction of the power of the true structure. Enough to defeat most Gods.", "1/1,000,000,000", base_chance = 1e9)
Item("HIM", (("HIS Domain", 66666), ("MAINFRAME", 33333), ("MAINFRAME//FALLEN", 6666)), "The antipode of The Figure, a being of pure darkness, is known to constantly wear some crimson cloak concealing his true appearance in the shadows...", "1/66666, His Domain Exclusive, God Roll Exclusive", god_roll=True)
Item("The Figure", (("Paradiso", 77777), ("MAINFRAME", 33333), ("MAINFRAME//FALLEN", 7777)), "A Godly figure, it is unknown whether this is the God that the abrahamic faiths refer to, or simply a seperate being. Is seemingly more powerful then his antithesis.", "1/77777, Paradiso Exclusive, God Roll Exclusive", god_roll=True)
Item("Apex Predator", (("HIS Domain", 1e12), ("MAINFRAME", 1e11), ("MAINFRAME//FALLEN", 1e6)), "A seemingly innocent duck-like creature, do not touch it as it'll lead to a very brutal death...", "1/1,000,000,000,000 His Domain Exclusive")
Item("Wizard10989",(("MAINFRAME", 1010101010), ("MAINFRAME//FALLEN", 10989), ("R34L1TY", 10)), "Wizard10989 is fabled to be the creator of this world, although he denies such claims, he is thought to hold unknown amounts of power and supposedly has never put any effort into defeating his opponenets, with control over the very laws of logic itself many wonder how much can he really do...", "1/10101010 MAINFRAME Exclusive, God Roll Exclusive", god_roll=True)
Item("S U P R E M A C Y", 1000, "The absolute peak of mortal capability.", "1/1000, God Roll Exclusive", god_roll=True)
Item("The First Vessel//DATA = NULL", (("MAINFRAME", 14293879), ("MAINFRAME//FALLEN", 1429387)), "There is a fable out there of the first mortal, a being that managed to gain power that could even rival the Gods, the absolute peak of mortal capability, he was nicknamed by some as the Risen King, but his fall was not as smooth as his rise... he dared to challenge the MAINFRAME, a fatal mistake, he lost himself to the infinite reality-scaling learning secrets no mind should witness, as a consequence of such his mind and soul were flayed from his mortal flesh, leaving nothing but an empty husk... of inexistent data...", "1/14293879 MAINFRAME Exclusive", god_roll=False)
Item("The First Vessel//S U P R E M A C Y", (("MAINFRAME", 1000), ("MAINFRAME//FALLEN", 100)), "Given the MAINFRAME's infinite storage the empty gap that once embodied the First Vessel still remained as nothing but NullData, but as time passed, the empty husk of data began to regain properties of what it once embodied, regaining some degree of consciousness, eventually the wandering soul of the first mortal found this familiar body, and upon merging created this monstronsity, due to the body being made of NullData any attempts to kill or even erase will fail, as there is nothing left to erase. The only way to end the First Vessel is via using the power of the MAINFRAME itself.", "1/1000 God Roll Exclusive, MAINFRAME Exclusive", god_roll=True)
Item("YOU", (("MAINFRAME", 1e50), ("MAINFRAME//FALLEN", 1e12), ("R34L1TY", 100)), "THE INTRUDER, YOU NEVER BELONGED IN THIS WORLD", "1/1,000,000,000 MAINFRAME//FALLEN Exclusive")
Item("YOU//ICARUS", (("MAINFRAME", 1e50), ("MAINFRAME//FALLEN", 5555555555555), ("R34L1TY", 5555)), "I'm sure you know the story of Icarus... the question is now... WHERE IS THE SUN?", "1/55,555,555,555 MAINFRAME//FALLEN Exclusive")
Item("Kronos", (("Shardscapes", 39417), ("Precipice of Eternity", 19709), ("MAINFRAME", 39417), ("MAINFRAME//FALLEN", 19709)), "The manifestation of time itself, yet also something much darker. He wanders across the plains of existence, having no greater purpose left for him, he is a benvolent reaper, and wishes to see mortals use the most out of their lives rather than carelessly waste them, after all he knows he will win, no matter if you are an immortal or someone who already stands at his doorstep.", "1/39417 Shardscapes Exclusive, God Roll Exclusive", god_roll=True)
Item("Goose", (("Duck Pond", 110113),("R34L1TY", 1000)), "The REAL Apex Predator", "1/110113 Duck Pond Exclusive, God Roll Exclusive", god_roll=True)
wiz = Item("Wizard10989//???", (("MAINFRAME//FALLEN", 1e18), ("R34L1TY", 1e6)), "Innovation is nothing but the result of desperation.", "1/1,000,000,000,000,000,000 MAINFRAME//FALLEN Exclusive, God Roll Exclusive, only obtainable if user has every other item in the game.", requirement=False, god_roll=True)
'''----------RNG----------'''
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame') #Create a tab in the notebook
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
Label(rng_frame, text="What's a God Roll? A God Roll is a regular roll with a 50kx luck boost, it stacks with gears. There are also some items only obtainable with God Rolls which have their odds unaffected by luck but affected by final luck.", bg="black", fg="white", anchor=CENTER, wraplength=450).pack()
Label(rng_frame, text="What's a Biome? Biomes change the background music, and also give access to biome exclusive items or boost the odds of regular items. For more info check the biome info tab.", bg="black", fg="white", anchor=CENTER, wraplength=450).pack()
roll = Button(rng_frame, text="Roll", command=lambda: Roll(collection, luck, root, current_biome, fin_luck, speed, threshold), bg="black", fg="white") # Create a button which runs the rng command
roll.pack()
Button(rng_frame, text="Auto Roll", command=lambda:auto_roll_stat(),bg="black", fg="white").pack() # Some mercy
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
  global collection
  #collection = dict(zip(sorted(list(collection.keys()), key=lambda e: Item.find(e).get_chance(current_biome, Item.find(e).base)), list(collection.values()))) # Really complex looking line which in summary finds the chance of each item and sorts the items via those chances.
  listvar = Variable(value=[f"{k}: {v}" for k,v in collection.items()]) #Create a list with the display of: item name: amount, use variable to turn it into something the Listbox is compatible with.
  List.configure(listvariable=listvar) # A bit nicer then destroying it right?
  List.configure(yscrollcommand= scrollbar.set)
  scrollbar.configure(command= List.yview)
desc = Label(collection_frame, text="Description: ", bg="black", fg="white", wraplength=450)
rarity = Label(collection_frame, text="Rarity: ", bg="black", fg="white", wraplength=450)
List.bind("<<ListboxSelect>>", get_info)
desc.pack()
rarity.pack()
collection_frame.pack()
Nb.add(collection_frame, text='Collection')
'''----------Biome Info----------'''
biome_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
biomes = {"Normal": {"Rarity": 1, "Description": "A flat plain with no notable details.", "Song": "Claude Debussy: Clair de Lune"}, "Shardscapes": {"Rarity": 10, "Description": "The landscape is described as being consisted of large black shards (hence the name), it is unknown what these shards are actually made of. The Shardscapes have a pure white backdrop with the exception of some mountains.", "Song": "Creo: Slow Down"}, "Paradiso": {"Rarity": 100, "Description": "Some kind of paradise... and the home of The Figure, apparently warps itself to match whatever the observer believes a paradise is, the true appearance can supposedly only be seen by those beyond the concepts of belief.", "Song": "Xi: Ascension to Heaven"}, "HIS Domain": {"Rarity": 100, "Description": "The antipode to Paradiso, HIS home, it warps itself to whatever the viewer percieves Hell as, similarly to Paradiso the true appearance can only be seen by those that are above belief.", "Song": "Toby Fox: Black Knife"}, "Precipice of Eternity": {"Rarity": 150, "Description": "The only thing that will remain past the end of time, it is described as a pitch black cliff edge with some kind of cosmic fluid flowing beneath it... it is unknown whether there is anything more due to the pitch-black nature.", "Song": "Toby Fox: Darkness Falls"},  "Duck Pond": {"Rarity": 250, "Description": "A pond full of ducks", "Song": "Chime and Teminite: Duckstep"}, "MAINFRAME": {"Rarity": 500, "Description": "The Foundational Structure that makes up this very reality, it takes the appearance of blue computer hardware when under nobody's control, but will match it's master aesthetic when controlled.", "Song": 'Nevan Dove: "Your_Friend = false"'}, "MAINFRAME//FALLEN": {"Rarity": 5000, "Description": "WATCH AS REALITY CRUMBLES AROUND YOU.", "Song": "Ludicin: Fallen Symphony"}, "R34L1TY": {"Rarity": 1000000, "Description": "Home..?", "Song": "LeaF: Aleph-0"}}
var = Variable(value=[f"{k}" for k,v in biomes.items()])
Biome_List = Listbox(biome_frame, listvariable=var, selectmode=SINGLE)
Biome_List.pack()
biome_desc = Label(biome_frame, text="Description: ", bg="black", fg="white", wraplength=450)
biome_rarity = Label(biome_frame, text="Rarity: ", bg="black", fg="white", wraplength=450)
biome_song_credit = Label(biome_frame, text="Song: ", bg="black", fg="white", wraplength=450)
Biome_List.bind("<<ListboxSelect>>", biome_info)
biome_desc.pack()
biome_rarity.pack()
biome_song_credit.pack()
biome_frame.pack()
Nb.add(biome_frame, text="Biome Info")
'''----------Crafting----------'''
gear_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Gear(name="Gear1", requirements={"Item1": 100, "Item3": 10}, luck_boost=2, speed_boost=1.1, description="Test Gear") # Create a gear
Gear(name="Amulet", requirements={"Item2": 10, "Essence": 1}, luck_boost=4, speed_boost=3, description="A simple magical artifact, seems to make you more lucky and slightly faster.")
Gear(name="Code Fragment", requirements={"Item1": 10000, "Item3": 1000, "Item2": 100, "NullData": 1}, luck_boost=10, speed_boost=5, description="A fragment of useless code")
Late_Gear(name="Black Knife", requirements={"Black Shard": 1000, "S U P R E M A C Y": 1}, luck_boost=1, speed_boost=30, fin_luck_boost=2, description="A strange knife, it feels as if it harms you... yet increases your power in another way...")
Gear(name="Data Reconstructer",requirements={"NullData": 10000, "The First Vessel//DATA = NULL": 1}, luck_boost=50, speed_boost=15, description="A simple mechanism capable of restoring NullData to it's former state.")
Late_Gear(name="Timeline Manipulator", requirements={"Kronos": 1}, luck_boost=100, speed_boost=20,fin_luck_boost=2, description="A simple mechanism capable of altering the flow of time.")
Late_Gear(name="KARMA Manipulator", requirements={"Seraphim": 100, "Apex Predator": 10, "HIM": 1, "The Figure": 1}, luck_boost=1e4, speed_boost=50, fin_luck_boost=10, description="Manipulate the fundemental ideas of good and evil via the manipulation of both sides.")
Late_Gear(name="Axe of SUPREMACY", requirements={"Black Shard": 1000000, "S U P R E M A C Y": 1000, "The First Vessel//DATA = NULL": 10, "The First Vessel//S U P R E M A C Y": 1}, luck_boost=25000, speed_boost=125, fin_luck_boost=30, description="A weapon of choice, no longer any downsides.")
Late_Gear(name="Quackularity", requirements={"Duck": 100000, "Apex Predator": 100, "D.U.C.K.": 10, "Goose": 1}, luck_boost=5e4, speed_boost=200, fin_luck_boost=50, description="A singularity created by the condensed power of ducks.")
Late_Gear(name="Deus Ex Machina", requirements={"HIM": 666, "MAINFRAME": 1e5, "Apex Predator": 1e4, "The Figure": 777, "Wizard10989": 1}, luck_boost=1e6, speed_boost=1e3, fin_luck_boost=100, description="The miracle machine, only limited by the imagination of its user.")
Late_Gear(name="YOUR Soul", requirements={"YOU": 1000, "YOU//ICARUS": 55}, luck_boost=1e9, speed_boost=1e6, fin_luck_boost = 10000, description="Despite everything... is it YOU..?")
Late_Gear(name="The LIMIT..?", requirements={"YOU": 10000, "YOU//ICARUS": 1000, "Wizard10989": 100, "Wizard10989//???": 1}, luck_boost=1e12, speed_boost=1e9, fin_luck_boost=1e6, description="Here we are, was it worth it?")
b = Button(gear_frame, text="Unequip Gear", bg="black", fg="white", command= lambda: equip(None))
gears = Variable(value=[i.name for i in Gear.instances])
Gear_List = Listbox(gear_frame, listvariable=gears, selectmode=SINGLE)
Gear_List.bind("<<ListboxSelect>>", get_gear)
gear_label = Label(gear_frame, text="Current Gear Equipped: None", bg="black", fg="white")
req_label = Label(gear_frame, text="Requirements: ", bg="black", fg="white", wraplength=460)
desc_label = Label(gear_frame, text="Description: ", bg="black", fg="white", wraplength=450)
luck_label = Label(gear_frame, text="Luck Boost: ", bg="black", fg="white", wraplength=450)
speed_label = Label(gear_frame, text="Speed Boost: ", bg="black", fg="white", wraplength=450)
fin_label = Label(gear_frame, text="Final Luck Boost: ", bg="black", fg="white", wraplength=450)
Gear_List.pack()
gear_label.pack()
req_label.pack()
desc_label.pack()
luck_label.pack()
speed_label.pack()
fin_label.pack()
b.pack()
Button(gear_frame, text="Equip selected Gear", bg="black", fg="white", command = lambda: equip(current_gear,collection, gear_label)).pack()
gear_frame.pack()
Nb.add(gear_frame, text="Crafting")
'''----------Save----------'''
save_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame')
Button(save_frame, text="Save", bg="black", fg="white", command=lambda: SaveLoad.Save(collection, God_roll, God_Roll_req, cutscene, threshold, current_gear)).pack() # Create a button to save your data 
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
Button(settings_frame, text="Disable Cutscenes", bg="black", fg="white", command= lambda: disable()).pack()
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
   '''Set final luck for debugging or cheating'''
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
          GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, root, current_biome, speed, threshold))
          GButton.pack()
        else:
          GButton.configure(text=f"God Roll: {God_roll}")
      except:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, root, current_biome, speed, threshold))
        GButton.pack()
   except ValueError:
      pass
def Set_Speed():
   '''Set speed for debugging or cheating'''
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
Button(admin_frame, text="Auto Roll Plus", bg="black", fg="white", command=lambda: auto_roll_stat_plus()).pack() # Change the status of the auto roll
Button(admin_frame, text="Hide The Evidence", bg="black", fg="white", command=lambda: Hide()).pack() # What ADMIN frame? You're imagining things
'''----------Music----------'''

def play_music():
    '''This constantly loops background music'''
    # Export to raw data
    while terminate.is_set():
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
    while auto_roll_var.is_set() and terminate.is_set():
       Roll(collection, luck, root, current_biome, fin_luck, speed, threshold)
       time.sleep(speed)
def auto_roll_plus(collection, fin_luck, speed):
   '''Auto roll but better'''
   while auto_roll_var_plus.is_set() and terminate.is_set():
      God_Roll.Rng(collection, fin_luck, root, current_biome, cutscene)
      Refresh()
      time.sleep(speed)
def auto_roll_stat_plus():
   if auto_roll_var_plus.is_set():
      auto_roll_var_plus.clear()
   else:
      auto_roll_var_plus.set()
      threading.Thread(target= lambda: auto_roll_plus(collection, fin_luck, speed), daemon=True).start()
def auto_roll_stat():
  '''Simple function that flips the auto roll status'''
  if auto_roll_var.is_set(): # If the auto roll is on
     auto_roll_var.clear() # Disable it
  else:
    auto_roll_var.set()
    threading.Thread(target= lambda: auto_roll(collection, luck, fin_luck, speed, threshold), daemon=True).start() # Start autorolling with freezing the GUI
    threading.Thread(target= lambda: auto_roll_plus(collection, fin_luck, speed), daemon=True).start()
# auto_roll_var.set() to enable, auto_roll_var.clear() to disable
def biome_change(Label):
   '''Changes the biome, who would've guessed?'''
   global current_biome
   while terminate.is_set():
     time.sleep(600)
     current_biome = Gamble.biome_change() # Run the function to change the biome, and set the current biome to it.
     Label.configure(text=f"Biome: {current_biome}") # Sets a label so the user can see
     sa.stop_all()
def Roll(collection, luck, GUI, current_biome, fin_luck, speed, threshold):
   '''Just triggers both RNG functions to roll'''
   global God_Roll_req, God_roll, Req_Label, GButton, wiz
   if len(Item.get_instances()) == len(collection) + 1:
      wiz.req = True
   luck *= fin_luck
   Gamble.Rng(collection, luck, GUI, threshold, current_biome)
   Refresh()
   God_Roll_req -= 1
   Req_Label.configure(text=f"Rolls till next God Roll: {God_Roll_req}")
   if God_Roll_req <= 0:
      God_roll += 1
      God_Roll_req = 20000
      if God_roll == 1:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, GUI, current_biome, speed, threshold))
        GButton.pack()
      else:
        GButton.configure(text=f"God Roll: {God_roll}")
def god_roll(collection, luck, fin_luck, GUI, current_biome, speed, threshold):
   '''God rolls, with either god roll exclusives or 50kx luck'''
   global God_Roll_req, God_roll, GButton, Req_Label, GButton, cutscene
   God_roll -= 1
   luck *= fin_luck
   stat = God_Roll.Rng(collection, fin_luck, GUI, current_biome, cutscene)
   if stat == "Special":
      SaveLoad.Save(collection, God_roll, God_Roll_req, threshold, cutscene)
      for item in GUI.winfo_children(): # Destroys all GUI content
         item.destroy()
      root = GUI
      root.config(bg="black")
      root.title("Terminal")
      root.overrideredirect(True) # Removes window screen
      root.state("zoomed")
      root.focus_force()
      text = Text(root, bg="black", fg="lime", insertbackground="white", font=("Courier", 12))
      text.pack(fill=BOTH, expand=TRUE)
      terminate.clear() # Kills all threads
      terminate_2 = threading.Event()
      terminate_2.set()
      time.sleep(10)
      lines = [
         "Attempting to Access MAINFRAME",
         "Loading...",
         "Access Denied",
         "Loading...",
         "Incorrect Username",
         "Loading...",
         "Incorrect Password",
         "Recover Password?",
         "Y/N",
         "Correct Username, Correct Password",
         "Access granted",
         "Welcome! V2l6YXJkMTA5ODk=",
         "What would you like to do?",
         "ERROR TrustedInstaller level access required.",
         "Access granted",
         "Opening PLAYER.exe",
         "Accessing Connection.exe",
         "Are you sure you would like to terminate the connection?",
         "Are you certain?",
         "Y/N",
         "Input accepted, termination beginning",
         "Loading...",
         "...",
         "...",
         "...",
         "Loading complete!",
         "Terminating connection to PLAYER",
         "Would you like to give a reason for termination?",
         "Y/N",
         "Please enter message below.",
         "Processing message...",
         "Sending message to PLAYER...",
         "Please wait",
         "Loading...",
         "Thank you for your patience, message shall load soon...",
         "CONNECTION TERMINATED",
      ]
      for line in lines: # Type animator effect
         l = list(line)
         l.append("\n")
         for char in l:
           text.configure(state=NORMAL) # Allows edits
           text.insert(END, f"{char}")
           text.see(END) # Forces to end of text
           text.configure(state=DISABLED) # Disables edits
           root.update() # Update GUI
           time.sleep(0.05)
         time.sleep(random.uniform(0.3,0.8)) # Random time between 0.3-0.8 seconds
      time.sleep(1)
      text.destroy() # Part 2
      finale = [
         "So here we are huh...",
         "The end...",
         "All of this time... for what..?",
         "Surely, surely you had something better to do...",
         "Something better to do then play a joke game made by some random.",
         "But here you are...",
         "At the end...",
         "Just, stop procastinating with whatever you should be doing, and do it.",
         "If you have work, finish it, some passion project, work on it.",
         "Anything is a better use of time than this.",
         "So, I'll leave you with one last question...",
         "Was it worth it?"
      ]
      thej_label = Label(root, bg="black", fg="green", font=("Courier", 24), wraplength=root.winfo_screenwidth()-100, justify=CENTER)
      thej_label.place(relx=0.5, rely=0.5, anchor=CENTER)
      for line in finale:
         for i in range(1, len(line) + 1): # Cycles through string
               thej_label.config(text=line[:i]) #Includes prior parts
               root.update()
               time.sleep(random.uniform(0.1,0.5))
         time.sleep(2)
         for i in range(len(line), -1, -1): # Cycles backwards
            thej_label.config(text=line[:i])
            root.update()
            time.sleep(random.uniform(0.1,0.3))
         time.sleep(1)
      root.destroy()
      return
   if stat != "Success" or "Special":
      stat = Gamble.Rng(collection, luck=(luck*50000), GUI=GUI, current_biome=current_biome, threshold=threshold)
   Refresh()
   God_Roll_req -= 1
   Req_Label.configure(text=f"Rolls till next God Roll: {God_Roll_req}")
   if God_Roll_req <= 0:
      God_roll += 1
      God_Roll_req = 20000
      if God_roll == 1:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, GUI, current_biome, speed, threshold))
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
if __name__ == "__main__": # Ensures program isn't imported, apparently increases security somehow
  load_collection() # Load the collection as the program starts, no cheating >:)
  root.protocol("WM_DELETE_WINDOW", lambda: close(collection, God_roll, God_Roll_req, root, cutscene=cutscene, threshold=threshold, gear=current_gear)) # Save once the window is closed,  no cheating >:(
  root.mainloop()