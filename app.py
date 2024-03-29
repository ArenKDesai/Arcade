import time
timer = time.time()
print(f"Importing pygame at {time.time() - timer}")
import pygame
print(f"Importing pygame.locals at {time.time() - timer}")
from pygame.locals import *
print(f"Running pygame.init at {time.time() - timer}")
pygame.init()
print(f"Importing sys at {time.time() - timer}")
import sys
print(f"Importing pygame_gui at {time.time() - timer}")
import pygame_gui
print(f"Importing gameplay at {time.time() - timer}")
from gameplay import *
print(f"Importing characters at {time.time() - timer}")
from characters import *
print(f"Importing sound_player at {time.time() - timer}")
import sound_player
print(f"Importing splash_message at {time.time() - timer}")
from universal import *
print(f"Importing pages at {time.time() - timer}")
from pages import *
print(f'Finished imports at {time.time() - timer}')

# Pygame setup
DISPLAYSURF = pygame.display.set_mode((1440, 900))
FPS = pygame.time.Clock()
# DISPLAYSURF = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
pygame.display.set_caption('Arcade Game')
manager = pygame_gui.UIManager((1440, 900), 'theme.json')
# Global variables
# TODO: This can probably be optimized
current_elements = []
running = True
usr_in = True
current_health = []
battling = False
item = None
# Handling controller input
joystick = None
selected_button = None

def exit_game(_):
    print("Exiting game")
    sound_player.button_sound()
    pygame.quit()
    sys.exit()

def character_selection():
    DISPLAYSURF.blit(pygame.image.load('artwork/icon_backgrounds.png'), (0, 0))
    # Character Selection
    character1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 325), (150, 50)),
                                            text='GOBLIN',
                                            manager=manager)
    character2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 325), (150, 50)),
                                            text='HORSE',
                                            manager=manager)
    character3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 325), (150, 50)),
                                            text='PHILOSOPHER',
                                            manager=manager)
    character4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 725), (150, 50)),
                                            text='HERETIC',
                                            manager=manager)
    character5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 725), (150, 50)),
                                            text='WITCH',
                                            manager=manager)
    character6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 725), (150, 50)),
                                            text='GAMBLER',
                                            manager=manager)
    c1_button = BetterButton(character1, second_character_selection)
    c2_button = BetterButton(character2, second_character_selection)
    c3_button = BetterButton(character3, second_character_selection)
    c4_button = BetterButton(character4, second_character_selection)
    c5_button = BetterButton(character5, second_character_selection)
    c6_button = BetterButton(character6, second_character_selection)
    # Setting the boundries for the buttons
    c1_button.add_right(c2_button)
    c1_button.add_below(c4_button)
    c2_button.add_right(c3_button)
    c2_button.add_below(c5_button)
    c2_button.add_left(c1_button)
    c3_button.add_below(c6_button)
    c3_button.add_left(c2_button)
    c4_button.add_right(c5_button)
    c4_button.add_above(c1_button)
    c5_button.add_right(c6_button)
    c5_button.add_above(c2_button)
    c5_button.add_left(c4_button)
    c6_button.add_above(c3_button)
    c6_button.add_left(c5_button)
    current_elements.append(c1_button)
    current_elements.append(c2_button)
    current_elements.append(c3_button)
    current_elements.append(c4_button)
    current_elements.append(c5_button)
    current_elements.append(c6_button)
    global selected_button
    selected_button = c1_button
    if joystick:
        c1_button.get_button().select()
    c1_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/goblin_icon.png'),
                                            manager=manager)
    c2_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/horse_icon.png'),
                                            manager=manager)
    c3_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/philosopher_icon.png'),
                                            manager=manager)
    c4_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/heretic_icon.png'),
                                            manager=manager)
    c5_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/witch_icon.png'),
                                            manager=manager)
    c6_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/gambler_icon.png'),
                                            manager=manager)
    current_elements.append(c1_icon)
    current_elements.append(c2_icon)
    current_elements.append(c3_icon)
    current_elements.append(c4_icon)
    current_elements.append(c5_icon)
    current_elements.append(c6_icon)
    return

