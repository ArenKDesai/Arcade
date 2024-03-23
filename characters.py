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

}