from termcolor import colored

class Character:
    def __init__(self):
        self.name = ""
        self.max_health = self.health = 100
        self.max_mana = self.mana = 100
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
        self.levelcap = 5+4*self.level**2
        self.str += 2
        self.agi += 2
        self.int += 2
        self.max_health = self.health = 100 + self.level*20-20
        self.max_mana = self.mana = 100 + self.level*20-20
        print (f"Level up! You are now level {self.level}!")
        print ("All stats increased by 2! Health and mana increased by 20! You feel refreshed!")

class Monster(Character):
    def __init__(self):
        super().__init__()

        self.name = colored('Monster', 'magenta', attrs=['bold',])
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
