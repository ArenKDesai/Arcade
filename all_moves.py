from glob_var import usr_in
import sound_player

class Move:
    def __init__(self, name, user, target, cost):
        self.name = name # Name of the move
        self.user = user # Character using the move
        self.target = target # Character being targeted
        self.cost = cost # Mana cost of the move

    # Will be overridden by the subclasses
    # This will be passed the generic input, but we don't need it
    def use(self, _):
        pass

    def change_target(self, target):
        self.target = target

    def change_user(self, user):
        self.user = user

class Slash(Move):
    def __init__(self, user, target):
        super().__init__("slash", user, target, 0)

    def use(self, _):
        sound_player.slash_sound()
        self.target.take_damage(10 * (self.user.attack / 10))
        print(f'{self.user.name} slashed {self.target.name} for {10 * (self.user.attack / 10) - self.target.defense} damage!')
    
class Spit(Move):
    def __init__(self, user, target):
        super().__init__("spit", user, target, 5)

    def use(self, _):
        sound_player.spit_sound()
        self.target.take_damage(15 * (self.user.attack / 10))
        self.user.change_mana(-5)
        global usr_in
        usr_in = True
        print(f'{self.user.name} spat at {self.target.name} for {15 * (self.user.attack / 10)} damage!')
        print(f'{self.user.name} lost 5 mana!')
    
class Block(Move):
    def __init__(self, user, target):
        super().__init__("block", user, target, 0)

    def use(self, _):
        sound_player.block_sound()
        self.user.add_buff("defense", 999999)
        print(f'{self.user.name} blocks!')
    
    def undo(self):
        self.user.add_buff("defense", -999999)

class Stomp(Move):
    def __init__(self, user, target):
        super().__init__("stomp", user, target, 0)
    
    def use(self, _):
        sound_player.stomp_sound()
        self.target.take_damage(8 * (self.user.attack / 10))
        print(f'{self.user.name} stomped {self.target.name} for {8 * (self.user.attack / 10)} damage!')