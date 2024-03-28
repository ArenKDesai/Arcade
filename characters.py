from gameplay import Enemy, Character, Player
from all_moves import *
from glob_var import enemy

all_enemies = {
    # name, totalHP, currentHP attack, defense, speed, mana, target
    "goblin_enemy": Enemy("GOBLIN", 200, 6, 5, 5, 5, "hp"),
}

all_characters = {
    # name, totalHP, attack, defense, speed, mana
    "goblin": Player("GOBLIN", 100, 10, 10, 10, 10, enemy), # Balance
    "horse": Player("HORSE", 150, 4, 15, 10, 15, enemy), # Tank
    "heretic": Player("HERETIC", 75, 10, 5, 15, 50, enemy), # Spellcaster
    "philosopher": Player("PHILOSOPHER", 100, 5, 10, 10, 30, enemy), # Support
    "witch": Player("WITCH", 75, 8, 6, 15, 30, enemy), # Debuff
    "gambler": Player("GAMBLER", 90, 9, 9, 9, 20, enemy) # Random
}