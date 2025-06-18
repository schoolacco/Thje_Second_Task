# 11SE Task 2 2025 - Text-Based Adventure
### By Anthony Revel

# Sprint 1
## Requirements Definition
### Functional Requirements
* The user needs to be able to view their collection of items and must be capable of viewing the statistics of them as well
* The user must be capable of retrieving data about their 'item' collection and be capable of using these in the game to battle enemies.
* The user must be capable of saving their data (via json)
* The user must be capable of "crafting" items upon meeting requirements
### Non-Functional Requirements
* The system must be capable of executing most functions in under a second.
* The system must not fail while running and data should not be lost.
* The system should be easily navigable with minimal instructions required to understand the major functions of the system.

## Determining Specifications
### Functional Specifications
* The user must be capable of interacting with the system via a GUI interface
* The user must be capable of playing the game with no runtime errors
* The program must be capable of handling invalid inputs as well as users attempting to break the program (attempting to edit save data)
* The program must be capable of:
  * Rolling with rng
  * Increasing luck or other aspects with items
  * Saving data
  * View their collection
  * Battling using items from their collection
* The program should have an 'admin' panel as to make it reasonable to mark the program
### Non-Functional Specifications
* The program must be capable of running most functions in under a second (with an exception to those that intentionally force waiting)
* The program should be efficient minimising redundant code with loops and functions
* The UI should be easy to understand and not complex to allow for ease of use, hard to see colours should not be used and text should be reasonably sized
* Everything within the program should work as intended, menu navigation should function as intended and data should not become corrupted (unless the user attempts to edit the save data themselves, then it is their fault)
### Use Case

*Viewing Collection*
![Use Case 1](Use_1.png)
*Actually playing the main game*
![Use Case 2](Use_2.png)
*Saving after playing for a bit*
![Use Case 3](Use_3.png)
*Crafting an item and selecting it after meeting requirements*
![Use Case 4](Use_4.png)
## Design
*Storyboard*
![Storyboard](Storyboard.png)
*Level 0 DFD*
![Data Flow Diagram](DFD0.png)
*Level 1 DFD*
![More Complex Data Flow Diagram](DFD1.png)
*Gantt Chart*
![Gantt Chart](Agile_Gantt.jpeg)
## Build and Test
```Python

```

## Review

