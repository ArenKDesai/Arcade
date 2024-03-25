import pygame
from pygame.locals import *
pygame.init()
import sys
import pygame_gui
import gameplay
from characters import all_characters, all_enemies, all_moves

# Global variables
DISPLAYSURF = pygame.display.set_mode((1440, 900))
# DISPLAYSURF = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
pygame.display.set_caption('Arcade Game')
manager = pygame_gui.UIManager((1440, 900), 'theme.json')
DTAN = pygame.Color(126, 99, 99)
TAN = pygame.Color(168, 124, 124)
BROWN = pygame.Color(80, 60, 60)
DBROWN = pygame.Color(60, 54, 51)

# Handling controller input
joystick = None
selected_button = None

# Current player and enemy
player1 = None
player2 = None
enemy = None
battling = False

FPS = pygame.time.Clock()

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
    return character1, character2, character3, character4, character5, character6

def character_icons():
    # Character Icons
    # TODO: could make this over the button
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
    return c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon

def select_item(chosen_char, character1, character2, character3, character4, character5, character6,
                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon):
    character1.kill()
    character2.kill()
    character3.kill()
    character4.kill()
    character5.kill()
    character6.kill()

    c1_icon.kill()
    c2_icon.kill()
    c3_icon.kill()
    c4_icon.kill()
    c5_icon.kill()
    c6_icon.kill()

    player1 = all_characters[chosen_char]
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
    

running = True
if __name__ == "__main__":
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 490), (200, 100)),
                                            text='START',
                                            manager=manager)
    start_bb = gameplay.BoundryButton(start_button, None, None, None, None)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 670), (200, 100)),
                                            text='EXIT',
                                            manager=manager)
    exit_bb = gameplay.BoundryButton(exit_button, None, None, None, None)
    start_bb.add_below(start_bb)
    exit_bb.add_above(exit_bb)
    selected_button = start_bb
    # Main Game loop
    while(running):
        time_delta = FPS.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
            if joystick:
                # sending controller input to controller_input
                selected_button = gameplay.controller_input(joystick.get_axis(0), joystick.get_axis(1), selected_button)
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    start_button.kill()
                    exit_button.kill()
                    # TODO: make this suck less
                    character1, character2, character3, character4, character5, character6 = character_selection()
                    c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon = character_icons()
                elif event.ui_element == exit_button:
                    running = False
                # TODO this sucks a lot
                # TODO add secondary character
                elif event.ui_element == character1:
                    select_item("c1", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character2:
                    select_item("c2", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character3:
                    select_item("c3", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character4:
                    select_item("c4", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character5:
                    select_item("c5", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character6:
                    select_item("c6", character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)

            manager.process_events(event)
        if(battling):
            gameplay.battle(player1, player2, enemy)
        # Reset the screen
        manager.update(time_delta)
        DISPLAYSURF.fill(DBROWN)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()