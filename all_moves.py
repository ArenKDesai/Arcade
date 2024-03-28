class Move:
    def __init__(self, name, user, target):
        self.name = name # Name of the move
        self.user = user # Character using the move
        self.target = target # Character being targeted

    # Will be overridden by the subclasses
    def use(self):
        pass

class Slash(Move):
    def __init__(self, user, target):
        super().__init__("slash", user, target)

    def use(self):
        self.target.take_damage(10 * (self.user.attack / 10))
        usr_in = True
        return f'{self.user.name} slashed {self.target.name} for {10 * (self.user.attack / 10)} damage!'
    
class Spit(Move):
    def __init__(self, userName):
        super().__init__("spit", userName)

    def use(self, user, target, usr_in):
        target.take_damage(15 * (user.attack / 10))
        user.change_mana(-5)
        usr_in = True
        return f'''
        {user.name} spat at {target.name} for {15 * (user.attack / 10)} damage!
        {user.name} lost 5 mana!
        '''
    
class Block(Move):
    def __init__(self, userName):
        super().__init__("block", userName)

    def use(self, user, target, usr_in):
        user.change_buff("defense", 999999)
        usr_in = True
        return f'{user.name} blocked!'
    
    def undo(self, user):
        user.change_buff("defense", -999999)

class Stomp(Move):
    def __init__(self, userName):
        super().__init__("stomp", userName)
    
    def use(self, user, target, usr_in):
        target.take_damage(8 * (user.attack / 10))
        usr_in = True
        return f'{user.name} stomped {target.name} for {8 * (user.attack / 10)} damage!'