import pygame
import pygame_gui
from gameplay import *
from universal import *

# Global Variables
current_elements = []

def start_screen(DISPLAYSURF, manager):
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
