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