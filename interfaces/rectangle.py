from interfaces.misc import info
from utils import clear, safe_input

def draw_rect():
    clear()

    print("Drawing Rectangle")
    print()

    info()

    width = safe_input("Enter the width: ", int, "Width must be an integer.")
    height = safe_input("Enter the height: ", int, "Height must be an integer.")

    print()

    for i in range(0, height):
        for j in range(0, width):
            print('* ', end='')
        print()