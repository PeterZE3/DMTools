# DMTools
A python library with many tools for tech inclined DM's who want to automate some of the more menial tasks.  This is project is based around Dungeons and Dragons 5th Edition, but I imagine with a few changes it could be used for other games. 

In this library there are the following functions

All of these functions will not print to the screen by default, so if you want them to print, place them in a print statement

# roll
accepts a die size as the first parameter (Default: 20), and a modifer to add or subtract as the second parameter(Default:0)
Returns an int of die roll plus the modifier

# rolladv
Accepts a Boolean of to print the two rolls to the screen(Defaults:False) and a mod to add or subtract(Default:0)
Returns an int of higher die roll plus the modifier

# rolldisadv
Accepts a Boolean of to print the two rolls to the screen(Defaults:False) and a mod to add or subtract(Default:0)
Returns an int of lower die roll plus the modifier

# massroll
Takes in a number of rolls(int), a modifer for the rolls(int), and a die size(Int).  Returns the list of rolls made

# masssave 
Takes in a number of rolls (int), a modifer for the rolls (int), the DC (int) and a die size(int). Doesn't return anything, but prints the values of the rolls and of they saved or failed

# genstats
Accepts no parameters
Returns a 4d6 drop lowest style stat array as a list

# genprofs
Accepts an int as number of profs to be chosen(Default:2)
Returns a list of chosen profs

# genlan
Accepts an int as number of languages to be chosen(Default:2)
Returns a list of chosen profs, common is always in slot 1

# genrace
Accepts no parameters
Returns a race, and subrace if required

# genhp
Accepts an int as the CR/level(Default:1),  constitution mod(Default:0) as an int, and the die size(Default:8) as an int
Returns an int that is the hp of the creature

# gensaves
Accepts an int as number of saves to be chosen(Default:2)
Returns a list of chosen saves

# genclass
Accepts no parameters
returns a class from the list of offical classes on DNDBeyond

# genweapons
accepts a number of weapons to pick(int), and which list to pick from, the options are simple_melee, simple_ranged, martial_melee, and martial_ranged
returns a list of the chosen weapons

# gentools
accepts a number of tools to pick(int), and which list to pick from, the options are art_tools, gaming_sets, and instruments
returns a list of the chosen weapons

# genname #code from ichabod808
Takes in no parameters
returns a fantasy style name

# crtoprof
Takes in the CR/Level of the creature as an int(No Default)
Returns the prof bonus of the creature as an int

# modcalc
Takes in a stat value as an int(No Default)
Returns the mod of the stat as an int

# ASI
takes in a statblock as a dictonary, then applys an ASI to it and returns the dictonary.

# assignstats
takes in a stats(list) and toptwo(list(valid entries:"STR", "DEX", "CON", "INT", "WIS", "CHA")) Assigns the highest stats from stats list to the toptwo and randomly assigns the rest.  Returns a statblock dictonary

# racialbonus
takes in a statblock dictonary and a race(str).  Applys the racial bonus to the statblock and then returns the statblock.

# randnpc
Takes in a name as a string(Default:""), is name is left blank, generates a name CR as an int(Default:1), Number of profs as an int(Default:2), Number of languages as an int(Default:2), and a Number of saves as an int(Default:2)
returns a formatted string with name, race, hit points, Profiency Bonus, Saves, and profs

# Rollbot
very simple loop that can be used to do large saves or damage rolls

# WIP

genArtificer
genBarbarian
genBard
genBlood_Hunter
genCleric
genDruid
genFighter
genMonk
genPaladin
genRanger
genRogue
genSorcerer
genWarlock
genWizard