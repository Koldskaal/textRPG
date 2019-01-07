from termcolor import colored

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

        self.name = colored('Player', 'blue', attrs=['bold',])
        self.Player = True

        self.level = 1
        self.exp = 0

        self.agi = 30

        self.current_weapon = ""
        self.equipment = [] # id
        self.items = []
        self.levelcap = 5+3*self.level**2

    def gain_exp(self, amount):
        self.exp += amount
        print(f"You gained {amount} experience!")
        if self.levelcap-self.exp <=0:
            print(f"Required experience untill next level: 0")
        else:
            print(f"Required experience untill next level: {self.levelcap-self.exp}")
        if self.exp >= self.levelcap:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = self.exp-self.levelcap
        print (f"Level up! You are now level {self.level}!")

class Monster(Character):
    def __init__(self):
        super().__init__()

        self.name = colored('Monster', 'magenta', attrs=['bold',])
        self.Enemy = True

        self.loot_table = 'table_x'
