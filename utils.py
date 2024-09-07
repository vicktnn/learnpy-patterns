import os

def safe_input(message, converter, error_message):
    value = None

    while True:
        try:
            value = converter(input(message))
            break
        except ValueError:
            print()
            print(error_message)
            print()

    return value

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')