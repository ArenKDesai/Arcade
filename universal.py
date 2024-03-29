import pygame
import pygame_gui

# Current player and enemy
player1 = None
player2 = None
enemy = None
usr_in = True

# Colors
DTAN = pygame.Color(126, 99, 99)
TAN = pygame.Color(168, 124, 124)
BROWN = pygame.Color(80, 60, 60)
DBROWN = pygame.Color(60, 54, 51)

def splash_message(content, screen, manager):
    font = pygame.font.Font(None, 30)
    text = font.render(content, True, (126, 99, 99))
    screen.blit(pygame.image.load('artwork/splash.png'), (0, 0))
    screen.blit(text, (50, 50))
    pygame.display.flip()
    pygame.time.delay(1750)