1. The system is entirely successful in meeting all specified functional and non-functional requirements and also meets many further unnessecary requirements (that realistically should've been implemented in future sprints), it is capable of saving and loading data via json, accessing the collection and allowing the user to view it, it is capable of "crafting" upon meeting requirements, there is currently little to no delay in the functionality of anything and the system encounter no runtime errors with it being relatively easy to naviagate.
2. The system handles inputs and outputs almost exactly as planned, although one use case has yet to have been made (planned for next sprint) all other use cases have been recreated in a similar fashion to what was originally planned for the system.
3. The functions, variables and docstrings/comments ensure that the code is easily readable and understandable with everything being rather clear if you have a fundemental level of understanding of the modules already being used. The system as a whole is very organised with designated sections seperated by strings to increase clarity.
4. The next sprint is intended to include the main feature of the game among various other smaller features for the game to have, including an auto-roll for normal players, for gears and a way to increase rolling speed, a roll cooldown, biomes and many other minor features to increase the complexity of the game.

# Sprint 2

## Design

![Minorly complex Structure Chart](Structure.png)
*From my new understanding of tkinter, all the frames exist simultaneously, the Notebook only shows you one at a time*

### Pseudo Code
```Pseudo
BEGIN main
  Initialise GUI
  Initialise Items
  Initialise GUI content
  play music
  auto roll
  biome change
  IF program is not imported THEN
    load collection
    set protocol for when GUI is closed to close
    WHILE GUI is not closed THEN
      IF roll button is pressed THEN
        Roll
      ENDIF
      IF God roll button is pressed THEN
        God_Roll
      ENDIF
      IF item in list is selected THEN
        get_info
      ENDIF
      IF item in biome list is selected THEN
        get_biome_info
      ENDIF
      IF item in gear list is selected THEN
        get_gear_info
      ENDIF
      IF equip button is pressed THEN
        equip_gear
      ENDIF
      IF unequip button is pressed THEN
        luck = final luck = speed = 0
      ENDIF
      IF save button is pressed THEN
        save
      ENDIF
      INPUT cutscene threshold
      IF set threshold button is pressed THEN
        threshold = cutscene threshold
      ENDIF
      INPUT Username
      INPUT Password
      IF Username == ADMIN and Password == *? DATA = NULL !" THEN
        Add DEBUG
      ENDIF
      INPUT luck entry
      INPUT god roll entry
      INPUT final luck entry
      INPUT biome entry
      INPUT speed entry
      IF set luck button is pressed THEN
        luck = luck entry
      ENDIF
      IF set god roll button is pressed THEN
        set god roll
      ENDIF
      IF set speed button is pressed THEN
        set speed
      ENDIF
      IF set biome button is pressed THEN
        current biome = biome entry
      ENDIF
      IF debug button is pressed THEN
        DISPLAY luck, final luck, speed, collection, god roll, god roll requirement
      ENDIF
      IF auto roll button is pressed THEN
        set auto roll status
      ENDIF
      IF hide button is pressed THEN
        hide
      ENDIF
    ENDWHILE
  ENDIF
END main
```

```Pseudo
BEGIN roll(collection, luck, GUI, current biome, final luck, speed, cutscene threshold)
  IF Length of Item instances == Length of collection + 1 THEN
    wiz requirement = True
  ENDIF
  luck = luck * final luck
  RNG(collection, luck, GUI, threshold, current_biome)
  Refresh
  God Roll Requirement = God Roll Requirement - 1
  Configure requirement label
  IF God Roll Requirement <= 0 THEN
    God Roll = God Roll + 1
    God Roll Requirement = 20000
    IF God Roll == 1 THEN
      Add God Roll Button to rng frame
    ELSE
      Edit God Roll Button to show current god roll amount
    ENDIF
  ENDIF
END Roll
```

```Pseudo
BEGIN set_biome(Label, Entry)
  current biome = Entry content
  Configure Label to show current biome
  Stop all music
END set_biome
```

### Flowcharts
*Main Flowchart*
[Main Flowchart](https://excalidraw.com/#json=NHkAqK_dTX2cExLYZJcaG,LzeEUau5EsoEpNclCcFvzQ)

*Close Function*
![Close Flowchart](Flow2.png)

*RNG Function*
![RNG Flowchart](Flow3.png)
## Build and Test

**No release for this sprint**

## Review

The project currently meets almost all functional and non-functional requirements, with a singular exception to the battle system, which I have decided not to implement, however all other functions outlined have been made and there currently seems to be no way to truly break the program and it behaves exactly as anticipated. The code is rather readable as it is littered with comments and docstrings throughout, with several design choices being explained with the code, I could now attempt to properly implement the code to create a properly functioning program rather than just test cases.

# Sprint 3

## Design
1[UML Class Diagram](UML.png)

## Build and Test
No release

## Review

The project currently meets almost all functional and non-functional requirements, with a singular exception to the battle system, as to why refer to the previous review., however all other functions outlined have been made and there currently seems to be no way to truly break the program and it behaves exactly as anticipated. The code is rather readable as it is littered with comments and docstrings throughout, with several design choices being explained with the code, I could now improve it by implementing QoL features such as a list of biomes + information and possibly revamping the Item system for efficiency, along with this I can also add the many QoL features I have already added but put behind a administrator wall.

# Sprint 4

## Design

* Remove all the placeholder items and replace them with proper items
* Rebalance game for some level of fairness (it's still meant to be painful though)
* Add more content in terms of items and gears
* Add auto roll
* Transform administrator auto roll to auto god roll
* Add more cutscenes for pre-existing content
* Make **the final cutscene**.
* Turn it into an executable maybe.

All of these will be easy to make, other than maybe the final cutscene, due to the pre-existing systems I have made adding and changing items/gears will be incredibly easy, and adding more cutscenes is just as easy, the auto roll has already been made, the only real things that require change are the administrator god rolls (which will be a minor edit to the pre-existing auto roll code), and the final cutscene, which will be simple to integrate, but difficult to actually make.

## Build and Test
main
```Python
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
sys.set_int_max_str_digits(int(2147483647)) # Mostly to prevent runtime errors from messing around
biome_song = {"Normal": "Clair_de_Lune.wav", "Shardscapes": "Slow_Down.wav", "Precipice of Eternity" : "Darkness_Falls.wav", "Paradiso": "Ascension_to_Heaven.wav", "HIS Domain": "Black_Knife.wav", "MAINFRAME": "Your_Friend_Equals_false.wav", "MAINFRAME//FALLEN": "Fallen_Symphony.wav", "R34L1TY": "Aleph-0.wav"}
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
   global Gear_List, current_gear, req_label, desc_label
   '''Get information from list and edit corresponding information'''
   try:
     content = Gear_List.get(Gear_List.curselection())
     current_gear = Gear.find(content.strip())
     thing = ', '.join([f"{k}: {v}" for k,v in current_gear.requirements.items()])
     req_label.configure(text=f"Requirements: {thing}")
     desc_label.configure(text=f"Description: {current_gear.desc}")
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
def close(collection, God_roll, God_Roll_req, root, cutscene, threshold):
   '''Function for what happens when program closes'''
   SaveLoad.Save(collection, God_roll, God_Roll_req, cutscene, threshold)
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
   global threshold
   try:
     amount = float(amount) # For e notation
     amount = int(amount) # Converts to float for convenience
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
   global God_roll, God_Roll_req, GButton, collection, wiz, cutscene, threshold, cut_entry
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
Item("Item3", 10, "Desc", "1/10")
Item("Item2", 100, "Desc", "1/100")
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
wiz = Item("Wizard10989//???", (("MAINFRAME//FALLEN", 1e18), ("R34L1TY", 1e6)), "Innovation is nothing but the result of desperation.", "1/1,000,000,000,000,000,000 MAINFRAME//FALLEN Exclusive, God Roll Exclusive, only obtainable if user has every other item in the game.", requirement=False, god_roll=True)
'''----------RNG----------'''
rng_frame = ttk.Frame(Nb, width=2000, height=2000, style='TFrame') #Create a tab in the notebook
Label(rng_frame, text="There is nothing much to say, click the button to begin.", bg="black", fg="white", anchor="center").pack()
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
biomes = {"Normal": {"Rarity": 1, "Description": "A flat plain with no notable details.", "Song": "Claude Debussy: Clair de Lune"}, "Shardscapes": {"Rarity": 10, "Description": "The landscape is described as being consisted of large black shards (hence the name), it is unknown what these shards are actually made of. The Shardscapes have a pure white backdrop with the exception of some mountains.", "Song": "Creo: Slow Down"}, "Precipice of Eternity": {"Rarity": 100, "Description": "The only thing that will remain past the end of time, it is described as a pitch black cliff edge with some kind of cosmic fluid flowing beneath it... it is unknown whether there is anything more due to the pitch-black nature.", "Song": "Toby Fox: Darkness Falls"}, "Paradiso": {"Rarity": 200, "Description": "Some kind of paradise... and the home of The Figure, apparently warps itself to match whatever the observer believes a paradise is, the true appearance can supposedly only be seen by those beyond the concepts of belief.", "Song": "Xi: Ascension to Heaven"}, "HIS Domain": {"Rarity": 200, "Description": "The antipode to Paradiso, HIS home, it warps itself to whatever the viewer percieves Hell as, similarly to Paradiso the true appearance can only be seen by those that are above belief.", "Song": "Toby Fox: Black Knife"}, "MAINFRAME": {"Rarity": 500, "Description": "The Foundational Structure that makes up this very reality, it takes the appearance of blue computer hardware when under nobody's control, but will match it's master aesthetic when controlled.", "Song": 'Nevan Dove: "Your_Friend = false"'}, "MAINFRAME//FALLEN": {"Rarity": 5000, "Description": "WATCH AS REALITY CRUMBLES AROUND YOU.", "Song": "Ludicin: Fallen Symphony"}, "R34L1TY": {"Rarity": 1000000, "Description": "Home..?", "Song": "LeaF: Aleph-0"}}
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
Gear(name="Code Fragment", requirements={"Item1": 10000, "Item3": 1000, "Item2": 100, "NullData": 1}, luck_boost=5, speed_boost=3, description="A fragment of useless code")
Gear(name="Data Reconstructer",requirements={"NullData": 10000, "The First Vessel//DATA = NULL": 10,"The First Vessel//S U P R E M A C Y": 1}, luck_boost=10, speed_boost=5, description="A simple mechanism capable of restoring NullData to it's former state.")
Late_Gear(name="Timeline Manipulator", requirements={"Kronos": 1}, luck_boost=100, speed_boost=20,fin_luck_boost=2, description="A simple mechanism capable of altering the flow of time.")
Late_Gear(name="KARMA Manipulator", requirements={"Seraphim": 100, "Apex Predator": 10, "HIM": 1, "The Figure": 1}, luck_boost=1e5, speed_boost=50, fin_luck_boost=10, description="Manipulate the fundemental ideas of good and evil via the manipulation of both sides.")
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
Gear_List.pack()
gear_label.pack()
req_label.pack()
desc_label.pack()
b.pack()
Button(gear_frame, text="Equip selected Gear", bg="black", fg="white", command = lambda: equip(current_gear,collection, gear_label)).pack()
gear_frame.pack()
Nb.add(gear_frame, text="Crafting")
'''----------Save----------'''
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
          GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, root, current_biome, speed))
          GButton.pack()
        else:
          GButton.configure(text=f"God Roll: {God_roll}")
      except:
        GButton = Button(rng_frame, text=f"God Roll: {God_roll}", bg="black", fg="white", command=lambda: god_roll(collection, luck, fin_luck, root, current_biome, speed))
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
      for item in GUI.winfo_children():
         item.destroy()
      root = GUI
      root.config(bg="black")
      root.title("Terminal")
      root.overrideredirect(True)
      root.state("zoomed")
      root.focus_force()
      text = Text(root, bg="black", fg="lime", insertbackground="white", font=("Courier", 12))
      text.pack(fill=BOTH, expand=TRUE)
      terminate.clear()
      terminate_2 = threading.Event()
      terminate_2.clear()
      time.sleep(10)
      def colour_switch(text,event, GUI):
       while event.is_set():
         GUI.after(1000, lambda: text.config(insertbackground="black"))
         GUI.after(1000, lambda: text.config(insertbackground="white"))
      threading.Thread(target= lambda: colour_switch(text, terminate_2, root), daemon=True).start()
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
      for line in lines:
         l = list(line)
         l.append("\n")
         for char in l:
           text.configure(state=NORMAL)
           text.insert(END, f"{char}")
           text.see(END)
           text.configure(state=DISABLED)
           root.update()
           time.sleep(0.05)
         time.sleep(random.uniform(0.3,0.8))
      time.sleep(1)
      terminate_2.set()
      text.destroy()
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
         for i in range(1, len(line) + 1):
               thej_label.config(text=line[:i])
               root.update()
               time.sleep(random.uniform(0.1,0.5))
         time.sleep(2)
         for i in range(len(line), -1, -1):
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
  root.protocol("WM_DELETE_WINDOW", lambda: close(collection, God_roll, God_Roll_req, root, cutscene, threshold)) # Save once the window is closed,  no cheating >:(
  root.mainloop()
```
Module
```Python
import random
import json
import os
from tkinter import *
from pydub import AudioSegment
import threading
import simpleaudio as sa
from abc import abstractmethod, ABC
class GEAR(ABC):
   @abstractmethod
   def check_requirements(self, collection):
      pass # I don't really understand why abcs are nessecary, but if they're being marked they're here.
# It's about as bad as the main program
class Item(): # This was just pain, required recoding of entire rng system.
   instances = [] # Initialising set on instances
   def __init__(self, name, chance_biome, description, rarity_desc, god_roll=False, requirement=True, base_chance=10e100):
      self.__class__.instances.append(self) #From what I understand this appends the class itself to a list
      self.name = name
      self.chance = chance_biome
      self.desc = description
      self.rdesc = rarity_desc
      self.req = requirement
      self.roll = god_roll
      self.base = base_chance
   @classmethod
   def get_instances(cls):
      '''Returns instances of this class'''
      return cls.instances
   @classmethod
   def find(cls, name):
      '''Searches through instances of class and returns instance with correct name'''
      return next((i for i in cls.instances if i.name == name), None) # it checks for each value in our class instances if the name arguement of the class is equivalent to the given name, if not it continues, if so it stops and returns our final value.
   def get_chance(self, current_biome, default):
      '''Return the chance required based on current biome, else return default value'''
      try:
        for b, c in self.chance: # b = biome, c = chance
           if b == current_biome:
              return c
        return default
      except:
         if isinstance(self.chance, int): # If it is obtainable anywhere
           return self.chance
         else:
           return self.base
   def set_requirement_state(self, bool):
      '''Change the requirement status for a class instance'''
      self.req = bool
class Cutscene:
  @staticmethod
  def Cutscene(texts, colours, GUI, wav):
     '''A foundation for any cutscenes I choose to create, flashes through text and colour and uses some music'''
     cutscene = Toplevel(GUI) # Keep relevant parts from prior GUI i.e. the title
     cutscene.state('zoomed') # Fullscreen
     cutscene.focus_force() # Force the window to be focused
     song = AudioSegment.from_wav(wav) # Get song data
     threading.Thread(target=lambda:sa.play_buffer(song.raw_data, num_channels=song.channels, bytes_per_sample=song.sample_width, sample_rate=song.frame_rate), daemon=True).start() # Play the song
     text = Label(cutscene, text="MAINFRAME", font=("Arial", 64), fg="white", bg="black") # Default text
     text.pack(expand=True)
     inter = 100 # Interval between flash
     steps = 30 # Steps
     step = 0 # Initialising amount of steps
     def effect(step):
       '''Flashes through text and colours'''
       # This is complex
       if step < steps: # If there are less steps done than there are set to be done
          bg = colours[step%len(colours)] # background = the index of colours based on the amounts of steps remainder length of colours, i.e. it cycles through each colour every step
          text_change = texts[step%len(texts)] # Cycles through each text every steps
          cutscene.configure(bg=bg) # change background to match step colour
          text.configure(text=text_change, bg=bg) # change text and background to match step text and colour
          step += 1 # Increase step
          cutscene.after(inter, lambda:effect(step)) # Repeat itself
       else:
         cutscene.destroy() # After finishing destroy the GUI
     effect(step) # Begin the effect
  @staticmethod
  def Cutscene_2(text, colours, GUI, wav):
     '''Same as regular cutscene but slowly shows text instead'''
     cutscene = Toplevel(GUI)
     cutscene.state('zoomed')
     cutscene.focus_force()
     song = AudioSegment.from_wav(wav)
     threading.Thread(target= lambda: sa.play_buffer(song.raw_data, num_channels=song.channels, bytes_per_sample=song.sample_width, sample_rate=song.frame_rate), daemon=True).start()
     text2 = Label(cutscene, text="", font=("Arial", 35), fg="grey", bg="black")
     text2.pack(expand=TRUE)
     inter = 4500//len(text)
     steps = len(text)
     step = 0
     sent = "" #sentence
     def effect(step, sentence):
        if step < steps:
           bg=colours[step%len(colours)]
           if step < len(text):
             sentence += text[step%len(text)]
           text_change = sentence
           cutscene.config(bg=bg)
           text2.config(text=text_change, bg=bg)
           step += 1
           cutscene.after(inter, lambda: effect(step, sentence))
        else:
           cutscene.destroy()
     effect(step, sent)
      

class Gamble:
   @staticmethod
   def Rng(collection, luck, GUI, threshold, current_biome):
    '''The actual rolling function, refer mostly loops the rolling and handles the scenario for if you get nothing, this version includes biome-exclusives and biome luck-boosts'''
    items = Item.get_instances()
    items.sort(key=lambda e: e.get_chance(current_biome, e.base), reverse=True)
    for item in items:
        result = Gamble.insert(collection, luck, item.get_chance(current_biome, item.base), item.name, GUI, threshold, item.req, item.roll)
        if result == "Success":
            return  "Success" # Stop rolling on success
   @staticmethod
   def insert(collection, luck, chance, name, GUI, threshold, requirement, god_roll):
      '''Just simplification to avoid clutter, simply adds to the collection, now also runs the cutscene'''
      if random.randint(0,round(chance/luck)) == 0 and requirement and not god_roll: # I am now aware that there is a version of random with weighting, but I'm not recoding this part again
          if name == "MAINFRAME" and int(chance) > threshold:
             GUI.after(0, lambda: Cutscene.Cutscene(colours=["#E5CC99", "#E59796", "#FFFFFF", "#BBE6A8", "#BF80E5","#ABD6EB"], texts=["MAINFRAME", "POWER", "OVERWHELMING", "CORRUPTION", "UNSTABLE", "ERROR", "FAILURE"], GUI=GUI, wav="Why.wav")) # This may look complicated, but it just defines some variables for the function, notably lists of what to flash through
          elif name == "Apex Predator" and chance > threshold:
             GUI.after(0, lambda: Cutscene.Cutscene(colours=["Yellow", "Black"], texts=["Quack"], GUI=GUI, wav="Quack.wav"))
          elif name == "Seraphim" and chance > threshold:
             GUI.after(0, lambda: Cutscene.Cutscene(colours=["#ffe3e3", "#ffffff", "#c0adad"], texts=["Incomprehensible", "Biblical..?", "Divine"], GUI=GUI, wav="Why.wav"))
          elif name == "The First Vessel//DATA = NULL" and chance > threshold:
             GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#585A27", "#C6B922", "#000000"],text="So close to greatness...", GUI=GUI, wav="Why.wav" ))
          elif name == "YOU" and chance > threshold:
             GUI.after(0,lambda: Cutscene.Cutscene_2(colours=['#000000', '#ffffff'], text="...",GUI=GUI, wav="Why.wav"))
          elif name == "YOU//ICARUS" and chance > threshold:
             GUI.after(0,lambda: Cutscene.Cutscene_2(colours=['#000000', '#ffffff'], text="Where is that peak..?", GUI=GUI, wav="Why.wav"))
          collection[name] = collection.get(name, 0) + 1
      else:
          collection["Item1"] = collection.get("Item1", 0) + 1
          return
   @staticmethod
   def biome_change():
      '''Changes the biome'''
      biomes = [
          (500, "MAINFRAME"), (100, "Paradiso"), (100, "HIS Domain"), (5000, "MAINFRAME//FALLEN"), (10, "Shardscapes"), (100, "Precipice of Eternity"), (1000000, "R34L1TY")
      ]
      biomes.sort(key= lambda e: e[0])
      for chance, name in biomes:
         result = Gamble.biome_roll(name, chance)
         if "Success" in result:
            return result[1]
      # If no success after all attempts
      return "Normal"
   @staticmethod
   def biome_roll(name, chance):
      '''A simplified version of the "insert" function for specifically the biome'''
      if random.randint(0,chance) == 0:
         return ["Success", name]
      else:
         return "Failure"
class God_Roll:
   @staticmethod
   def Rng(collection, fin_luck, GUI, current_biome, cutscene):
      '''A Roll function exclusive to God rolls'''
      items = Item.get_instances()
      for item in items:
        result = God_Roll.insert(collection, fin_luck, item.get_chance(current_biome, item.base), item.name, GUI, item.req, item.roll, cutscene)
        if result == "Success":
           return "Success"
        elif result == "Special":
           return "Special"
   @staticmethod
   def insert(collection, luck, chance, name, GUI, requirement, god_roll, cutscene):
    '''Corresponds to the Gamble class'''
    if random.randint(0,round(chance/luck)) == 0 and requirement and god_roll:
       if name == "HIM" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#3b0808", "#000000", "#611c1c", "#380404", "#361515"], text="DID YOU EVER THINK YOU STOOD A CHANCE?", GUI=GUI, wav="Why.wav"))
       elif name == "The Figure" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#ffffff", "#f0ffff", '#fff0ff', '#fffff0'], text='I care for all my "children" but YOU are no child of mine.', GUI=GUI, wav="Why.wav"))
       elif name == "Wizard10989" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#30750b", "#000000"], text="Are you not bored?", GUI=GUI, wav="Why.wav"))
       elif name == "S U P R E M A C Y" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#000000", "#888888","#ffffff"], text="-Arise thy noble warrior-", GUI=GUI, wav="Why.wav"))
       elif name == "The First Vessel//S U P R E M A C Y" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#000000","#888888","#FFFFFF"],text="-Bear witness, to the rebirth of a Primordial-"), GUI=GUI, wav="Why.wav")
       elif name == "Kronos" and cutscene:
        GUI.after(0, lambda: Cutscene.Cutscene_2(colours=["#000000", "#11111111","#22222222", "#33333333", "#44444444", "#55555555", "#66666666", "#77777777", "#88888888"], text="I would spare your life, but it would be a waste.", GUI=GUI, wav="Why.wav"))
       elif name == "Wizard10989//???":
          collection[name] = collection.get(name, 0) + 1
          return "Special"
       collection[name] = collection.get(name, 0) + 1
       return "Success"
    else:
       return "Failure"



class Gear(GEAR):
    instances = []
    def __init__(self, requirements, name, luck_boost, speed_boost, description):
        '''Initialise information about the gear'''
        if isinstance(requirements, list):
            requirements = dict(requirements)
        self.__class__.instances.append(self)
        self.requirements = requirements
        self.name = name
        self.luck_boost = int(luck_boost)
        self.speed_boost = speed_boost
        self.desc = description
    def check_requirements(self, collection):
          '''A function to check if you meet every requirement'''
          return  all(collection.get(k,0) >= v for k,v in self.requirements.items()) # All only returns true if everything value is satisfied, collections.get(k,0) essentially tries to find the key and retrieve the value else it will default to 0, the rest is simple, checking if the value is greater than or equal to that of the pre-defined requirements
    def equip(self, luck, speed, collection, *args,**kargs):
     '''Simple code that increases luck based on the gear luck boost, speed boost will be added in future'''
     if self.check_requirements(collection):
       luck*= self.luck_boost # Change value of luck
       speed /= self.speed_boost
       return luck, speed
     else:
         print("Requirements not met")
    @classmethod
    def find(cls, name):
       '''Finds instances of the gear class'''
       return next((i for i in cls.instances if i.name == name), None)
class Late_Gear(Gear):
   def __init__(self, requirements, name, luck_boost, speed_boost, fin_luck_boost, description):
      super().__init__(requirements, name, luck_boost, speed_boost, description)
      self.fin_luck = fin_luck_boost
   def check_requirements(self, collection):
      '''Checks requirements'''
      return super().check_requirements(collection)
   def equip(self, luck, speed, collection, fin_luck): # I'm pretty sure this is obselete
      '''Equips gear if requirements are met'''
      luck, speed = super().equip(luck, speed, collection)
      if self.check_requirements(collection):
         fin_luck *= self.fin_luck
      return luck, speed, fin_luck

class SaveLoad:
    @staticmethod
    def Save(collection, God_roll, God_Roll_req, cutscene, threshold):
        '''Saves your data to a json file, and makes the previous file a backup'''
        collection["God Roll"] = God_roll
        collection["God Roll Requirement"] = God_Roll_req
        collection["Cutscene"] = cutscene
        collection["threshold"] = threshold
        try:
          if os.path.exists("savefile.json") and collection != {}: # If there is a savefile and your collection isn't empty
            with open("savefile.json", "r") as file: # Read the file
               data = json.load(file)
            with open("backup.json", "w") as file: # Write to the backup file and place the data
               json.dump(data, file)
          with open("savefile.json", "w") as file: # Insert data into main save file
            json.dump(collection, file)
        except json.JSONDecodeError: # If file is corrupted
           print("WARNING: Your back up file or main save file is CORRUPTED")
    @staticmethod
    def Load():
       '''Load your data from your savefile'''
       if os.path.exists("savefile.json"): # If you have saved before
        with open("savefile.json", "r")  as file: # Read the file
          try:
           return json.load(file) # Attempt to return the data
          except json.JSONDecodeError: # If file is corrupted
             print("Savefile is corrupted, attempting to load backup if it exists...")
             if os.path.exists("backup.json"): # If you have a backup
                with open("backup.json", "r") as file: # Read the backup file
                   try:
                      return json.load(file) # Attempt to return backup data
                   except json.JSONDecodeError: # If corrupted
                      print("Backup file is also corrupted.")
                      return {}
             else:
              print("Backup file does not exist.")
              return {}
       else:
          print("You have never saved before.")
          return {} # Return your empty collection
```
## Review

Here we are now, the end, as per usual it meets the stated function and non-functional requirements, but now there is one exception, the final cutscene which can take several seconds to load due to how demanding it is. Other then this it meets all the use cases (except for the one relating to the battle system) as the user is capable of rolling and accessing their collection amongst many other things. Any of the code that would require edting is easy to edit and any core features add ons (such as adding more Items or Gears) are extremely easy to add due to the Item and Gear classes. In theory if this were to be continued the battle system could be re-implemented and the game could be more balanced for some level of enjoyment.

## System Evaluations

The system could easily be improved in future with increased content via more Items or Gears, which would increase the overall content in the game, but the much larger features that could be finally implemented would be the battle system, a feature that was never added to the final product, this would add an entirely new dimension in the game giving use to Items beyond just collecting them, this would be an overall positive change as it would not affect the original gameplay much, it would likely cause the player to need more active involvement.
When evaluating against the function and non-functional requirements and specifications it is difficult to see areas where success has not been achieved (other than the lack of a battle system), as stated *most* functions run in under a second, the save file and overall collection system have been implemented alongside the crafting system and it does not run into any runtime errors (excluding a singular error which has now been patched). Therefore I would say that the program is successful in meeting all set requirements and specifications (excluding those relating to the battle system).
When evaluating against time management, it is massively mixed, although a vast majority of the coding goals were achieved earlier than expected, due to vigor for development decreasing with time, time management worsened with time. The most blatant example of this is the severe lack of the promised battle system, which wasn't implemented because of the lack of time (and ot wanting to figure out how to code another entire aspect of the game), but a majority of coding goals were completed early whilst a majority of design goals were extremely delayed, however the goals relating to installation were all completed extremely early, as it did not change much over time.

OOP classes...
4 of them are static classes... so let's cover them first. So the Cutscene class was simply used as a class for the Gamble and God Roll classes to use, does it need an entire class? Technically no, but I feel as if it increase clarity to seperate it from the others. Gamble and God Roll both serve similar functions, and are the fundemental foundation of the entire program. In theory God Roll should've inherited from Gamble, but I could not find a way for such to happen. Gamble and God Roll run the rng system itself and the functions clearly reflect this, the major reason for their existence outside of the main program is to simply reduce clutter for functions that don't need global variables yet also fit into a neat-ish area. The biome functions in Gamble exist for a similar reason, however the sole reason they are in one class other than two different classes is simply due to the merging of the Gamble class with the Biome class after the new system introduced by the Item class. Before moving onto the real classes a small comment on the SaveLoad class, the class simply contains the saving and loading systems and nothing else, it in itself is extremely useful but doesn't entirely require a class, yet it exists anyway. Now to the real classes. First there is the GEAR class, an abstract base class which simply ensures that the Gear class has a check_requirements function... no comment. The Gear class is one of the essential parts of the game giving luck, final luck and speed boosts turning the game from torturous to tedious, it is a proper requirement and it's existence allows for the easy implementation and integration of gears into the program, using equip and check_requirements rather often for anything relating to gears. Late Gear inherits from Gear is essential to the program, due almost everything being the same as Gear, Late Gear inherits it's initialisation, check requirements and equip from gear to prevent redundancy, Late Gear adds the variable of final luck, something that which regular gear did not have, yes, in theory I simply could've set final luck to 1 as a default value to gear but shhhh. Finally, the biggest and most fundemental class that was also the final addition somehow... the Item class, the class was initially made to allow for the easier integration of the battle system, although the battle system was never added the Item class allowed for easy item descriptions with some class functions allowing for the creation of instances of the Item class without initialising endless variables, the item system allowed for the creation of item systems directly relating to the items themselves when previously all items were simply added to the collection by name and nothing else, the item system also revamped the chance-biome system which in turn revamped the fundemental rolling system. Overall the Item system was inarguably a long-term nessecity to allow for easy addition of items and easier implementation of item-related features.

---

# **THJE END (AGAIN)**