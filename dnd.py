
import random
import string
import math

def roll(die_size:int = 20, mod:int = 0):
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
        

def rolladv(show:bool = False, mod:int = 0):
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
  return roll + mod

def rolldisadv(show:bool = False, mod:int = 0):
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
  return roll + mod


def massroll(num_rolls:int, mod:int = 0, die_size:int = 20):
  i = 0
  rolls = []
  while i <+ num_rolls:
    rolls.append(roll(die_size, mod))
    i += 1
  return rolls

def masssave(num_rolls:int, DC:int, mod:int = 0, die_size:int = 20):
  rolls = massroll(num_rolls, mod)
  save_fail = []
  for roll in rolls:
    if roll < DC:
      save_fail.append("Failed")
    if roll >= DC:
      save_fail.append("Saved")
  print(rolls)
  print(save_fail)
  return


def modcalc(stat:int):
  mod = (stat - 10) // 2
  if mod > 0:
    mod = "+" + str(mod)
  return mod

def genprofs(total_profs:int = 2):
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
  "Tiefling", "Aasimar", "Vedalken", "Yuan-ti", "Half Orc", "Leonin", "Satyr",
  "Fairy", "Harengon", "Owlin", "Aarakocra", "Genasi", "Goliath", "Bugbear", "Firbolg", "Goblin",
  "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Tabaxi", "Triton", "Feral Tiefling", "Tortle", 
  "Changeling", "Kalashtar", "Shifter", "Warforged", "Gith", "Centaur", "Loxodon",
  "Minotaur", "Simic Hybrid", "Verdan", "Locathah", "Grung"]
  race = random.choice(options)
  if race == "Dragonborn":
    types = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Genasi":
    types = ["Water", "Earth", "Fire", "Air"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Elf":
    types = ["High", "Wood", "Dark", "Eladrin", "Sea", "Shadar-kai", "Eladrin"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Dwarf":
    types = ["Hill", "Mountain", "Gray"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Shifter":
    types = ["Beasthide", "Longtooth", "Swiftstride", "Wildhunt"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Aasimar":
    types = ["Protector", "Scourge", "Fallen"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Halfling":
    types = ["Lightfoot", "Stout", "Ghostwise"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  if race == "Gnome":
    types = ["Forest", "Rock", "Deep"]
    type = types[random.randint(0, (len(types)-1))]
    race = f"{race} ({type})"
  return race

def genhp(CR: int = 1, Con_mod: int = 0, die_size:int = 8):
  hp = 0
  i = 0
  while i != CR:
    hp += roll(die_size, Con_mod)
    i += 1
  return hp

def crtoprof(CR: int):
  test = CR / 4
  test = int(math.ceil(test))
  prof = test + 1
  return prof


#Code from user ichabod801
def genname():

  FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
    'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has', 
    'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo', 
    'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel', 
    'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']
 
  SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra', 
    'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku', 
    'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak', 
    'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
    'wain', 'wan', 'win', 'wise', 'ya']

  name = random.choice(FIRST) + random.choice(SECOND)

  return name



def genclass():
  classes = ["Artificer", "Barbarian", "Bard", "Blood Hunter", "Cleric", "Druid", "Fighter", "Monk", 
  "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
  choice = random.choice(classes)
  return choice

def genweapons(num_choices: int, list_choice: str):
  simple_melee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]
  simple_ranged = ["Light Crossbow", "Dart", "Shortbow", "Sling"]
  martial_melee = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar",
   "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
  martial_ranged = ["Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
  
  options = []
  
  if list_choice == "simple_melee":
    options = simple_melee
  elif list_choice == "simple_ranged":
    options = simple_ranged
  elif list_choice == "martial_melee":
    options = martial_melee
  elif list_choice == "martial_ranged":
    options = martial_ranged

  choices = []
  i = 0

  while i != num_choices:
    num = random.randint(0, (len(options)-1))
    choice = options.pop(num)
    choices.append(choice)
    i += 1

  return choices

def gentools(num_choices: int, list_choice: str):
  art_tools = ["Alchemists supplies", "Brewers supplies", "Calligraphers Supplies", "Carpenters tools", "Cartographers tools", "Cobblers tools",
  "Cooks utensils", "Glassblowers tools", "Jewelers tools", "Leatherworkers tools", "Masons tools", "Painters supplies", "Potters tools", "Smiths tools",
  "Tinkers tools", "Weavers tools", "Woodcarvers tools", "Navigators tools", "Thieves tools", "Vehicles(land)", "Vehicles(water)"]
  gaming_sets = ["Dice set", "Playing card set"]
  instruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"]

  options = []
  
  if list_choice == "art_tools":
    options = art_tools
  elif list_choice == "gaming_sets":
    options = gaming_sets
  elif list_choice == "instruments":
    options = instruments

  choices = []
  i = 0

  while i != num_choices:
    num = random.randint(0, (len(options)-1))
    choice = options.pop(num)
    choices.append(choice)
    i += 1

  return choices


def ASI(statblock: dict):
  options = ["+2", "+1"]
  choice = random.choice(options)
  stat_options = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

  if choice == "+2":
    stat = random.choice(stat_options)
    statblock[stat] += 2
  elif choice == "+1":
    stat = random.choice(stat_options)
    statblock[stat] += 1
    stat = random.choice(stat_options)
    statblock[stat] += 1

  return statblock



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
  if name == "":
    name = genname()
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

def assignstats(stats:list, toptwo:list):
  i = len(stats) - 1
  order = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
  statblock = {"STR" : 0, "DEX" : 0, "CON" : 0, "INT" : 0, "WIS" : 0, "CHA" : 0}
  stats.sort()

  for e in toptwo:
    statblock[e] = stats[i]
    stats.pop(i)
    order.remove(e)
    i -= 1
  
  i = len(stats) - 1 
  random.shuffle(stats)

  for e in order:
    statblock[e] = stats[i]
    i -= 1

  return statblock


def racialbonus(statblock:dict, race:str):
  STRplus2 = ["Dwarf (Mountain)", "Half Orc", "Goliath", "Bugbear", "Orc", "Githyanki", "Tortle", "Shifter (Longtooth)", 
  "Centaur", "Minotaur", "Dragonborn (Black)", "Dragonborn (Blue)", "Dragonborn (Brass)", "Dragonborn (Bronze)", "Dragonborn (Copper)", 
  "Dragonborn (Gold)", "Dragonborn (Green)", "Dragonborn (Red)", "Dragonborn (Silver)", "Dragonborn (White)",]
  STRplus1 = ["Genasi (Earth)", "Dwarf (Gray)", "Aasimar (Fallen)", "Firbolg", "Triton", 
  "Shifter (Beasthide)", "Leonin"]
  DEXplus2 = ["Elf (High)", "Elf (Wood)", "Elf (Dark)", "Elf (Eladrin)", "Elf (Sea)", "Elf (Shadar-kai)", "Elf (Eladrin)", 
  "Halfling (Lightfoot)", "Halfling (Stout)", "Aarakocra", "Halfling (Ghostwise)", "Feral Tiefling", "Kenku", "Tabaxi", 
  "Goblin", "Kobold", "Shifter (Swiftstride)"]
  DEXplus1 = ["Gnome (Forest)", "Gnome (Deep)", "Genasi (Air)", "Gnome (Deep)", "Bugbear", "Shifter (Longtooth)",
  "Shifter (Wildhunt)", "Satyr"]
  CONplus2 = ["Dwarf (Hill)", "Dwarf (Mountain)", "Genasi (Air)", "Genasi (Earth)", "Genasi (Fire)", "Genasi (Water)",
  "Dwarf (Gray)", "Lizardfolk", "Hobgoblin", "Shifter (Beasthide)", "Loxodon", "Leonin"]
  CONplus1 = ["Halfling (Stout)", "Gnome (Rock)", "Half Orc", "Goliath", "Aasimar (Scourge)", "Triton", "Goblin", "Orc",
  "Elf (Sea)", "Elf (Shadar-kai)", "Verdan", "Minotaur"]
  INTplus2 = ["Gnome (Forest)", "Gnome (Rock)", "Gnome (Deep)", "Vedalken"]
  INTplus1 = ["Elf (High)", "Tiefling", "Elf (Eladrin)", "Genasi (Fire)", "Feral Tiefling", "Hobgoblin", "Yuan-ti",
  "Githyanki", "Githzerai"]
  WISplus2 = ["Firbolg", "Githzerai", "Kalashtar", "Shifter (Wildhunt)"]
  WISplus1 = ["Dwarf (Hill)", "Elf (Wood)", "Aasimar (Protector)", "Aarakocra", "Genasi (Water)", "Halfling (Ghostwise)",
  "Kenku", "Lizardfolk", "Tortle", "Centuar", "Loxodon", "Vedalken", "Centaur"]
  CHAplus2 = ["Tiefling", "Aasimar (Protector)", "Aasimar (Scourge)", "Aasimar (Fallen)", "Yuan-ti", "Verdan", "Satyr"]
  CHAplus1 = ["Elf (Dark)", "Halfling (Lightfoot)", "Tabaxi", "Triton", "Elf (Eladrin)", "Kalashtar", "Shifter (Swiftstride)", 
  "Dragonborn (Black)", "Dragonborn (Blue)", "Dragonborn (Brass)", "Dragonborn (Bronze)", "Dragonborn (Copper)", "Dragonborn (Gold)", 
  "Dragonborn (Green)", "Dragonborn (Red)", "Dragonborn (Silver)", "Dragonborn (White)",]
  special = ["Human", "Half Elf", "Changeling", "Warfoged", "Simic Hybrid", "Fairy", "Harengon", "Owlin"]

  i = 0
  stat_types = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

  if race in STRplus2:
    statblock["STR"] += 2
  if race in STRplus1:
    statblock["STR"] += 1
  if race in DEXplus2:
    statblock["DEX"] += 2
  if race in DEXplus1:
    statblock["DEX"] += 1  
  if race in CONplus2:
    statblock["CON"] += 2
  if race in CONplus1:
    statblock["CON"] += 1
  if race in INTplus2:
    statblock["INT"] += 2
  if race in INTplus1:
    statblock["INT"] += 1
  if race in WISplus2:
    statblock["WIS"] += 2
  if race in WISplus1:
    statblock["WIS"] += 1
  if race in CHAplus2:
    statblock["CHA"] += 2
  if race in CHAplus1:
    statblock["CHA"] += 1
  if race in special:
    if race == "Human": #+1 to all stats
      for t in stat_types:
        statblock[t] += 1
    if race == "Half Elf": #+2 to Cha and +1 to 2 random stats
      statblock["CHA"] += 2
      while i < 2:
        choice = random.choice(stat_types)
        statblock[choice] += 1
        stat_types.remove(choice)
        i += 1
    if race == "Changling": #+2 to Cha and +1 to 1 random stat
      statblock["CHA"] += 2
      statblock[random.choice(stat_types)] += 1
    if race == "Warforged" or race == "Simic Hybrid": #+2 to Con and +1 to 1 random stat
      statblock["CON"] += 2
      statblock[random.choice(stat_types)] += 1
    if race == "Fairy" or race == "Harengon": #+2 to a random stat and +1 to another random stat, or +1 to 3 random stats
      N = random.randint(0,1)
      if N == 0:
        choice = random.choice(stat_types)
        statblock[choice] += 2
        stat_types.remove(choice)
        choice = random.choice(stat_types)
        statblock[choice] += 1
        stat_types.remove(choice)

      if N == 1:
        while i < 3:
          choice = random.choice(stat_types)
          statblock[choice] += 1
          stat_types.remove(choice)
          i += 1
    if race == "Owlin": #+2 to a random stat and +1 to another random stat
      choice = random.choice(stat_types)
      statblock[choice] += 2
      stat_types.remove(choice)
      choice = random.choice(stat_types)
      statblock[choice] += 1
      stat_types.remove(choice)
  return statblock


def genArtificer(Level:int = 1, stats:list = [],  Subclass:str = "", race:str = ""):
    toptwo = ["INT"]
    toptwo.append(random.choice(["DEX", "CON"]))
    subclasses = ["Alchemist", "Armorer", "Artillerist", "Battle Smith"]
    if Subclass == "":
      Subclass = random.choice(subclasses)
    if stats == []:
      stats = genstats()
    statblock = assignstats(stats, toptwo)
    if race == "":
      race = genrace()
    statblock = racialbonus(statblock, race)
    profs = {
      "saves" : ["CON", "INT"],
      "armor" : ["Light", "Medium", "Shields"],
      "weapons" : ["simple", "firearms"],
      "skills" : [],
      "Tools" : ["Thieves Tools", "Tinkers Tools"]
    }

    art_tools = ["Alchemists supplies", "Brewers supplies", "Calligraphers Supplies", "Carpenters tools", "Cartographers tools", "Cobblers tools",
    "Cooks utensils", "Glassblowers tools", "Jewelers tools", "Leatherworkers tools", "Masons tools", "Painters supplies", "Potters tools", "Smiths tools", 
    "Weavers tools", "Woodcarvers tools", "Navigators tools", "Vehicles(land)", "Vehicles(water)"]

    profs["Tools"].append(random.choice(art_tools))



    total_profs = 2
    options = ["Sleight of Hand", "Arcana", "History",
    "Investigation", "Nature", "Medicine", "Perception"]
    i = 0
    while i != total_profs:
      num = random.randint(0, (len(options)-1))
      choice = options.pop(num)
      profs["skills"].append(choice)
      i += 1

    equipment = ["Light Crossbow and 20 bolts", "Thieves Tools", "Dungeoneers Pack"]

    armor_choices = ["Studded Leather", "Scale Mail"]
    equipment.append(random.choice(armor_choices))

    weapons = genweapons(2, "simple_melee")

    for e in weapons:
      equipment.append(e)

    abilities = []

    if Level >= 1:
      abilities.append("Magical Tinkering")
    if Level >= 2:
      abilities.append("Infuse Item")
    if Level >= 3:
      abilities.append("Right Tool for the Job")
      #Subclass Ability
    if Level >= 4:
      statblock = ASI(statblock)
    if Level >= 5:
      pass #Subclass Ability
    if Level >= 6:
      abilities.append("Tool Expertise")
    if Level >= 7:
      abilities.append("Flash of Genius")
    if Level >= 8:
      statblock = ASI(statblock)
    if Level >= 9:
      pass #Subclass Ability
    if Level >= 10:
      abilities.append("Magic Item Adept")
    if Level >= 11:
      abilities.append("Spell-Storing Item")
    if Level >= 12:
      statblock = ASI(statblock)
    if Level >= 13:
      pass #Nothing
    if Level >= 14:
      abilities.append("Magic Item Savant")
    if Level >= 15:
      pass #Subclass Ability
    if Level >= 16:
      statblock = ASI(statblock)
    if Level >= 17:
      pass #Nothing
    if Level >= 18:
      abilities.append("Magic Item Master")
    if Level >= 19:
      statblock = ASI(statblock)
    if Level >= 20:
      abilities.append("Soul of Artifice")

    #Spells
    #infusions














    print(race)
    print(statblock)
    print(toptwo)
    print(profs)
    print(equipment)


  

  
  
    pass
def genBarbarian(Level:int = 1, Subclass:str = ""):   
    pass
def genBard(Level:int = 1, Subclass:str = ""):        
    pass
def genBlood_Hunter(Level:int = 1, Subclass:str = ""):
    pass
def genCleric(Level:int = 1, Subclass:str = ""):      
    pass
def genDruid(Level:int = 1, Subclass:str = ""):
    pass
def genFighter(Level:int = 1, Subclass:str = ""):
    pass
def genMonk(Level:int = 1, Subclass:str = ""):
    pass
def genPaladin(Level:int = 1, Subclass:str = ""):
    pass
def genRanger(Level:int = 1, Subclass:str = ""):
    pass
def genRogue(Level:int = 1, Subclass:str = ""):
    pass
def genSorcerer(Level:int = 1, Subclass:str = ""):
    pass
def genWarlock(Level:int = 1, Subclass:str = ""):
    pass
def genWizard(Level:int = 1, Subclass:str = ""):
    pass


  

def randchar(name:str = "", Level:int = 1, Class:str = "", Subclass:str = ""):
  stats = genstats()
  if Class == "":
    Class = genclass()
  if Class == 'Artificer':
    genArtificer()     
  if Class == 'Barbarian':
    genBarbarian()        
  if Class == 'Bard':
    genBard()
  if Class == 'Blood Hunter':
    genBlood_Hunter()     
  if Class == 'Cleric':
    genCleric()
  if Class == 'Druid':
    genDruid()
  if Class == 'Fighter':
    genFighter()
  if Class == 'Monk':
    genMonk()
  if Class == 'Paladin':
    genPaladin()
  if Class == 'Ranger':
    genRanger()
  if Class == 'Rogue':
    genRogue()
  if Class == 'Sorcerer':
    genSorcerer()
  if Class == 'Warlock':
    genWarlock()
  if Class == 'Wizard':
    genWizard()
