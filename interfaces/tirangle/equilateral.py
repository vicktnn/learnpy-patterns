from convert import Mapping
from interfaces.misc import info
from utils import clear, safe_input

def draw_equilateral_triangle_0_degree():
    clear()

    print('Drawing 0 Degree Equilateral Triangle')
    print()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(i, size - 1):
            print(' ', end='')
        for j in range(0, i + 1):
            print('* ', end='')
        print()

def draw_equilateral_triangle_180_degrees():
    clear()

    print('Drawing 180 Degrees Equilateral Triangle')
    print()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(0, i):
            print(' ', end='')
        for j in range(i, size):
            print('* ', end='')
        print()

def draw_equilateral_triangle():
    clear()

    print("Drawing Equilateral Triangle")
    print()

    info()

    print("Select the angle (clockwise, starting from 3 o'clock):")
    print("1. 0 degree (type '0')")
    print("3. 180 degrees (type '180')")
    print()

    mapping = (
        (('0',), draw_equilateral_triangle_0_degree),
        (('180',), draw_equilateral_triangle_180_degrees),
    )

    angle_func = safe_input('Type here: ', Mapping(mapping), 'Invalid angle.')
    angle_func()