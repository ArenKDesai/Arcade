# Arcade

## For users
To run the game, do these steps:
1. Launch a command prompt. If you don't know how to do this, it will most likely be a difficult step, so look up a video and learn basic commands 'cd' and 'git clone'. If you don't have git installed, install it.
2. Copy and paste `https://github.com/ArenKDesai/Arcade.git` and hit enter. This will download the game to your computer. If you don't have python installed, [install it](https://www.python.org/downloads/). 
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
- Make delays smoother

# TODO
- Design characters
- Design enemies
- Design backgrounds
- Make moves
- Remove / Smoothen transitions
- Make database to hold player data
- Make icon
- Make start screen
- Rename sounds
- Remove scroll animation
- Add idle animation
- Make separate draw function for drawing enemy and characters
- Fix splash location and enemy / character sizes and location
- Make a plan for how to balance game
- make 6 more characters, separate character selection into two groups
- Fix characters models to be 400x200

# Ideas
## Ogre
- Level 1
- Low defense, medium health
- medium attack

## Drunkard
- Level 1
- Low health, low defense
- medium attack

## Rogue Pop Star
- Level 2
- Low health, low defense
- High attack

## Mushroom Man
- Level 3
- High defense, medium health
- Low attack