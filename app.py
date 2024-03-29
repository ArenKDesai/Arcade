import time
timer = time.time()
print(f"Importing pygame at {time.time() - timer}")
import pygame
print(f"Importing pygame.locals at {time.time() - timer}")
from pygame.locals import *
print(f"Running pygame.init at {time.time() - timer}")
pygame.init()
print(f"Importing pygame_gui at {time.time() - timer}")
import pygame_gui
print(f"Importing gameplay at {time.time() - timer}")
from gameplay import *
print(f"Importing characters at {time.time() - timer}")
from characters import *
print(f"Importing sound_player at {time.time() - timer}")
import sound_player
print(f"Importing splash_message at {time.time() - timer}")
from universal import *
print(f"Importing pages at {time.time() - timer}")
from pages import *
print(f'Finished imports at {time.time() - timer}')

if __name__ == "__main__":
    print(f'Starting game at {time.time() - timer}')
    battle_ptr = 0 # Pointer for the battle loop
    music_player = sound_player.MusicPlayer('honor-and-sword-main-11222.mp3')
    music_player.play()

    # Begin game
    start_screen()
    
    # Main Game loop
    while(running):
        generic_input = None
        time_delta = FPS.tick(60)/1000.0

        # Controller input
        if joystick:
            # TODO: Fix controller input
            # sending controller input to controller_input
            controller_input(joystick.get_axis(0), joystick.get_axis(1), 
                             selected_button, joystick.get_button(0), generic_input)
            
        # Event handling
        for event in pygame.event.get():
            # Quitting game
            if event.type == pygame.QUIT:
                exit_game(None)
            # Controller connected
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
            # All button pressing
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # Finds the button pressed in current_elements
                for element in current_elements:
                    if event.ui_element == element.button:
                        # Button names will be the function inputs
                        generic_input = element.button.text
                        print(f'Button pressed: {generic_input}')
                        sound_player.button_sound()
                        element.press(generic_input)
                        # If the button is an attack, pause for gameplay
                        if(element.is_attack):
                            usr_in = True
                            clear_elements(current_elements)
                        break
            manager.process_events(event)

        # Battle loop
        if(battling and usr_in):
            # Sorts characters by speed
            order = speed_check(player1, player2, enemy)
            # Switches between characters once per loop
            battle_ptr += 1
            if battle_ptr == 3:
                battle_ptr = 0
            char = order[battle_ptr]
            clear_elements(current_elements)
            # Regen mana & decrement buffs every turn
            char.change_mana(2)
            for buff in char.buffs:
                char.buffs[buff] -= 1
                if char.buffs[buff] == 0:
                    buff.undo()
                    char.buffs.pop(buff)
            # Redraw health bars every turn
            draw_health(player1, player2, enemy)
            if char.is_alive():
                print(f'{char.name}\'s turn!')
                print(f'{char.name} is at {char.get_hp_percent()}')
                if not char.is_enemy():
                    usr_in = False # Pauses gameplay for user input
                    # TODO: Could find a better way to do this
                    char.move1.change_target(enemy)
                    char.move2.change_target(enemy)
                    char.move3.change_target(enemy)
                    char.move4.change_target(enemy)
                    # Display the attack options
                    if(char == player1):
                        # Show attack options
                        attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                                text=f'{char.move1.name.upper()}',
                                                                manager=manager)
                        attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                                text=f'{char.move2.name.upper()}',
                                                                manager=manager)
                        attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                                text=f'{char.move3.name.upper()}',
                                                                manager=manager)
                        attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                                text=f'{char.move4.name.upper()}',
                                                                manager=manager)
                        a1BB = BetterButton(attack1, char.move1.use)
                        a2BB = BetterButton(attack2, char.move2.use)
                        a3BB = BetterButton(attack3, char.move3.use)
                        a4BB = BetterButton(attack4, char.move4.use)
                        # TODO: This can be optimized or turned into a function
                        a1BB.add_below(a3BB)
                        a1BB.add_right(a2BB)
                        a2BB.add_below(a4BB)
                        a2BB.add_left(a1BB)
                        a3BB.add_above(a1BB)
                        a3BB.add_right(a4BB)
                        a4BB.add_above(a2BB)
                        a4BB.add_left(a3BB)
                        a1BB.set_attack()
                        a2BB.set_attack()
                        a3BB.set_attack()
                        a4BB.set_attack()
                        current_elements.append(a1BB)
                        current_elements.append(a2BB)
                        current_elements.append(a3BB)
                        current_elements.append(a4BB)
                    else:
                        attack1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 680), (200, 100)),
                                                                text=f'{char.move1.name.upper()}',
                                                                manager=manager)
                        attack2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 680), (200, 100)),
                                                                text=f'{char.move2.name.upper()}',
                                                                manager=manager)
                        attack3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 580), (200, 100)),
                                                                text=f'{char.move3.name.upper()}',
                                                                manager=manager)
                        attack4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1150, 580), (200, 100)),
                                                                text=f'{char.move4.name.upper()}',
                                                                manager=manager)
                        a1BB = BetterButton(attack1, char.move1.use)
                        a2BB = BetterButton(attack2, char.move2.use)
                        a3BB = BetterButton(attack3, char.move3.use)
                        a4BB = BetterButton(attack4, char.move4.use)
                        a1BB.add_below(a3BB)
                        a1BB.add_right(a2BB)
                        a2BB.add_below(a4BB)
                        a2BB.add_left(a1BB)
                        a3BB.add_above(a1BB)
                        a3BB.add_right(a4BB)
                        a4BB.add_above(a2BB)
                        a4BB.add_left(a3BB)
                        a1BB.set_attack()
                        a2BB.set_attack()
                        a3BB.set_attack()
                        a4BB.set_attack()
                        current_elements.append(a1BB)
                        current_elements.append(a2BB)
                        current_elements.append(a3BB)
                        current_elements.append(a4BB)
                        
                else:
                    # Enemy's turn            
                    enemy.aggro(player1, player2)
                    pygame.time.delay(50)
            # Character is dead
            else:
                # TODO: Change death to only occur once
                if char.is_enemy():
                    sound_player.death_sound()
                    splash_message(f'{char.name} has been defeated!', DISPLAYSURF, manager)
                    pygame.time.delay(3500)
                    battling = False
                else:
                    sound_player.death_sound()
                    splash_message(f'{char.name} has been defeated!', DISPLAYSURF, manager)
                    
        # Reset the screen
        manager.update(time_delta)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.flip()