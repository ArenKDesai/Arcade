from gameplay import Enemy, Character, Player
from all_moves import *
from glob_var import enemy

all_enemies = {
    # name, totalHP, attack, defense, speed, mana, target
    "goblin_enemy": Enemy("GOBLIN", 100, 10, 5, 10, 10, "hp"),
}

all_characters = {
    # name, totalHP, attack, defense, speed, mana
    "goblin": Player("GOBLIN", 50, 10, 5, 10, 10, enemy), # Balance
    "horse": Player("HORSE", 75, 8, 10, 10, 15, enemy), # Tank
    "heretic": Player("HERETIC", 35, 10, 2, 15, 50, enemy), # Spellcaster
    "philosopher": Player("PHILOSOPHER", 50, 8, 5, 10, 30, enemy), # Support
    "witch": Player("WITCH", 35, 15, 2, 15, 30, enemy), # Debuff
    "gambler": Player("GAMBLER", 45, 9, 4, 9, 20, enemy) # Random
}