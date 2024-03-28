class Move:
    def __init__(self, name, userName):
        self.name = name # Name of the move
        self.userName = userName

    # Will be overridden by the subclasses
    def use(self):
        pass

class Slash(Move):
    def __init__(self, userName):
        super().__init__("slash", userName)

    def use(self, user, target):
        target.take_damage(10 * (user.attack / 10))
        return f'{user.name} slashed {target.name} for {10 * (user.attack / 10)} damage!'
    
class Spit(Move):
    def __init__(self, userName):
        super().__init__("spit", userName)

    def use(self, user, target):
        target.take_damage(15 * (user.attack / 10))
        user.change_mana(-5)
        return f'''
        {user.name} spat at {target.name} for {15 * (user.attack / 10)} damage!
        {user.name} lost 5 mana!
        '''
    
class Block(Move):
    def __init__(self):
        super().__init__("block")

    def use(self, user):
        user.change_buff("defense", 999999)
        return f'{user.name} blocked!'
    
    def undo(self, user):
        user.change_buff("defense", -999999)
