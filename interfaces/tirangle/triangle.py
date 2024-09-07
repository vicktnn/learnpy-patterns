from convert import Mapping
from interfaces.misc import info
from utils import clear, safe_input

from .equilateral import draw_equilateral_triangle
from .right import draw_right_triangle

def draw_triangle():
    clear()

    print("Drawing Triangle")
    print()

    info()

    print("Select the type of triangle you want to draw:")
    print("1. Equilateral triangle (type 'equilateral' / 'equi' / 'equal' / 'eq' / 'e')")
    print("2. Right triangle (type 'right' / 'r')")
    print()

    mapping = (
        (('equilateral', 'equi', 'equal', 'eq', 'e'), draw_equilateral_triangle),
        (('right', 'r'), draw_right_triangle),
    )

    triangle_func = safe_input("Type here: ", Mapping(mapping), "Invalid triangle type.")
    triangle_func()