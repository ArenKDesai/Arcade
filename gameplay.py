import random
import pygame
import pygame_gui
import sound_player
from all_moves import *
from universal import *

class Character:
    def __init__(self, name, totalHP, attack, defense, speed, maxMana):
        self.name = name
        self.totalHP = totalHP
        self.currentHP = totalHP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.currentMana = maxMana
        self.maxMana = maxMana
        self.buffs = {}
        self.sprite = None
        self.display = None
        self.manager = None

    def __str__(self):
        return f"{self.name} has {self.hp} HP, {self.attack} attack, {self.defense} defense, and {self.speed} speed."

    def take_damage(self, damage):
        if self.defense < damage:
            self.currentHP -= (damage - self.defense)

    def is_alive(self):
        return self.currentHP > 0

    def heal(self, amount):
        self.currentHP += amount

    # Will be used for both using and gaining mana
    def change_mana(self, amount):
        self.currentMana += amount

    def reset_hp(self):
        self.currentHP = self.totalHP

    # TODO fix mana
    def reset_mana(self):
        pass

    def get_hp_percent(self):
        return self.currentHP / self.totalHP
    
    def add_buff(self, buff, buffDuration):
        self.buffs[buff] = buffDuration

    def set_sprite(self, sprite):
        self.sprite = sprite

    # TODO: fix shaking
    # TODO: There's probably a better way to do this
    def set_display(self, display, manager):
        self.display = display
        self.manager = manager

    def shake(self):
        for _ in range(3):
            self.sprite.get_relative_rect().move_ip(80,0)
            self.display.flip()
            pygame.time.delay(100)
            self.sprite.get_relative_rect().move_ip(-80,0)
            self.display.flip()
            pygame.time.delay(100)


class Player(Character):
    def __init__(self, name, totalHP, attack, defense, speed, mana, enemy):
        super().__init__(name, totalHP, attack, defense, speed, mana)
        self.move1 = Slash(self, enemy)
        self.move2 = Spit(self, enemy)
        self.move3 = Block(self, enemy)
        self.move4 = Stomp(self, enemy)

    def is_enemy(self):
        return False


# Enemies have two attacks, one basic, one special. The speical takes mana and happens less frequently.
# The target attribute will determine which character the enemy will attack.
class Enemy(Character):
    def __init__(self, name, totalHP, attack, defense, speed, mana, target):
        super().__init__(name, totalHP, attack, defense, speed, mana)
        self.target = target
        self.player_target = None
        self.move1 = Slash(self, player1)
        self.move2 = Spit(self, player1)
    # Enemy will attack based on what stat it targets
    # TODO make this less repetitive
    # TODO could also introduce attack patterns specifc to enemies
    def aggro(self, player1, player2):
        decision = random.random()
        p1 = player1
        p2 = player2
        if decision > 0.65:
            p2 = player1
            p1 = player2
        if self.target == "hp":
            if p1.totalHP > p2.totalHP:
                self.__use_move(p1)
            else:
                self.__use_move(p2)
        elif self.target == "attack":
            if p1.attack > p2.attack:
                self.__use_move(p1)
            else:
                self.__use_move()
        elif self.target == "defense":
            if p1.defense > p2.defense:
                self.__use_move(p2)
            else:
                self.__use_move()
        elif self.target == "speed":
            if p1.speed > p2.speed:
                self.__use_move(p1)
            else:
                self.__use_move(p2)
        elif self.target == "mana":
            if p1.totalMana > p2.totalMana:
                self.__use_move(p1)
            else:
                self.__use_move(p2)
    # Will be used to determine which move the enemy uses
    def __use_move(self, player_target):
        # TODO may have to update for more interesting moves
        if random.random() < 0.65 or self.currentMana < self.move2.cost:
            self.move1.change_target(player_target)
            self.move1.use(None)
        else:
            self.move2.change_target(player_target)
            self.move2.use(None)
        
    def is_enemy(self):
        return True

def speed_check():
    player1 = get_player1()
    player2 = get_player2()
    enemy = get_enemy()
    #TODO: make sure this works
    order = [player1, player2, enemy]
    order.sort(key=lambda x: x.speed, reverse=True) 
    return order

def clear_elements(current_elements):
    for element in current_elements:
        if type(element) == BetterButton:
            element.button.kill()
        else:
            element.kill()
    current_elements.clear()

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
        self.is_attack = False
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
    def set_attack(self):
        self.is_attack = True
    def get_is_attack(self):
        return self.is_attack


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

def move_activation(move):
    pass

def draw_health():
    player1 = get_player1()
    player2 = get_player2()
    enemy = get_enemy()

    DISPLAYSURF.blit(pygame.image.load('artwork/template.png'), (0, 0))
    # Draw player names and health percentages
    font = pygame.font.Font(None, 30)
    player1_name = font.render(f'{player1.name}:', True, DTAN)
    player1_health = font.render(f"{player1.currentHP}/{player1.totalHP}", True, DTAN)
    player2_name = font.render(f'{player2.name}:', True, DTAN)
    player2_health = font.render(f"{player2.currentHP}/{player2.totalHP}", True, DTAN)
    enemy_name = font.render(f'{enemy.name}:', True, DTAN)
    enemy_health = font.render(f"{enemy.currentHP}/{enemy.totalHP}", True, DTAN)
    current_health.append(player1_health)
    current_health.append(player2_health)
    current_health.append(enemy_health)

    DISPLAYSURF.blit(player1_name, (970, 255))
    DISPLAYSURF.blit(player1_health, (1250, 255))
    DISPLAYSURF.blit(player2_name, (970, 335))
    DISPLAYSURF.blit(player2_health, (1250, 335))
    DISPLAYSURF.blit(enemy_name, (970, 175))
    DISPLAYSURF.blit(enemy_health, (1250, 175))
    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 275, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 280, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 280, 360 * player1.get_hp_percent(), 30))

    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 355, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 360, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 360, 360 * player2.get_hp_percent(), 30))

    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 195, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 200, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 200, 360 * enemy.get_hp_percent(), 30))

def walkup(background):
    # TODO: fix flashing
    player1 = get_player1()
    player2 = get_player2()
    enemy = get_enemy()

    DISPLAYSURF.blit(background, (0, 0))
    player1_image = pygame.image.load(f'artwork/{player1.name}.png')
    player2_image = pygame.image.load(f'artwork/{player2.name}.png')
    enemy_image = pygame.image.load(f'artwork/{enemy.name}.png')
    DISPLAYSURF.blit(enemy_image, (280, 75))
    pygame.display.flip()
    pygame.time.delay(1000)

    # Allies walk up
    for i in range(100):
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(enemy_image, (280, 75))
        DISPLAYSURF.blit(player1_image, (280, 1640 - (1190/100)*(i+1)))
        DISPLAYSURF.blit(player2_image, (120, 1640 - (1190/100)*(i+1)))
        pygame.display.flip()
        pygame.time.delay(5)

    # Scroll UI opens
    pygame.time.delay(500)
    for i in range(11):
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(pygame.image.load(f'artwork/transition{i+1}.png'), (0, 0))
        DISPLAYSURF.blit(enemy_image, (280, 75))
        DISPLAYSURF.blit(player1_image, (280, 450))
        DISPLAYSURF.blit(player2_image, (120, 450))
        pygame.display.flip()
        pygame.time.delay(5)

