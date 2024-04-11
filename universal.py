import pygame
import pygame_gui

# Pygame setup
# DISPLAYSURF = pygame.display.set_mode((480, 270))
FPS = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
pygame.display.set_caption('Arcade Game')
manager = pygame_gui.UIManager((1440, 900), 'theme.json')

# Global variables
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
    screen.blit(pygame.image.load('artwork/splash.png'), (50, 775))
    screen.blit(text, (90, 820))
    pygame.display.flip()

def get_battling():
    global battling
    return battling

def battling_begin():
    global battling
    battling = True

def battling_end():
    global battling
    battling = False

def get_usr_in():
    global usr_in
    return usr_in

def usr_in_begin():
    global usr_in
    usr_in = True

def usr_in_end():
    global usr_in
    usr_in = False

def get_enemy():
    global enemy
    return enemy

def set_enemy(new_enemy):
    global enemy
    enemy = new_enemy

def get_player1():
    global player1
    return player1

def set_player1(new_player):
    global player1
    player1 = new_player

def get_player2():
    global player2
    return player2

def set_player2(new_player):
    global player2
    player2 = new_player
