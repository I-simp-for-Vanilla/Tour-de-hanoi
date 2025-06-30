# Tower of Hanoi

This project implements the classic Tower of Hanoi game using the `pygame` library. It provides a graphical interface to play and select different difficulty levels.

## Features

- **Main Menu**: Access the main menu to start a game.
- **Level Selection**: Choose from 8 difficulty levels.
- **Interactive Gameplay**: Move disks between towers while following the game rules.
- **Score Screen**: Displays the number of moves made and the optimal score.

## Project Structure

- `main.py`: Contains the main game logic, including menus, event handling, and screen transitions.
- `object.py`: Defines the main game classes, such as `Button`, `Disk`, and `Tower`.
- `var.py`: Contains global variables, such as screen dimensions, colors, and fonts.

## Requirements

- Python 3.10 or higher
- `pygame` library

## Installation

1. Install dependencies:
```bash 
    pip install pygame
```

## Usage

1. Run the game:
```bash
    python main.py
```

2. Navigate through the main menu and select a level.

3. Move the disks by clicking on the towers to solve the puzzle.

## Game Rules

You can only move one disk at a time.
A disk can only be placed on a larger disk or an empty tower.
The goal is to move all disks from the first tower to the last tower while following the rules.

## Author
Antonin Lartillot-Auteuil

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it. 