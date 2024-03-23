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

FPS = pygame.time.Clock()

def character_selection():
    # Character Selection
    character1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 250), (150, 50)),
                                            text='C1',
                                            manager=manager)
    
    character2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 250), (150, 50)),
                                            text='C2',
                                            manager=manager)
    character3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 250), (150, 50)),
                                            text='C3',
                                            manager=manager)
    character4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (150, 50)),
                                            text='C4',
                                            manager=manager)
    character5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 450), (150, 50)),
                                            text='C5',
                                            manager=manager)
    character6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 450), (150, 50)),
                                            text='C6',
                                            manager=manager)
    return character1, character2, character3, character4, character5, character6

def character_icons():
    # Character Icons
    # TODO: could make this over the button
    c1_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((100, 90), (150, 150)),
                                          image_surface=pygame.image.load('artwork/c1_icon.png'),
                                          manager=manager)
    c2_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((400, 90), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c2_icon.png'),
                                            manager=manager)
    c3_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((700, 90), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c3_icon.png'),
                                            manager=manager)
    c4_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((100, 290), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c4_icon.png'),
                                            manager=manager)
    c5_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((400, 290), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c5_icon.png'),
                                            manager=manager)
    c6_icon = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((700, 290), (150, 150)),
                                            image_surface=pygame.image.load('artwork/c6_icon.png'),
                                            manager=manager)
    return c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon

def select_attribute(character1, character2, character3, character4, character5, character6,
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
    # TODO: Attribute Selection

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
                    character1, character2, character3, character4, character5, character6 = character_selection()
                    c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon = character_icons()
                # TODO this sucks a lot
                elif event.ui_element == character1:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character2:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character3:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character4:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character5:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)
                elif event.ui_element == character6:
                    select_attribute(character1, character2, character3, character4, character5, character6,
                                     c1_icon, c2_icon, c3_icon, c4_icon, c5_icon, c6_icon)

            manager.process_events(event)

        # Reset the screen
        manager.update(time_delta)
        DISPLAYSURF.fill(color1)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()