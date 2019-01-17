from termcolor import colored
from .game_log import log

class Character:
    def __init__(self):
        self.isPlayer = False

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

        self.buffs = []
        self.debuffs = []



    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        if self.__health-amount > 0:
            if self.isPlayer:
                log.add_to_log(f"You took {self.__health-amount} damage", 'Combat', 'bad')
            else:
                log.add_to_log(f"{self.name} lost {self.__health-amount} hp", 'Combat')
        elif self.__health-amount < 0 and self.__health:
            if self.isPlayer:
                log.add_to_log(f"You recovered {-(self.__health-amount)} hp", 'Combat', 'positive')
            else:
                log.add_to_log(f"{self.name} recovered {-(self.__health-amount)} hp", 'Combat', 'positive')
        self.__health = amount
        if self.__health > self.max_health:
            self.__health = self.max_health
        for callback in self._observers:
            callback()

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, amount):
        self.__mana = amount
        if self.__mana > self.max_mana:
            self.__mana = self.max_mana
        for callback in self._observers:
            callback()

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, amount):
        self.__gold = amount
        for callback in self._observers:
            callback()

    def bind_stats(self, callback):
        self._observers.append(callback)

    def hit(self, target):
        self.mana += self.int
        dmg = int((1*self.str**2)/(target.armor+1*self.str))
        self.log_attack_target(target)
        target.health -= dmg
        if target.health <= 0:
            log.add_to_log(f"WOAH! {target.name.capitalize()} died!", 'Announcer', 'surprise')
            if self.health > self.max_health*0.8:
                log.add_to_log(f"What a blow out!", 'Announcer', 'surprise')
        return dmg

    def log_attack_target(self, target):
        log.add_to_log(f"{self.name} attacks {target.name}!", 'Combat')
