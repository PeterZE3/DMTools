import dnd

options = ["DMG", "MSAVE"]

while True:
    print("The options are ", options, " (Leave blank to close program)")
    choice = str(input())
    choice = choice.upper()

    if choice == "DMG":
        num_dice = int(input("Total number of dice: "))
        die_size = int(input("Input the die size: "))
        modifier = int(input("Modifer: "))
        rolls = dnd.massroll(num_dice, modifier, die_size)
        total = sum(rolls)
        print(total)

    elif choice == "MSAVE":
        num_saves = int(input("Number of saves: "))
        modifier = int(input("Modifer: "))
        save_DC = int(input("Save DC: "))
        dnd.masssave(num_saves, save_DC, modifier)

    elif choice == "":
        break
    
    else:
        print("Not an option, please try again")
