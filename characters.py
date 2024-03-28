from gameplay import Enemy, Character, Player
from all_moves import *

all_enemies = {
    # name, totalHP, currentHP attack, defense, speed, mana, target, move1, move2
    "goblin_enemy": Enemy("GOBLIN", 50, 10, 5, 5, 10, "hp", Slash("GOBLIN"), Spit("GOBLIN")),
}

all_characters = {
    # name, totalHP, attack, defense, speed, mana
    "goblin": Player("GOBLIN", 100, 10, 5, 5, 10), # Balance
    "horse": Player("HORSE", 50, 5, 5, 10, 20), # Tank
    "heretic": Player("HERETIC", 75, 10, 5, 10, 10), # Spellcaster
    "philosopher": Player("PHILOSOPHER", 150, 15, 10, 5, 5), # Support
    "witch": Player("WITCH", 75, 10, 5, 10, 10), # Debuff
    "gambler": Player("GAMBLER", 100, 5, 10, 5, 10) # Random
}