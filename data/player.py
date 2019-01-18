import msvcrt
from termcolor import colored
from .character import Character
from .game_log import log
from . import spells
from . import talent_menu

class Player(Character):
    def __init__(self):
        super(Player, self).__init__()

        self.name = 'Player'
        self.isPlayer = True

        self.level = 1
        self.exp = 0
        self.points = 7

        self.str = 150
        self.int = 10
        self.agi = 150

        self.current_weapon = ""
        self.equipment =[] # id
        self.items = []
        self.levelcap = 5+3*self.level**2

        self.spells = [spells.BasicDoT(self)]
        self.talents = []

        self.helmet = ''
        self.body = ''
        self.ring = ''
        self.amulet = ''
        self.weapon = ''



    def gain_exp(self, amount):
        self.exp += amount
        log.add_to_log(f"You gained {amount} experience!", 'info', 'useful')
        if self.levelcap-self.exp <=0:

            log.add_to_log(f"Required experience until next level: 0", 'info', 'useful')
        else:
            log.add_to_log(f"Required experience until next level: {self.levelcap-self.exp}", 'info')
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
        self.points += 3
        self.max_health = self.health = 100 + self.level*20-20
        self.max_mana = self.mana = 100 + self.level*20-20
        log.add_to_log(f"Level up! You are now level {self.level}!", 'info', 'recked')
        log.add_to_log("All stats increased by 2! Health and mana increased by 20! You feel refreshed!", 'info', 'recked')
        for spell in self.spells:
            spell.level_up()

    def choose_talent(self):
        menu = talent_menu.TalentMenu()
        menu.print_room()
        while True:
            # log.print_canvas()
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())

                talent = menu.use_key(chr(key))

                if talent:
                    break
        self.talents.append(talent)

    def log_attack_target(self, target):
        log.add_to_log(f"You attack {target.name}!", 'Combat', 'yellow')
