import random
import pygame
import pygame_gui
import sound_player

class Character:
    def __init__(self, name, totalHP, currentHP, attack, defense, speed, mana):
        self.name = name
        self.totalHP = totalHP
        self.currentHP = currentHP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.mana = mana

    def __str__(self):
        return f"{self.name} has {self.hp} HP, {self.attack} attack, {self.defense} defense, and {self.speed} speed."

    def take_damage(self, damage):
        self.currentHP -= (damage - self.defense)

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.currentHP += amount
        print(f"{self.name} heals for 10 HP.")

    # Will be used for both using and gaining mana
    def change_mana(self, amount):
        self.mana += amount

    def reset_hp(self):
        self.currentHP = self.totalHP

    # TODO fix mana
    def reset_mana(self):
        pass

    def get_hp_percent(self):
        return self.currentHP / self.totalHP

class Player(Character):
    def __init__(self, name, totalHP, currentHP, attack, defense, speed, mana, num):
        super().__init__(name, totalHP, currentHP, attack, defense, speed, mana)
        self.num = num

# Enemies have two attacks, one basic, one special. The speical takes mana and happens less frequently.
# The target attribute will determine which character the enemy will attack.
class Enemy(Character):
    def __init__(self, name, totalHP, currentHP, attack, defense, speed, mana, target, move1, move2):
        super().__init__(name, totalHP, currentHP, attack, defense, speed, mana)
        self.target = target
        self.move1 = move1
        self.move2 = move2
    # Enemy will attack based on what stat it targets
    # TODO make this less repetitive
    # TODO could also introduce attack patterns specifc to enemies
    def attack(self, player1, player2):
        decision = random.random()
        p1 = player1
        p2 = player2
        if decision > 0.65:
            p2 = player1
            p1 = player2
        if self.target == "hp":
            if p1.hp > p2.totalHP:
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
    #TODO: make sure this works
    order = [player1, player2, enemy]
    order.sort(key=lambda x: x.speed, reverse=True) 
    return order


def clear_elements():
    global current_elements
    for element in current_elements:
        if type(element) == BetterButton:
            element.button.kill()
        else:
            element.kill()
    current_elements.clear()

def battle(player1, player2, enemy):
    global DISPLAYSURF
    global manager
    order = speed_check(player1, player2, enemy)
    #TODO: could clean up code
    for char in order:
        clear_elements()
        if char.is_alive():
            if isinstance(char, Player):
                if(char.num == 1):
                    # Draw health bar
                    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 195, 370, 40))
                    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 200, 360, 30))
                    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 200, 360 * char.get_hp_percent(), 30))

                    # Show attack options
                    attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                            text=f'BLOCK',
                                                            manager=manager)
                    attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                            text=f'SLASH',
                                                            manager=manager)
                    attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                            text=f'EXPLODE',
                                                            manager=manager)
                    attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                            text=f'CRY',
                                                            manager=manager)
                    a1BB = BetterButton(attack1, None, attack3, None, attack2, lambda x: char.attack(enemy, "block"))
                    a2BB = BetterButton(attack2, None, attack4, a1BB, None, lambda x: char.attack(enemy, "slash"))
                    a3BB = BetterButton(attack3, attack1, None, None, attack4, lambda x: char.attack(enemy, "explode"))
                    a4BB = BetterButton(attack4, attack2, None, attack3, None, lambda x: char.attack(enemy, "cry"))

                    
                else:
                    # Draw health bar
                    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 275, 370, 40))
                    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 280, 360, 30))
                    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 280, 360 * char.get_hp_percent(), 30))

                    # Show attack options
                    attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                            text=f'BLOCK',
                                                            manager=manager)
                    attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                            text=f'SLASH',
                                                            manager=manager)
                    attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                            text=f'EXPLODE',
                                                            manager=manager)
                    attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                            text=f'CRY',
                                                            manager=manager)

            else:
                # Draw health bar
                pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 355, 370, 40))
                pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 360, 360, 30))
                pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 360, 360 * char.get_hp_percent(), 30))

                # Enemy's turn            
                enemy.attack(player1, player2)

def choose_enemy():
    # TODO make this work
    return "goblin"

# A class to make buttons easier to work with
# Will include boundries and a function to call when pressed
class BetterButton:
    def __init__(self, button, function):
        self.button = button
        self.above = None
        self.below = None
        self.left = None
        self.right = None
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
    # passed generic input
    def press(self, gen_in):
        self.function(gen_in)


# Input: controller input, could be movement or pressing
# Input: selected button, a string indicating the currently selected button
# Output: selects and unselects buttons
def controller_input(x_axis, y_axis, selected_button, x_button, glob_in):
    if (x_button):
        selected_button.press(glob_in)
        sound_player.button_sound()
    elif (x_axis < -0.9 and selected_button.get_left() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_left()
        new_button.get_button().select()
        selected_button = new_button
    elif (x_axis > 0.9 and selected_button.get_right() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_right()
        new_button.get_button().select()
        selected_button = new_button
    elif (y_axis < -0.9 and selected_button.get_above() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_above()
        new_button.get_button().select()
        selected_button = new_button
    elif (y_axis > 0.9 and selected_button.get_below() != None):
        selected_button.get_button().unselect()
        new_button = selected_button.get_below()
        new_button.get_button().select()
        selected_button = new_button