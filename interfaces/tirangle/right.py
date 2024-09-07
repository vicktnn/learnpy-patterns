from convert import Mapping
from interfaces.misc import info
from utils import clear, safe_input

def draw_right_triangle_0_degree():
    clear()

    print("Drawing 0 Degree Right Triangle")
    print()

    info()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(0, i + 1):
            print('* ', end='')
        print()

def draw_right_triangle_90_degrees():
    clear()

    print("Drawing 90 Degrees Right Triangle")
    print()

    info()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(i, size):
            print('* ', end='')
        print()

def draw_right_triangle_180_degrees():
    clear()

    print("Drawing 180 Degrees Right Triangle")
    print()

    info()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(0, i):
            print('  ', end='')
        for k in range(i, size):
            print('* ', end='')
        print()

def draw_right_triangle_270_degrees():
    clear()

    print("Drawing 270 Degrees Right Triangle")
    print()

    info()

    size = safe_input('Enter the size: ', int, 'Size must be an integer.')

    print()

    for i in range(0, size):
        for j in range(i, size - 1):
            print('  ', end='')
        for k in range(0, i + 1):
            print('* ', end='')
        print()

def draw_right_triangle():
    clear()

    print("Drawing Right Triangle")
    print()

    info()

    print("Select the angle (clockwise, starting from 3 o'clock):")
    print("1. 0 degree (type '0')")
    print("2. 90 degrees (type '90')")
    print("3. 180 degrees (type '180')")
    print("4. 270 degrees (type '270')")
    print()

    mapping = (
        (('0',), draw_right_triangle_0_degree),
        (('90',), draw_right_triangle_90_degrees),
        (('180',), draw_right_triangle_180_degrees),
        (('270',), draw_right_triangle_270_degrees),
    )

    angle_func = safe_input('Type here: ', Mapping(mapping), 'Invalid angle.')
    angle_func()