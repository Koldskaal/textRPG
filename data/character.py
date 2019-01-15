from termcolor import colored
from . import game_log
from . import spells
from . import talent_menu
import msvcrt

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

        self.buffs = []
        self.debuffs = []

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
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

class Player(Character):
    def __init__(self):
        super(Player, self).__init__()

        self.name = 'Player'
        self.Player = True



        self.level = 1
        self.exp = 0

        self.str = 100
        self.int = 10
        self.agi = 10

        self.current_weapon = ""
        self.equipment = [] # id
        self.items = []
        self.levelcap = 5+3*self.level**2

        self.spells = [spells.BasicSpell(self), spells.BasicDoT(self), spells.BasicHeal(self)]
        self.talents = []



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
        if self.level % 2 == 0:
            self.choose_talent()
        self.exp = self.exp-self.levelcap
        self.levelcap = 5+4*self.level**2
        self.str += 2
        self.agi += 2
        self.int += 2
        self.max_health = self.health = 100 + self.level*20-20
        self.max_mana = self.mana = 100 + self.level*20-20
        game_log.log.add_to_log(f"Level up! You are now level {self.level}!", 'info', 'recked')
        game_log.log.add_to_log("All stats increased by 2! Health and mana increased by 20! You feel refreshed!", 'info', 'recked')
        for spell in self.spells:
            spell.level_up()

    def choose_talent(self):
        menu = talent_menu.TalentMenu()
        menu.print_room()
        while True:
            # game_log.log.print_canvas()
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())

                talent = menu.use_key(chr(key))

                if talent:
                    break
        self.talents.append(talent)

"""
monster types: names up for debate
Giant:          High hp, low agi, high str.
Exoskeleton:    low hp, high armor, medium str, medium agi.
Warrior:        medium hp, medium armor, medium str, medium agi.
Mage:           low hp, low armor, medium agi, high int, focus spells.
    sub types:
Demon:          low hp, low armor, high str, high agi.
Colossus:       High hp, High armor, medium str, low agi.
Angel:          low hp, medium armor, medium int, has healing spells.
Barbarian:      medium hp, low armor, high str, medium agi.
Goblin:         low hp, low armor, low str, high agi.
Faery:          low hp, low armor, medium str, high agi, medium int, has spells.
"""
class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()

        self.name = 'xXxSh4dowLordxXx'
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'

class Giant(Character):
    def __init__(self):
        super(Giant, self).__init__()

        self.name = "Giant"
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 1000
        self.armor = 5
        self.str = 50
        self.agi = 4
        self.int = 4
        self.gold = 1000

class Exoskeleton(Character):
    def __init__(self):
        super(Exoskeleton, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 50
        self.str = 15
        self.agi = 15
        self.int = 4
        self.gold = 1000

class Warrior(Character):
    def __init__(self):
        super(Warrior, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 250
        self.armor = 15
        self.str = 15
        self.agi = 15
        self.int = 15
        self.gold = 1000

class Mage(Character):
    def __init__(self):
        super(Mage, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 4
        self.agi = 15
        self.int = 50
        self.gold = 1000
        #subclasses with type spells

class Demon(Character):
    def __init__(self):
        super(Demon, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 50
        self.agi = 50
        self.int = 4
        self.gold = 1000

class Colossus(Character):
    def __init__(self):
        super(Colossus, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 1000
        self.armor = 50
        self.str = 15
        self.agi = 4
        self.int = 4
        self.gold = 1000

class Angel(Character):
    def __init__(self):
        super(Angel, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 15
        self.str = 4
        self.agi = 15
        self.int = 15
        self.gold = 1000
        #healing spells

class Barbarian(Character):
    def __init__(self):
        super(Barbarian, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 250
        self.armor = 5
        self.str = 50
        self.agi = 15
        self.int = 4
        self.gold = 1000

class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 4
        self.agi = 50
        self.int = 4
        self.gold = 1000

class Faery(Character):
    def __init__(self):
        super(Faery, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 15
        self.agi = 50
        self.int = 15
        self.gold = 1000
        #spells
