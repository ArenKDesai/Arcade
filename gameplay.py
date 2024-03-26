import random
import pygame
import pygame_gui
import sound_player

class Character:
    def __init__(self, name, hp, attack, defense, speed, mana):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.mana = mana

    def __str__(self):
        return f"{self.name} has {self.hp} HP, {self.attack} attack, {self.defense} defense, and {self.speed} speed."

    def take_damage(self, damage):
        self.hp -= (damage - self.defense)

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for 10 HP.")

    # Will be used for both using and gaining mana
    def change_mana(self, amount):
        self.mana += amount

class Player(Character):
    def __init__(self, name, hp, attack, defense, speed, mana):
        super().__init__(name, hp, attack, defense, speed, mana)

# Enemies have two attacks, one basic, one special. The speical takes mana and happens less frequently.
# The target attribute will determine which character the enemy will attack.
class Enemy(Character):
    def __init__(self, name, hp, attack, defense, speed, mana, target, move1, move2):
        super().__init__(name, hp, attack, defense, speed, mana)
        self.target = target
        self.move1 = move1
        self.move2 = move2
    # Enemy will attack based on what stat it targets
    # TODO make this less repetitive
    def attack(self, player1, player2):
        decision = random.random()
        p1 = player1
        p2 = player2
        if decision > 0.65:
            p2 = player1
            p1 = player2
        if self.target == "hp":
            if p1.hp > p2.hp:
                p1.take_damage(self.__use_move())
            else:
                p2.take_damage(self.__use_move())
        elif self.target == "attack":
            if p1.attack > p2.attack:
                p1.take_damage(self.__use_move())
            else:
                p2.take_damage(self.__use_move())
        elif self.target == "defense":
            if p1.defense > p2.defense:
                p1.take_damage(self.__use_move())
            else:
                p2.take_damage(self.__use_move())
        elif self.target == "speed":
            if p1.speed > p2.speed:
                p1.take_damage(self.__use_move())
            else:
                p2.take_damage(self.__use_move())
        elif self.target == "mana":
            if p1.mana > p2.mana:
                p1.take_damage(self.__use_move())
            else:
                p2.take_damage(self.__use_move())
    # Will be used to determine which move the enemy uses
    def __use_move(self):
        # TODO may have to update for more interesting moves
        if random.random > 0.65 or self.mana < self.move2.cost:
            return self.move1.damage
        else:
            self.change_mana(self.move2.cost)
            return self.move2.damage

class Move:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost
    # TODO implement target
    def __str__(self):
        return f"{self.name} does {self.damage} damage and costs {self.cost} mana."

def speed_check(player1, player2, enemy):
    order = [player1, player2, enemy]
    order.sort(key=lambda x: x.speed, reverse=True) 
    return order

def battle(player1, player2, enemy, attribute):
    order = speed_check(player1, player2, enemy)
    for char in order:
        if char.is_alive():
            if isinstance(char, Player):
                pass
            else:
                enemy.attack(player1, player2)

def choose_enemy():
    # TODO make this work
    return "goblin"

# A class to make buttons easier to work with
# Will include boundries and a function to call when pressed
class BetterButton:
    def __init__(self, button, above, below, left, right, function):
        self.button = button
        self.above = above
        self.below = below
        self.left = left
        self.right = right
        self.function = function
    def get_above(self):
        return self.above
    def get_below(self):
        return self.below
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_button(self):
        return self.button
    def add_above(self, button):
        self.above = button
    def add_below(self, button):
        self.below = button
    def add_left(self, button):
        self.left = button
    def add_right(self, button):
        self.right = button
    def press(self):
        self.function()


# Input: controller input, could be movement or pressing
# Input: selected button, a string indicating the currently selected button
# Output: selects and unselects buttons
def controller_input(x_axis, y_axis, selected_button, x_button):
    if (x_button):
        selected_button.press()
        sound_player.button_sound()
        return None
    elif (x_axis < -0.9 and selected_button.get_left() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_left()
        new_button.get_button().select()
        return new_button
    elif (x_axis > 0.9 and selected_button.get_right() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_right()
        new_button.get_button().select()
        return new_button
    elif (y_axis < -0.9 and selected_button.get_above() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_above()
        new_button.get_button().select()
        return new_button
    elif (y_axis > 0.9 and selected_button.get_below() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_below()
        new_button.get_button().select()
        return new_button
    else:
        return None