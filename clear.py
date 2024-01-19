import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        # Unsupported operating system
        print("Clear screen not supported on this OS")