def second_character_selection(char):
    global current_elements
    clear_elements(current_elements)
    global enemy
    global player1
    player1 = all_characters[char.lower()]
    print(f'Player has chosen {player1.name}')
    # Character Selection
    character1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 325), (150, 50)),
                                            text='GOBLIN',
                                            manager=manager)
    character2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 325), (150, 50)),
                                            text='HORSE',
                                            manager=manager)
    character3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 325), (150, 50)),
                                            text='PHILOSOPHER',
                                            manager=manager)
    character4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 725), (150, 50)),
                                            text='HERETIC',
                                            manager=manager)
    character5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 725), (150, 50)),
                                            text='WITCH',
                                            manager=manager)
    character6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 725), (150, 50)),
                                            text='GAMBLER',
                                            manager=manager)
    c1_button = BetterButton(character1, select_item)
    c2_button = BetterButton(character2, select_item)
    c3_button = BetterButton(character3, select_item)
    c4_button = BetterButton(character4, select_item)
    c5_button = BetterButton(character5, select_item)
    c6_button = BetterButton(character6, select_item)
    # Setting the boundries for the buttons
    c1_button.add_right(c2_button)
    c1_button.add_below(c4_button)
    c2_button.add_right(c3_button)
    c2_button.add_below(c5_button)
    c2_button.add_left(c1_button)
    c3_button.add_below(c6_button)
    c3_button.add_left(c2_button)
    c4_button.add_right(c5_button)
    c4_button.add_above(c1_button)
    c5_button.add_right(c6_button)
    c5_button.add_above(c2_button)
    c5_button.add_left(c4_button)
    c6_button.add_above(c3_button)
    c6_button.add_left(c5_button)
    current_elements.append(c1_button)
    current_elements.append(c2_button)
    current_elements.append(c3_button)
    current_elements.append(c4_button)
    current_elements.append(c5_button)
    current_elements.append(c6_button)
    global selected_button
    selected_button = c1_button
    if joystick:
        c1_button.get_button().select()
    c1_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 125), (150, 150)),
                                              image_surface=pygame.image.load('artwork/goblin_icon.png'),
                                              manager=manager)
    c2_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/horse_icon.png'),
                                            manager=manager)
    c3_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/philosopher_icon.png'),
                                            manager=manager)
    c4_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/heretic_icon.png'),
                                            manager=manager)
    c5_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/witch_icon.png'),
                                            manager=manager)
    c6_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/gambler_icon.png'),
                                            manager=manager)
    current_elements.append(c1_icon)
    current_elements.append(c2_icon)
    current_elements.append(c3_icon)
    current_elements.append(c4_icon)
    current_elements.append(c5_icon)
    current_elements.append(c6_icon)
    return

def run_start_button(_):
    global current_elements
    clear_elements(current_elements)
    DISPLAYSURF.fill(DBROWN)
    character_selection()
    return

def select_item(char):
    global current_elements
    # TODO: might be able to have less global variables
    clear_elements(current_elements)
    global player2
    player2 = all_characters[char.lower()]
    print(f'Player has chosen {player2.name}')
    # TODO: Item Selection
    item = None
    global enemy
    enemy = all_enemies["drunk"]
    start_battle()
    return item

def walkup(background):
    pygame.time.delay(500)
    for i in range(5):
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(pygame.image.load(f'artwork/transition{i+1}.png'), (0, 0))
        pygame.display.flip()
        pygame.time.delay(5)

# Begin battle
def start_battle():
    global battling
    global DISPLAYSURF
    battling = True
    DISPLAYSURF.blit(pygame.image.load('artwork/grass_background.png'), (0, 0))
    pygame.display.flip()
    walkup(pygame.image.load('artwork/grass_background.png'))
    DISPLAYSURF.blit(pygame.image.load('artwork/grass.png'), (0, 0))
    enemy_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((280, 75), (450, 450)),
                                            image_surface=pygame.image.load(f'artwork/{enemy.name}.png'),
                                            manager=manager)
    pygame.display.flip()
    player1_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((120, 450), (400, 400)),
                                            image_surface=pygame.image.load(f'artwork/{player1.name}.png'),
                                            manager=manager)
    player2_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((440, 450), (400, 400)),
                                            image_surface=pygame.image.load(f'artwork/{player2.name}.png'),
                                            manager=manager)
    # TODO: fix shaking
    # player1.set_sprite(player1_fighter)
    # player2.set_sprite(player2_fighter)
    # enemy.set_sprite(enemy_fighter)
    player1.set_display(DISPLAYSURF, manager)
    player2.set_display(DISPLAYSURF, manager)
    enemy.set_display(DISPLAYSURF, manager)
    draw_health(player1, player2, enemy)

