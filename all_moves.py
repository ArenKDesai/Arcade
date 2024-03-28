class Move:
    def __init__(self, name, user, target):
        self.name = name # Name of the move
        self.user = user # Character using the move
        self.target = target # Character being targeted

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
        super().__init__("slash", user, target)

    def use(self, _):
        self.target.take_damage(10 * (self.user.attack / 10))
        global usr_in
        usr_in = True
        return f'{self.user.name} slashed {self.target.name} for {10 * (self.user.attack / 10)} damage!'
    
class Spit(Move):
    def __init__(self, user, target):
        super().__init__("spit", user, target)

    def use(self, _):
        self.target.take_damage(15 * (self.user.attack / 10))
        self.user.change_mana(-5)
        global usr_in
        usr_in = True
        return f'''
        {self.user.name} spat at {self.target.name} for {15 * (self.user.attack / 10)} damage!
        {self.user.name} lost 5 mana!
        '''
    
class Block(Move):
    def __init__(self, user, target):
        super().__init__("block", user, target)

    def use(self, _):
        print('test')
        self.user.add_buff("defense", 999999)
        global usr_in
        usr_in = True
        return f'{self.user.name} blocked!'
    
    def undo(self):
        self.user.add_buff("defense", -999999)

class Stomp(Move):
    def __init__(self, user, target):
        super().__init__("stomp", user, target)
    
    def use(self, _):
        self.target.take_damage(8 * (self.user.attack / 10))
        global usr_in
        usr_in = True
        return f'{self.user.name} stomped {self.target.name} for {8 * (self.user.attack / 10)} damage!'