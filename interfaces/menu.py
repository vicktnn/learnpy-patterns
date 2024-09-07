from convert import Mapping
from interfaces.misc import abort, info, pause
from interfaces.rectangle import draw_rect
from interfaces.tirangle import draw_triangle
from interfaces.circle import draw_circle
from utils import clear, safe_input

def menu():
    clear()

    print("Pattern App")
    print()

    info()

    print("What you want to do?")
    print("1. Draw a rectangle (type 'rectangle' / 'rect / 'r')")
    print("2. Draw a triangle (type 'triangle' / 'tri' / 't')")
    print("3. Draw a circle (type 'circle' / 'circ' / 'c')")
    print("4. Quit the app (type 'quit' / 'q' / 'exit' / 'ex')")
    print()

    mapping = (
        (('rectangle', 'rect', 'r'), draw_rect),
        (('triangle', 'tri', 't'), draw_triangle),
        (('circle', 'circ', 'c'), draw_circle),
        (('quit', 'q', 'exit', 'ex'), abort),
    )

    action = safe_input("Type here: ", Mapping(mapping), 'Invalid action.')
    action()

    pause()