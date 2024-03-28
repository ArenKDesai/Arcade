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
from characters import all_characters, all_enemies, all_moves
print(f"Importing sound_player at {time.time() - timer}")
import sound_player
print(f'Finished imports at {time.time() - timer}')

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
# TODO: Probably don't need this many global variables
selected_button = None

# Current player and enemy
player1 = None
player2 = None
enemy = None
battling = False
item = None

FPS = pygame.time.Clock()

def exit_game(_):
    print("Exiting game")
    global running
    running = False
    sound_player.button_sound()
    pygame.quit()
    sys.exit()

def clear_elements():
    for element in current_elements:
        if type(element) == BetterButton:
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
    c1_button = BetterButton(character1, None, None, None, None, second_character_selection)
    c2_button = BetterButton(character2, None, None, None, None, second_character_selection)
    c3_button = BetterButton(character3, None, None, None, None, second_character_selection)
    c4_button = BetterButton(character4, None, None, None, None, second_character_selection)
    c5_button = BetterButton(character5, None, None, None, None, second_character_selection)
    c6_button = BetterButton(character6, None, None, None, None, second_character_selection)
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

def second_character_selection(char):
    clear_elements()
    global player1
    player1 = all_characters[char.lower()]
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
    c1_button = BetterButton(character1, None, None, None, None, select_item)
    c2_button = BetterButton(character2, None, None, None, None, select_item)
    c3_button = BetterButton(character3, None, None, None, None, select_item)
    c4_button = BetterButton(character4, None, None, None, None, select_item)
    c5_button = BetterButton(character5, None, None, None, None, select_item)
    c6_button = BetterButton(character6, None, None, None, None, select_item)
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

def run_start_button(_):
    clear_elements()
    character_selection()
    return

def select_item(char):
    # TODO: might be able to have less global variables
    clear_elements()
    global player2
    player2 = all_characters[char.lower()]
    # TODO: Item Selection
    item = None
    global enemy
    enemy = all_enemies["goblin"]
    start_battle()
    return item

# Begin battle
def start_battle():
    global battling
    global DISPLAYSURF
    battling = True
    DISPLAYSURF.blit(pygame.image.load('artwork/grass.png'), (0, 0))
    enemy_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((280, 150), (400, 400)),
                                            image_surface=pygame.image.load(f'artwork/{enemy.name}.png'),
                                            manager=manager)
    player1_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((220, 550), (200, 200)),
                                            image_surface=pygame.image.load(f'artwork/{player1.name}.png'),
                                            manager=manager)
    player2_fighter = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((540, 550), (200, 200)),
                                            image_surface=pygame.image.load(f'artwork/{player2.name}.png'),
                                            manager=manager)
    
    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 195, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 200, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 200, 360, 30))

    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 275, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 280, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 280, 360, 30))

    pygame.draw.rect(DISPLAYSURF, (122, 122, 125), pygame.Rect(965, 355, 370, 40))
    pygame.draw.rect(DISPLAYSURF, (160, 21, 61), pygame.Rect(970, 360, 360, 30))
    pygame.draw.rect(DISPLAYSURF, (165, 221, 155), pygame.Rect(970, 360, 360, 30))

        
if __name__ == "__main__":
    print(f'Starting game at {time.time() - timer}')
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 490), (200, 100)),
                                            text='START',
                                            manager=manager)
    start_bb = BetterButton(start_button, None, None, None, None, run_start_button)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((620, 670), (200, 100)),
                                            text='EXIT',
                                            manager=manager)
    exit_bb = BetterButton(exit_button, None, None, None, None, exit_game)
    start_bb.add_below(exit_bb)
    exit_bb.add_above(start_bb)
    selected_button = start_bb
    current_elements.append(start_bb)
    current_elements.append(exit_bb)
    DISPLAYSURF.fill(DBROWN)
    # Main Game loop
    while(running):
        generic_input = None
        time_delta = FPS.tick(60)/1000.0
        if joystick:
            # TODO: Fix controller input
            # sending controller input to controller_input
            controller_input(joystick.get_axis(0), joystick.get_axis(1), 
                                      selected_button, joystick.get_button(0), generic_input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game(None)
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for element in current_elements:
                    if event.ui_element == element.button:
                        DISPLAYSURF.fill(DBROWN)
                        # Button names will be the function inputs
                        generic_input = element.button.text
                        element.press(generic_input)
                        sound_player.button_sound()
                        break
            manager.process_events(event)
        if(battling):
            battle(player1, player2, enemy, item)
        # Reset the screen
        manager.update(time_delta)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()