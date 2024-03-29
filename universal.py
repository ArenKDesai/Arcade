import pygame
import pygame_gui

# Current player and enemy
player1 = None
player2 = None
enemy = None

usr_in = True

def splash_message(content, screen, manager):
    font = pygame.font.Font(None, 30)
    # text = font.render(content, True, (126, 99, 99))
    # splash_background = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((300, 500), (600, 100)),
    #                                         image_surface=pygame.image.load('artwork/splash.png'),
    #                                         manager=manager)
    # splash = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 500), (600, 100)), 
    #                                      text=content, manager=manager)
    # manager.draw_ui(screen)
    # pygame.display.flip()
    # pygame.time.delay(1250)
    # splash.kill()
    # splash_background.kill()
    # manager.draw_ui(screen)
    # pygame.display.flip()