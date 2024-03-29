import pygame
import pygame_gui

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
item = 'test'
# Handling controller input
joystick = None
selected_button = None

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

# TODO: move this to a different file
def splash_message(content, screen, manager):
    font = pygame.font.Font(None, 30)
    text = font.render(content, True, (126, 99, 99))
    screen.blit(pygame.image.load('artwork/splash.png'), (0, 0))
    screen.blit(text, (50, 50))
    pygame.display.flip()
    pygame.time.delay(1750)