import math

from convert import Mapping
from interfaces.misc import info
from utils import clear, safe_input

def draw_circle():
    clear()

    print("Drawing Circle")
    print()

    info()

    diameter = safe_input('Diameter: ', int, 'Diameter must be an integer')
    radius = diameter / 2

    print()

    for i in range (0, diameter):
        for j in range(0, diameter):
            dx = j - radius + 0.5
            dy = i - radius + 0.5

            current_radius = math.sqrt(dx ** 2 + dy ** 2)

            if current_radius <= radius:
                print('* ', end='')
            else:
                print('  ', end='')
        print()