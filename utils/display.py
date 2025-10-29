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

def ask_confirmation(message="Are you sure?"):
    """
    Ask for confirmation from the user
    
    Args:
        message (str): Confirmation message
        
    Returns:
        bool: True if the user confirms (O/o), False otherwise
    """
    response = input(f"\n{message} (O/N) : ").strip().upper()
    return response == 'O'


def display_framed_message(message, width=70, character="*"):
    """
    Display a message in a frame
    
    Args:
        message (str): Message to display
        width (int): Width of the frame
        character (str): Character for the frame
    """
    print("\n" + character * width)
    
    # Handle multi-line messages
    lines = message.split("\n")
    for line in lines:
        padding = (width - len(line) - 4) // 2
        print(f"{character} {' ' * padding}{line}{' ' * (width - len(line) - padding - 4)} {character}")
    
    print(character * width + "\n")

def display_progress_bar(current_value, max_value, width=30, label=""):
    """
    Display a progress bar
    
    Args:
        current_value (int): Current value
        max_value (int): Maximum value
        width (int): Width of the bar
        label (str): Text to display before the bar
    
    Example:
        display_progress_bar(75, 100, 20, "PV")
        # Display: PV [████████████████░░░░] 75/100 (75%)
    """
    if max_value == 0:
        percentage = 0
    else:
        percentage = int((current_value / max_value) * 100)
    
    filled = int((current_value / max_value) * width) if max_value > 0 else 0
    empty = width - filled
    
    # Choose the symbol according to the percentage
    if percentage > 50:
        symbol = "█"
    elif percentage > 20:
        symbol = "▓"
    else:
        symbol = "░"
    
    bar = symbol * filled + "░" * empty
    
    if label:
        print(f"{label} [{bar}] {current_value}/{max_value} ({percentage}%)")
    else:
        print(f"[{bar}] {current_value}/{max_value} ({percentage}%)")

def wait_for_input(message="Press Enter to continue..."):
    """
    Wait for the user to press Enter
    
    Args:
        message (str): Message to display
    """
    input(f"\n{message}")