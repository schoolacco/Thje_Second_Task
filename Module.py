import random
import json
import os
from tkinter import *
from pydub import AudioSegment
import threading
import simpleaudio as sa
# It's about as bad as the main program
class Gamble:
  def __init__(self, chance, name):
      '''Initialises variables'''
      self.chance = int(chance)
      self.name = name
  @staticmethod
  def insert(collection, luck, chance, name, GUI):
      '''Just simplification to avoid clutter, simply adds to the collection, now also runs the cutscene'''
      if random.randint(0,round(chance/luck)) == 0:
          if name == "MAINFRAME":
             GUI.after(0, lambda: Gamble.Cutscene(colours=["#E5CC99", "#E59796", "#FFFFFF", "#BBE6A8", "#BF80E5","#ABD6EB"], texts=["MAINFRAME", "POWER", "OVERWHELMING", "CORRUPTION", "UNSTABLE", "ERROR", "FAILURE"], GUI=GUI, wav="Why.wav")) # This may look complicated, but it just defines some variables for the function, notably lists of what to flash through
          if name not in collection:
              collection[name] = 1
              return "Success"
          else:
              collection[name] += 1
              return "Success"
      else:
          return "Failure"
  @staticmethod
  def Rng(collection, luck, GUI):
    '''The actual rolling function, refer mostly loops the rolling and handles the scenario for if you get nothing'''
    items = [
        (1000000000, "MAINFRAME"),
        (1000, "Item2"),
        (10, "Item3")
    ]
    for chance, name in items:
        result = Gamble.insert(collection, luck, chance, name, GUI)
        if result == "Success":
            return  # Stop rolling on success
    # If no success after all attempts
    collection["Item1"] = collection.get("Item1", 0) + 1
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
class Biome(Gamble):
   def __init__(self, chance, name, biome):
      super().__init__(chance, name)
      self.biome = biome
   @staticmethod
   def Rng(collection, luck, GUI, current_biome):
    '''The actual rolling function, refer mostly loops the rolling and handles the scenario for if you get nothing, this version includes biome-exclusives and biome luck-boosts'''
    items = [
        (1000000, "MAINFRAME", "MAINFRAME"), (100, "ItemE", "MAINFRAME"), (1000, "MAINFRAME", "MAINFRAME//FALLEN"), (2, "ItemE", "MAINFRAME//FALLEN"), (1e12, "Apex Predator", ("HIS Domain", "MAINFRAME"))
    ]
    for chance, name, biome in items:
        result = Biome.insert(current_biome, biome, collection, luck, chance, name, GUI)
        if result == "Success":
            return  "Success" # Stop rolling on success
   @staticmethod
   def insert(current_biome, biome, collection, luck, chance, name, GUI):
      '''Just simplification to avoid clutter, simply adds to the collection, now also runs the cutscene'''
      if random.randint(0,round(chance/luck)) == 0 and current_biome in biome:
          if name == "MAINFRAME":
             GUI.after(0, lambda: Gamble.Cutscene(colours=["#E5CC99", "#E59796", "#FFFFFF", "#BBE6A8", "#BF80E5","#ABD6EB"], texts=["MAINFRAME", "POWER", "OVERWHELMING", "CORRUPTION", "UNSTABLE", "ERROR", "FAILURE"], GUI=GUI, wav="Why.wav")) # This may look complicated, but it just defines some variables for the function, notably lists of what to flash through
          elif name == "Apex Predator":
             GUI.after(0, lambda: Gamble.Cutscene(colours=["Yellow", "Black"], texts=["Quack"], GUI=GUI, wav="Quack.wav"))
          if name not in collection:
              collection[name] = 1
              return "Success"
          else:
              collection[name] += 1
              return "Success"
      else:
          return "Failure"
   @staticmethod
   def biome_change():
      '''Changes the biome'''
      biomes = [
          (500, "MAINFRAME"), (100, "Paradiso"), (100, "HIS Domain"), (5000, "MAINFRAME//FALLEN")
      ]
      for chance, name in biomes:
         result = Biome.biome_roll(name, chance)
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
class God_Roll(Gamble):
   @staticmethod
   def Rng(collection, fin_luck, GUI, current_biome):
      items = [
       ("HIM", 1e6, ("HIS Domain", "MAINFRAME")), ("S U P R E M A C Y", 1000, "Any")
      ]
      for name, chance, biome in items:
        result = God_Roll.insert(current_biome, biome, collection, fin_luck, chance, name, GUI)
        if result == "Success":
           return "Success"
   @staticmethod
   def insert(current_biome, biome, collection, luck, chance, name, GUI):
    if biome == "Any":
       biome = current_biome
    if random.randint(0,round(chance/luck)) == 0 and current_biome in biome:
       if name == "HIM":
        GUI.after(0, lambda: Gamble.Cutscene(colours=["#3b0808", "#000000", "#611c1c", "#380404", "#361515"], texts=["DID", "YOU", "EVER", "THINK", "YOU", "STOOD", "A", "CHANCE?"], GUI=GUI, wav="Why.wav"))
       if name not in collection:
          collection[name] = 1
          return "Success"
       else:
          collection[name] += 1
          return "Success"
    else:
       return "Failure"



class Gear:
    def __init__(self, requirements, name, luck_boost):
        '''Initialise information about the gear'''
        if isinstance(requirements, list):
            dict(requirements)
        self.requirements = requirements
        self.name = name
        self.luck_boost = int(luck_boost)
    def check_requirements(self, collection):
          '''A function to check if you meet every requirement'''
          return  all(collection.get(k,0) >= v for k,v in self.requirements.items()) # All only returns true if everything value is satisfied, collections.get(k,0) essentially tries to find the key and retrieve the value else it will default to 0, the rest is simple, checking if the value is greater than or equal to that of the pre-defined requirements
    def equip(self, luck, collection):
     '''Simple code that increases luck based on the gear luck boost, speed boost will be added in future'''
     if self.check_requirements(collection):
       luck = luck * self.luck_boost # Change value of luck
       return luck
     else:
         print("Requirements not met")
class Late_Gear(Gear):
   def __init__(self, requirements, name, luck_boost, speed_boost, fin_luck_boost):
      super().__init__(requirements, name, luck_boost)
      self.speed_boost = speed_boost
      self.fin_luck = fin_luck_boost
   def check_requirements(self, collection):
      return super().check_requirements(collection)
   def equip(self, luck, speed, fin_luck, collection):
      super().equip(luck, collection)
      if self.check_requirements(collection):
         speed %= self.speed_boost
         fin_luck *= self.fin_luck

class SaveLoad:
    @staticmethod
    def Save(collection, God_roll):
        '''Saves your data to a json file, and makes the previous file a backup'''
        collection["God Roll"] = God_roll
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