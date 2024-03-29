# Arcade

## For users
To run the game, do these steps:
1. Launch a command prompt. If you don't know how to do this, it will most likely be a difficult step, so look up a video and learn basic commands 'cd' and 'git clone'.
1.5 If you don't have git installed, install it. 
2. Type `git clone {this repository}`. This will download the game to your computer. 
2.5 If you don't have python installed, install it. 
3. Run `pip install -r requirements.txt`. This will install all the packages needed to run the game.
4. Run `python app.py`. This will run the game.

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

## Next Steps
- Fix the cleaned code, which is now broken

# TODO
- Design characters
- Design enemies
- Design backgrounds
- Make moves
- Make transitions (scroll opening, walking to / from combat)
- Make database to hold player data
- Make icon
- Make start screen
- CLean up global variables, replace with parameters?
- Delete time module for pygame.delay
- Make better backgrounds and animations with blit