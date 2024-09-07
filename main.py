from interfaces.menu import menu
from interfaces.misc import abort

if __name__ == '__main__':
    while True:
        try:
            menu()
        except KeyboardInterrupt:
            pass