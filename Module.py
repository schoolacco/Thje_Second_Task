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

  def placeholder_function(collection):
      print(collection)