class Character:
    def __init__(self, name, hp, attack, defense, speed, mana):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.mana = mana

    def __str__(self):
        return f"{self.name} has {self.hp} HP, {self.attack} attack, {self.defense} defense, and {self.speed} speed."

    def take_damage(self, damage):
        self.hp -= (damage - self.defense)

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for 10 HP.")

    # Will be used for both using and gaining mana
    def change_mana(self, amount):
        self.mana += amount

class Player(Character):
    def __init__(self, name, hp, attack, defense, speed, mana):
        super().__init__(name, hp, attack, defense, speed, mana)

class Enemy(Character):
    def __init__(self, name, hp, attack, defense, speed, mana, target):
        super().__init__(name, hp, attack, defense, speed, mana)
        self.target = target
    # Enemy will attack based on what stat it targets
    # TODO make this less repetitive
    def attack(self, player1, player2):
        if self.target == "hp":
            if player1.hp > player2.hp:
                player1.take_damage(self.__use_move())
            else:
                player2.take_damage(self.__use_move())
        elif self.target == "attack":
            if player1.attack > player2.attack:
                player1.take_damage(self.__use_move())
            else:
                player2.take_damage(self.__use_move())
        elif self.target == "defense":
            if player1.defense > player2.defense:
                player1.take_damage(self.__use_move())
            else:
                player2.take_damage(self.__use_move())
        elif self.target == "speed":
            if player1.speed > player2.speed:
                player1.take_damage(self.__use_move())
            else:
                player2.take_damage(self.__use_move())
        elif self.target == "mana":
            if player1.mana > player2.mana:
                player1.take_damage(self.__use_move())
            else:
                player2.take_damage(self.__use_move())
    def __use_move(self):
        pass

class Move:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def __str__(self):
        return f"{self.name} does {self.damage} damage and costs {self.cost} mana."

def speed_check(player1, player2, enemy):
    order = [player1, player2, enemy]
    order.sort(key=lambda x: x.speed, reverse=True)
    return order

def battle(player1, player2, enemy, attribute):
    order = speed_check(player1, player2, enemy)
