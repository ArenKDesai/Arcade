import gameplay

class ExampleEnemy(gameplay.Enemy):
    def __init__(self):
        super().__init__(name="Example Enemy", health=100, attack=10, defense=10, speed=10)

    def __use_move(self):
        