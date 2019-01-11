from termcolor import colored
from . import game_log

class Character:
    def __init__(self):
        self.__health = self.__mana = 0
        self._observers = []
        self.name = ""
        self.max_health = self.health = 100
        self.max_mana = self.mana = 100
        self.gold = 4000
        self.armor = 5

        self.str = 10
        self.int = 10
        self.agi = 10

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        self.__health = amount
        for callback in self._observers:
            callback()

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, amount):
        self.__mana = self.__mana + amount
        for callback in self._observers:
            callback()

    def bind_stats(self, callback):
        self._observers.append(callback)

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
        super(Player, self).__init__()

        self.name = 'Player'
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
        game_log.log.add_to_log(f"You gained {amount} experience!", 'info', 'useful')
        if self.levelcap-self.exp <=0:

            game_log.log.add_to_log(f"Required experience until next level: 0", 'info', 'useful')
        else:
            game_log.log.add_to_log(f"Required experience until next level: {self.levelcap-self.exp}", 'info')
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
        game_log.log.add_to_log(f"Level up! You are now level {self.level}!", 'info', 'recked')
        game_log.log.add_to_log("All stats increased by 2! Health and mana increased by 20! You feel refreshed!", 'info', 'recked')

class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()

        self.name = 'Monster'
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
