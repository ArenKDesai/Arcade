import pygame
from pygame.locals import *
pygame.init()
import sys
import pygame_gui
import gameplay
from characters import all_characters, all_enemies, all_moves
import sound_player

# Global variables
DISPLAYSURF = pygame.display.set_mode((1440, 900))
# DISPLAYSURF = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
pygame.display.set_caption('Arcade Game')
manager = pygame_gui.UIManager((1440, 900), 'theme.json')
DTAN = pygame.Color(126, 99, 99)
TAN = pygame.Color(168, 124, 124)
BROWN = pygame.Color(80, 60, 60)
DBROWN = pygame.Color(60, 54, 51)
current_elements = []
running = True

# Handling controller input
joystick = None
selected_button = None

# Current player and enemy
player1 = None
player2 = None
enemy = None
battling = False

FPS = pygame.time.Clock()

def exit_game():
    print("Exiting game")
    running = False
    sound_player.button_sound()
    pygame.quit()
    sys.exit()

def clear_elements():
    for element in current_elements:
        if type(element) == gameplay.BetterButton:
            element.button.kill()
        else:
            element.kill()
    current_elements.clear()

def character_selection():
    # Character Selection
    character1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 325), (150, 50)),
                                            text='C1',
                                            manager=manager)
    character2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 325), (150, 50)),
                                            text='C2',
                                            manager=manager)
    character3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 325), (150, 50)),
                                            text='C3',
                                            manager=manager)
    character4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 725), (150, 50)),
                                            text='C4',
                                            manager=manager)
    character5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((645, 725), (150, 50)),
                                            text='C5',
                                            manager=manager)
    character6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1005, 725), (150, 50)),
                                            text='C6',
                                            manager=manager)
    c1_button = gameplay.BetterButton(character1, None, character4, None, character2, select_item)
    current_elements.append(c1_button)
    current_elements.append(gameplay.BetterButton(character2, None, character5, character1, character3, select_item))
    current_elements.append(gameplay.BetterButton(character3, None, character6, character2, None, select_item))
    current_elements.append(gameplay.BetterButton(character4, character1, None, None, character5, select_item))
    current_elements.append(gameplay.BetterButton(character5, character2, None, character4, character6, select_item))
    current_elements.append(gameplay.BetterButton(character6, character3, None, character5, None, select_item))
    selected_button = c1_button
    if joystick:
        c1_button.get_button().select()
    c1_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 125), (150, 150)),
                                              image_surface=pygame.image.load('artwork/c1_icon.png'),
                                              manager=manager)
    c2_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c2_icon.png'),
                                            manager=manager)
    c3_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 125), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c3_icon.png'),
                                            manager=manager)
    c4_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((285, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c4_icon.png'),
                                            manager=manager)
    c5_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((645, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c5_icon.png'),
                                            manager=manager)
    c6_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1005, 525), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c6_icon.png'),
                                            manager=manager)
    current_elements.append(c1_icon)
    current_elements.append(c2_icon)
    current_elements.append(c3_icon)
    current_elements.append(c4_icon)
    current_elements.append(c5_icon)
    current_elements.append(c6_icon)
    return

def run_start_button():
    clear_elements()
    character_selection()
    return

def select_item():
    clear_elements()
    player1 = all_characters['c1']
    # TODO make player choose player2
    player2 = all_characters["c2"]
    # TODO: Item Selection
    item = None
    enemy = all_enemies["goblin"]
    start_battle(player1, player2, enemy)
    return item

# Begin battle
def start_battle(player1, player2, enemy):
    battling = True
    enemy_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((520, 20), (400, 400)),
                                            image_surface=pygame.image.load(f'artwork/{enemy.name}.png'),
                                            manager=manager)
    player1_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((380, 450), (200, 200)),
                                            image_surface=pygame.image.load(f'artwork/{player1.name}.png'),
                                            manager=manager)
    player2_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((860, 450), (200, 200)),
                                            image_surface=pygame.image.load(f'artwork/{player2.name}.png'),
                                            manager=manager)
    # TODO: fill with actual attacks
    attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 700), (200, 100)),
                                            text=f'test',
                                            manager=manager)
    attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 700), (200, 100)),
                                            text=f'test',
                                            manager=manager)
    attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 700), (200, 100)),
                                            text=f'test',
                                            manager=manager)
    attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 700), (200, 100)),
                                            text=f'test',
                                            manager=manager)
    
if __name__ == "__main__":
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 490), (200, 100)),
                                            text='START',
                                            manager=manager)
    start_bb = gameplay.BetterButton(start_button, None, None, None, None, run_start_button)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 670), (200, 100)),
                                            text='EXIT',
                                            manager=manager)
    exit_bb = gameplay.BetterButton(exit_button, None, None, None, None, exit_game)
    start_bb.add_below(exit_bb)
    exit_bb.add_above(start_bb)
    selected_button = start_bb
    current_elements.append(start_bb)
    current_elements.append(exit_bb)
    # Main Game loop
    while(running):
        time_delta = FPS.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
            elif joystick:
                # sending controller input to controller_input
                new_button = gameplay.controller_input(joystick.get_axis(0), joystick.get_axis(1), selected_button, joystick.get_button(0))
                if new_button != None:
                    print("New button")
                    selected_button = new_button
                    sound_player.ui_sound()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for element in current_elements:
                    if event.ui_element == element.button:
                        element.press()
                        sound_player.button_sound()
                        break
            manager.process_events(event)
        if(battling):
            gameplay.battle(player1, player2, enemy)
        # Reset the screen
        manager.update(time_delta)
        DISPLAYSURF.fill(DBROWN)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()