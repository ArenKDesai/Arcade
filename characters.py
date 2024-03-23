import gameplay
import random

all_moves = {
    "slash": gameplay.Move("Slash", 10, 0),
    "spit": gameplay.Move("Spit", 15, 0)
}

all_enemies = {
    "goblin": gameplay.Enemy("Goblin", 50, 10, 5, 5, 10, "hp", all_moves["slash"], all_moves["spit"]),
}

all_characters = {
    "c1": gameplay.Character("Knight", 100, 10, 5, 5, 10),
    "wizard": gameplay.Character("Wizard", 50, 5, 5, 10, 20),
    "rogue": gameplay.Character("Rogue", 75, 10, 5, 10, 10),
    "barbarian": gameplay.Character("Barbarian", 150, 15, 10, 5, 5),
    "archer": gameplay.Character("Archer", 75, 10, 5, 10, 10),
    "cleric": gameplay.Character("Cleric", 100, 5, 10, 5, 10)
}