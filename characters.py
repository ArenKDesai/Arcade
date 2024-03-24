from gameplay import Move, Enemy, Character
import random

all_moves = {
    "slash": Move("Slash", 10, 0),
    "spit": Move("Spit", 15, 0)
}

all_enemies = {
    "goblin": Enemy("Goblin", 50, 10, 5, 5, 10, "hp", all_moves["slash"], all_moves["spit"]),
}

all_characters = {
    "c1": Character("Knight", 100, 10, 5, 5, 10),
    "c2": Character("Wizard", 50, 5, 5, 10, 20),
    "c3": Character("Rogue", 75, 10, 5, 10, 10),
    "c4": Character("Barbarian", 150, 15, 10, 5, 5),
    "c5": Character("Archer", 75, 10, 5, 10, 10),
    "c6": Character("Cleric", 100, 5, 10, 5, 10)
}