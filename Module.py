import random, asyncio
from tkinter import *
class Gamble:
  def __init__(self, chance, name):
      self.chance = int(chance)
      self.name = name
  def insert(collection, luck, chance, name):
      if random.randint(0,round(chance/luck)) == 0:
          if name not in collection:
              collection[name] = 1
              return "Success"
          else:
              collection[name] += 1
              return "Success"
      else:
          return "Failure"
<<<<<<< Updated upstream
<<<<<<< Updated upstream
  def Rng(collection, luck):
    items = [
        (1000000000, "MAINFRAME"),
        (1000, "Item2"),
        (10, "Item3")
    ]
    for chance, name in items:
        result = Gamble.insert(collection, luck, chance, name)
        if result == "Success":
            return  # Stop rolling on success
    # If no success after all attempts
    collection["Item1"] = collection.get("Item1", 0) + 1

=======
=======
>>>>>>> Stashed changes
  def Check_Success(collection,luck,chance,name):
      var1 = "Failure"
      count = 0
      while var1 != "Success" and count <= 4:
          Item = Gamble(chance,name)
          var1 = Gamble.insert(collection,luck,Item.chance, Item.name)
          count += 1
  def Rng(collection, luck):
      var1 = Gamble.insert(collection, luck, 1000000000, "MAINFRAME")
      var2 = Gamble.insert(collection, luck, 1000, "Item2")
      Item = Gamble(10,"Item3")
      var3 = Gamble.insert(collection, luck, Item.chance, Item.name)
      if var1 == "Failure" or var2 == "Failure" or var3 == "Failure":
         if "Item1" not in collection:
             collection["Item1"] = 1
         else:
          collection["Item1"] += 1
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
  def placeholder_function(collection):
      print(collection)