"""
utils/display.py
Utility functions for displaying in the terminal
"""

import os
import sys


def clear_screen():
    """
    Clear the terminal screen
    Compatible Windows, Linux and macOS
    """
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux and macOS
    else:
        os.system('clear')


def display_title(text, width=70):
    """
    Display a framed title
    
    Args:
        text (str): Title text
        width (int): Width of the frame
    """
    print("\n" + "=" * width)
    print(text.center(width))
    print("=" * width)


def display_separator(character="=", width=70):
    """
    Display a separator line
    
    Args:
        character (str): Character to use
        width (int): Width of the line
    """
    print(character * width)

def display_menu(options, title=None):
    """
    Display a menu with numbered options
    
    Args:
        options (list): List of options to display
        title (str, optional): Title of the menu
    """
    if title:
        display_title(title)
    
    print()
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")


def display_framed_message(message, width=70, character="*"):
    """
    Display a message in a frame
    
    Args:
        message (str): Message to display
        width (int): Width of the frame
        character (str): Character for the frame
    """
    print("\n" + character * width)
    
    # Gérer les messages multi-lignes
    lines = message.split("\n")
    for line in lines:
        padding = (width - len(line) - 4) // 2
        print(f"{character} {' ' * padding}{line}{' ' * (width - len(line) - padding - 4)} {character}")
    
    print(character * width + "\n")