# Arcade

## For users
Good luck lmao

## For developers

### app.py
This is the main file that runs the game. It imports all the other files and runs the game.

### pages.py
All of the screens and levels in the game. 

### gameplay.py
All of the gameplay functions, player and enemy classes, and combat functions.

### all_moves.py
All of the moves in the game. Coded uniquely for better control.

### sound_player.py
Controls sound. Will need to be updated for Linux. 

### characters.py
A few dictionaries creating the characters of the game. This will most likely be updated with a better method. 

### universal.py
All of the global variables that are used throughout the game.

### requirements.txt
All of the packages needed to run the game.

### theme.json
All of the colors used in the game.

# Next Steps
- Make splash screen so player knows what's happening

# TODO
- Design characters
- Design enemies
- Design backgrounds
- Make moves
- Make transitions (scroll opening, walking to / from combat)
- Make database to hold player data
- Make icon
- Make start screen
- CLean up global variables
- Delete time module for pygame.delay
- Make better backgrounds and animations with blit