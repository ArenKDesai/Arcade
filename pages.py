import pygame
import pygame_gui
from gameplay import *
from universal import *
from characters import *
import sys

def start_screen():
    global current_elements
    global selected_button
    global DISPLAYSURF
    global manager

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 490), (200, 100)),
                                        text='START',
                                        manager=manager)
    start_bb = BetterButton(start_button, run_start_button)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 670), (200, 100)),
                                            text='EXIT',
                                            manager=manager)
    exit_bb = BetterButton(exit_button, exit_game)
    start_bb.add_below(exit_bb)
    exit_bb.add_above(start_bb)
    selected_button = start_bb
    current_elements.append(start_bb)
    current_elements.append(exit_bb)
    DISPLAYSURF.fill(DBROWN)

# Begin battle
def start_battle():
    global battling
    global current_elements
    global DISPLAYSURF
    global manager
    global player1
    global player2
    global enemy

    battling = True
    DISPLAYSURF.blit(pygame.image.load('artwork/grass_background.png'), (0, 0))
    pygame.display.flip()
    walkup(pygame.image.load('artwork/grass_background.png'))
    DISPLAYSURF.blit(pygame.image.load('artwork/grass.png'), (0, 0))
    enemy_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((280, 75), (450, 450)),
                                            image_surface=pygame.image.load(f'artwork/{enemy.name}.png'),
                                            manager=manager)
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
    pygame.display.flip()
    draw_health(player1, player2, enemy)

def select_item(char):
    global current_elements
    global player2
    global enemy

    clear_elements(current_elements)
    player2 = all_characters[char.lower()]
    print(f'Player has chosen {player2.name}')
    # TODO: Item Selection
    item = None
    # TODO: Enemy selection
    enemy = all_enemies["drunk"]
    start_battle()
    return item

def run_start_button(_):
    global current_elements
    global DISPLAYSURF

    clear_elements(current_elements)
    DISPLAYSURF.fill(DBROWN)
    character_selection()
    return

def exit_game(_):
    print("Exiting game")
    sound_player.button_sound()
    pygame.quit()
    sys.exit()

def character_selection():
    global current_elements
    global selected_button
    global DISPLAYSURF
    global manager

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
    global enemy
    global player1
    global selected_button
    global manager

    clear_elements(current_elements)
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
