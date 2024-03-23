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
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for 10 HP.")

class Player(Character):
    def __init__(self, name, hp, attack, defense, speed, mana):
        super().__init__(name, hp, attack, defense, speed, mana)

class Enemy(Character):
    def __init__(self, name, hp, attack, defense, speed, mana):
        super().__init__(name, hp, attack, defense, speed, mana)