def draw_health(player1, player2, enemy):
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

        
if __name__ == "__main__":
    print(f'Starting game at {time.time() - timer}')
    battle_ptr = 0
    music_player = sound_player.MusicPlayer('honor-and-sword-main-11222.mp3')
    music_player.play()
    
    # Main Game loop
    while(running):
        generic_input = None
        time_delta = FPS.tick(60)/1000.0

        # Controller input
        if joystick:
            # TODO: Fix controller input
            # sending controller input to controller_input
            controller_input(joystick.get_axis(0), joystick.get_axis(1), 
                             selected_button, joystick.get_button(0), generic_input)
            
        # Event handling
        for event in pygame.event.get():
            # Quitting game
            if event.type == pygame.QUIT:
                exit_game(None)
            # Controller connected
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
            # All button pressing
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # Finds the button pressed in current_elements
                for element in current_elements:
                    if event.ui_element == element.button:
                        # Button names will be the function inputs
                        generic_input = element.button.text
                        print(f'Button pressed: {generic_input}')
                        sound_player.button_sound()
                        element.press(generic_input)
                        # If the button is an attack, pause for gameplay
                        if(element.is_attack):
                            usr_in = True
                            clear_elements(current_elements)
                        break
            manager.process_events(event)

        # Battle loop
        if(battling and usr_in):
            # Sorts characters by speed
            order = speed_check(player1, player2, enemy)
            # Switches between characters once per loop
            battle_ptr += 1
            if battle_ptr == 3:
                battle_ptr = 0
            char = order[battle_ptr]
            clear_elements(current_elements)
            # Regen mana & decrement buffs every turn
            char.change_mana(2)
            for buff in char.buffs:
                char.buffs[buff] -= 1
                if char.buffs[buff] == 0:
                    buff.undo()
                    char.buffs.pop(buff)
            # Redraw health bars every turn
            draw_health(player1, player2, enemy)
            if char.is_alive():
                print(f'{char.name}\'s turn!')
                print(f'{char.name} is at {char.get_hp_percent()}')
                if not char.is_enemy():
                    usr_in = False # Pauses gameplay for user input
                    # TODO: Could find a better way to do this
                    char.move1.change_target(enemy)
                    char.move2.change_target(enemy)
                    char.move3.change_target(enemy)
                    char.move4.change_target(enemy)
                    # Display the attack options
                    if(char == player1):
                        # Show attack options
                        attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                                text=f'{char.move1.name.upper()}',
                                                                manager=manager)
                        attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                                text=f'{char.move2.name.upper()}',
                                                                manager=manager)
                        attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                                text=f'{char.move3.name.upper()}',
                                                                manager=manager)
                        attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                                text=f'{char.move4.name.upper()}',
                                                                manager=manager)
                        a1BB = BetterButton(attack1, char.move1.use)
                        a2BB = BetterButton(attack2, char.move2.use)
                        a3BB = BetterButton(attack3, char.move3.use)
                        a4BB = BetterButton(attack4, char.move4.use)
                        # TODO: This can be optimized or turned into a function
                        a1BB.add_below(a3BB)
                        a1BB.add_right(a2BB)
                        a2BB.add_below(a4BB)
                        a2BB.add_left(a1BB)
                        a3BB.add_above(a1BB)
                        a3BB.add_right(a4BB)
                        a4BB.add_above(a2BB)
                        a4BB.add_left(a3BB)
                        a1BB.set_attack()
                        a2BB.set_attack()
                        a3BB.set_attack()
                        a4BB.set_attack()
                        current_elements.append(a1BB)
                        current_elements.append(a2BB)
                        current_elements.append(a3BB)
                        current_elements.append(a4BB)
                    else:
                        attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                                text=f'{char.move1.name.upper()}',
                                                                manager=manager)
                        attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                                text=f'{char.move2.name.upper()}',
                                                                manager=manager)
                        attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                                text=f'{char.move3.name.upper()}',
                                                                manager=manager)
                        attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                                text=f'{char.move4.name.upper()}',
                                                                manager=manager)
                        a1BB = BetterButton(attack1, char.move1.use)
                        a2BB = BetterButton(attack2, char.move2.use)
                        a3BB = BetterButton(attack3, char.move3.use)
                        a4BB = BetterButton(attack4, char.move4.use)
                        a1BB.add_below(a3BB)
                        a1BB.add_right(a2BB)
                        a2BB.add_below(a4BB)
                        a2BB.add_left(a1BB)
                        a3BB.add_above(a1BB)
                        a3BB.add_right(a4BB)
                        a4BB.add_above(a2BB)
                        a4BB.add_left(a3BB)
                        a1BB.set_attack()
                        a2BB.set_attack()
                        a3BB.set_attack()
                        a4BB.set_attack()
                        current_elements.append(a1BB)
                        current_elements.append(a2BB)
                        current_elements.append(a3BB)
                        current_elements.append(a4BB)
                        
                else:
                    # Enemy's turn            
                    enemy.aggro(player1, player2)
                    pygame.time.delay(50)
            # Character is dead
            else:
                # TODO: Change death to only occur once
                if char.is_enemy():
                    sound_player.death_sound()
                    splash_message(f'{char.name} has been defeated!', DISPLAYSURF, manager)
                    pygame.time.delay(3500)
                    battling = False
                else:
                    sound_player.death_sound()
                    splash_message(f'{char.name} has been defeated!', DISPLAYSURF, manager)
                    
        # Reset the screen
        manager.update(time_delta)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()