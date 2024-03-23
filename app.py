import pygame
from pygame.locals import *
pygame.init()
import sys
import pygame_gui

# Global variables
DISPLAYSURF = pygame.display.set_mode((1000, 600))
# DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.FULLSCREEN)
pygame.display.set_caption('Arcade Game')
manager = pygame_gui.UIManager((1000, 600), 'theme.json')
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(62, 180, 137)    # Mint

test = False

FPS = pygame.time.Clock()

def start_game():
    # Character Selection
    test = True
    character1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 50), (150, 200)),
                                            text='C1',
                                            manager=manager)
    character2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 50), (150, 200)),
                                            text='C2',
                                            manager=manager)
    character3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 50), (150, 200)),
                                            text='C3',
                                            manager=manager)
    character4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 300), (150, 200)),
                                            text='C4',
                                            manager=manager)
    character5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 300), (150, 200)),
                                            text='C5',
                                            manager=manager)
    character6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 300), (150, 200)),
                                            text='C6',
                                            manager=manager)
    return character1, character2, character3, character4, character5, character6

def select_attribute(character1, character2, character3, character4, character5, character6):
    character1.kill()
    character2.kill()
    character3.kill()
    character4.kill()
    character5.kill()
    character6.kill()
    # Attribute Selection

running = True
if __name__ == "__main__":
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 350), (200, 100)),
                                            text='START',
                                            manager=manager)
    # Main Game loop
    while(running):
        time_delta = FPS.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    start_button.kill()
                    # TODO: make this suck less
                    character1, character2, character3, character4, character5, character6 = start_game()
                elif event.ui_element == character1:
                    print("Character 1 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
                elif event.ui_element == character2:
                    print("Character 2 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
                elif event.ui_element == character3:
                    print("Character 3 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
                elif event.ui_element == character4:
                    print("Character 4 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
                elif event.ui_element == character5:
                    print("Character 5 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
                elif event.ui_element == character6:
                    print("Character 6 selected")
                    select_attribute(character1, character2, character3, character4, character5, character6)
            manager.process_events(event)
        if test:
            button_image = pygame.image.load("artwork/cat_icon.jpg").convert_alpha()
            button_rect = button_image.get_rect()
            button_rect.topleft = character1.rect.topleft
            DISPLAYSURF.blit(button_image, button_rect)

        # Reset the screen
        manager.update(time_delta)
        DISPLAYSURF.fill(color1)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()
