import random
import string
import math

def roll(die_size = 20, mod = 0):
  roll = random.randint(1,die_size)
  mod = int(mod)
  return roll + mod

def genstats():
   stats = []
   for i in range(0,6):
    rolls = []
    for n in range(0,4):
      num = roll(6)
      rolls.append(num)
    rolls.sort()
    rolls.pop(0)
    total = sum(rolls)
    stats.append(total)
   return stats
        

def rolladv(show = False, mod = 0):
  roll1 = random.randint(1,20)
  roll2 = random.randint(1,20)
  if show == True:
      print(f"{roll1}, {roll2}")
  if roll1 > roll2:
    roll = roll1
  elif roll1 < roll2:
    roll = roll2
  else:
    roll = roll1
  try:
    mod = int(mod)
  except ValueError:
    print("Please input your modifier as only an integer.")
  return roll + mod

def rolldisadv(show = False, mod = 0):
  roll1 = random.randint(1,20)
  roll2 = random.randint(1,20)
  if show == True:
      print(f"{roll1}, {roll2}")
  if roll1 < roll2:
    roll = roll1
  elif roll2 < roll1:
    roll = roll2
  else:
    roll = roll1
  try:
    mod = int(mod)
  except ValueError:
    print("Please input your modifier as only an integer.")
  return roll + mod

def modcalc(stat):
  mod = (stat - 10) // 2
  if mod > 0:
    mod = "+" + str(mod)
  return mod

def genprofs(total_profs: int = 2):
  options = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth",
  "Arcana", "History", "Investigation", "Nature", "Religon", "Animal Handling", 
  "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation",
  "Performance", "Persuasion"]
  profs = []
  i = 0
  while i != total_profs:
    num = random.randint(0, (len(options)-1))
    choice = options.pop(num)
    profs.append(choice)
    i += 1
  return profs

def gensaves(total_saves: int = 2):
  options = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
  saves = []
  i = 0
  while i != total_saves:
    num = random.randint(0, (len(options)-1))
    choice = options.pop(num)
    saves.append(choice)
    i += 1
  return saves

def genlan(total_languages: int = 2): #Common is assumed
  options = ["Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc",
  "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan",
  "Undercommon"]
  lan = ["Common"]
  i = 0
  while i != (total_languages -1):
    num = random.randint(0, (len(options)-1))
    choice = options.pop(num)
    lan.append(choice)
    i += 1
  return lan

def genrace():
  options = ["Human", "Elf", "Dwarf", "Orc", "Half Elf", "Gnome", "Halfling", "Dragonborn",
  "Tiefling", "Aasimar", "Vedalken", "Yuan-ti", "Half Orc", "Orc of Exandria", "Leonin", "Satyr",
  "Fairy", "Harengon", "Owlin", "Aarakocra", "Genasi", "Goliath", "Bugbear", "Firbolg", "Goblin",
  "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Tabaxi", "Triton", "Feral Tiefling", "Tortle", 
  "Changeling", "Kalashtar", "Orc of Eberron", "Shifter", "Warforged", "Gith", "Centaur", "Loxodon",
  "Minotaur", "Simic Hybrid", "Verdan", "Locathah", "Grung"]
  race = options[random.randint(0, (len(options)-1))]
  if race == "Dragonborn":
    types = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Genasi":
    types = ["Water", "Earth", "Fire", "Air"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Elf":
    types = ["High", "Wood", "Dark"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  return race

def genhp(CR: int = 1, Con_mod: int = 0):
  hp = 0
  i = 0
  while i != CR:
    hp += roll(8, Con_mod)
    i += 1
  return hp

def crtoprof(CR: int):
  test = CR / 4
  test = int(math.ceil(test))
  prof = test + 1
  return prof



def randnpc(name: string = "", CR: int = 1, num_profs: int = 2, num_lan: int = 2, num_saves: int = 2):
  statblock = {
  "STR" : "",
  "DEX" : "",
  "CON" : "",
  "INT" : "",
  "WIS" : "",
  "CHA" : ""
  }
  order = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
  printprofs = ""
  printlan = ""
  printsaves = ""
  statprint = ""
  conmod = 0
  stats = genstats()
  for i in range(0,6):
    num = stats[i]
    loc = order[i]
    mod = modcalc(num)
    stat = f"{order[i]}: {num}({mod})"
    statblock[loc] = stat
    if order[i] == "CON":
      conmod = int(modcalc(num))
  hp = genhp(CR, conmod)
  hp = str(hp)
  profbonus = crtoprof(CR)
  profs = genprofs(num_profs)
  race = genrace()
  languages = genlan(num_lan)
  saves  = gensaves(num_saves)
  for e in profs:
    printprofs += (e + ", ")
  for e in languages:
    printlan += (e + ", ")
  for e in saves:
    printsaves += (e + ", ")
  statprint = statblock["STR"] + " " + statblock["DEX"] + " " + statblock["CON"] + " " + statblock["INT"] + " " + statblock["WIS"] + " " + statblock["CHA"]
  printout = f"Name:{name}\nRace:{race}\nHit Points:{hp}\n{statprint}\nProfiency Bonus: +{profbonus}\nSaves:{printsaves}\nProfiencies:{printprofs}\nLanguages:{printlan}"
  return printout



  

#randchar