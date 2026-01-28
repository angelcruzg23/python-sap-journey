
from os import system
import os 

# nombre = input('Dime tu nombre: ')
# edad = input('Dime tu edad ')

# system('clear')

# print(f'Tu nombre es {nombre}. y edad {edad}')


def clear_screen_cross_platform():
    # Check the operating system name
    if os.name == 'nt':
        # 'cls' is for Windows
        _ = os.system('cls')
    else:
        # 'clear' is for macOS and Linux (where os.name is 'posix')
        _ = os.system('clear')

# Example usage:
print("This will be cleared on any OS...")
input("Press Enter to clear the screen...") # Use input() to pause
clear_screen_cross_platform()
print("Screen cleared successfully.")
