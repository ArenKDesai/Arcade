from gameplay import Enemy, Character, Player
from all_moves import *
from universal import enemy

all_enemies = {
    # name, totalHP, attack, defense, speed, mana, target
    "drunk": Enemy("DRUNKEN_BRAWLER", 100, 10, 0, 10, 5, "hp"),
}

all_characters = {
    # name, totalHP, attack, defense, speed, mana
    "goblin": Player("GOBLIN", 50, 10, 0, 10, 10, enemy), # Balance
    "horse": Player("HORSE", 80, 8, 10, 5, 15, enemy), # Tank
    "heretic": Player("HERETIC", 35, 15, 0, 15, 50, enemy), # Spellcaster
    "philosopher": Player("PHILOSOPHER", 50, 9, 0, 10, 30, enemy), # Support
    "witch": Player("WITCH", 35, 12, 0, 15, 30, enemy), # Debuff
    "gambler": Player("GAMBLER", 45, 10, 1, 10, 25, enemy) # Random
}