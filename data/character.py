class Character:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.mana = 100
        self.gold = 4000
        self.armor = 5

        self.str = 10
        self.int = 10
        self.agi = 10


class Player(Character):
    """
    {'helmet' : {
        'id': 12,
        'str': 1,
        'int': 0,
        'type': 1
    }}
    """
    def __init__(self):
        super().__init__()

        self.name = 'Player'
        self.Player = True

        self.level = 1
        self.exp = 0

        self.agi = 30

        self.current_weapon = ""
        self.equipment = [] # id
        self.items = []

    def gain_exp(self, amount):
        self.exp += amoumt
        if exp >= levelcap:
            self.level_up()

    def level_up(self):
        pass

class Monster(Character):
    def __init__(self):
        super().__init__()

        self.name = "Monster"
        self.Enemy = True
