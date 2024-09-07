from utils import clear

def abort():
    clear()

    print("Thank you for uisng the app.")
    print()

    exit()

def pause():
    print()
    input("Press enter to continue.")

def info():
    print("You can go back to the main menu by pressing `Ctrl + C`.")
    print()