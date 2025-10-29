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
