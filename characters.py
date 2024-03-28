from gameplay import Move, Enemy, Character
import random

all_moves = {
    "slash": Move("Slash", 10, 0),
    "spit": Move("Spit", 15, 0)
}

all_enemies = {
    # name, totalHP, currentHP attack, defense, speed, mana, target, move1, move2
    "goblin": Enemy("Goblin", 50, 50, 10, 5, 5, 10, "hp", all_moves["slash"], all_moves["spit"]),
}

all_characters = {
    # name, totalHP, currentHP attack, defense, speed, mana
    "c1": Character("c1", 100, 10, 10, 5, 5, 10),
    "c2": Character("c2", 50, 5, 5, 5, 10, 20),
    "c3": Character("c3", 75, 10, 10, 5, 10, 10),
    "c4": Character("c4", 150, 15, 15, 10, 5, 5),
    "c5": Character("c5", 75, 10, 10, 5, 10, 10),
    "c6": Character("c6", 100, 5, 5, 10, 5, 10)
}