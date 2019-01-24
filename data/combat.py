import time
from termcolor import colored
from random import choice,randint, random
import sys
import msvcrt
from blinker import signal

try:
    from  .loot_tables import grab_loot,low_level
    from .game_log import log
    from .textures import *
    from .spell_menu import CombatSpellMenu
except ModuleNotFoundError:
    from  loot_tables import grab_loot,low_level

def activate(p, data, type):
    for talent in p.talents:
        if type in talent.type:
            talent.activate(data)


class Combat:
    player_melee_before = signal('player_melee_before')
    player_melee_after = signal('player_melee_after')

    enemy_melee_before = signal('enemy_melee_before')
    enemy_melee_after = signal('enemy_melee_after')

    player_spell_before = signal('player_spell_before')
    player_spell_after = signal('player_spell_after')
    player_spell_during = signal('player_spell_during')

    enemy_spell_before = signal('enemy_spell_before')
    enemy_spell_after = signal('enemy_spell_after')

    def __init__(self, player, enemy, exit_room):
        self.exit_room = exit_room
        self.data = {'enemy': enemy, 'player': player}

        self.data['enemy'].bind_stats(lambda: self.enemy_health_bar(self.data['enemy']))

        self.tick_rate = 0.2

        self.spell_menu = CombatSpellMenu(self.data['player'])

    @staticmethod
    def enemy_health_bar(character):
        length = 10
        iteration = character.health
        total = character.max_health
        filledLength = int(length * iteration // total)
        percent = ("{}").format(100 * (iteration / float(total)))
        fill = HEALTH_BAR
        enemy_bar = character.name + ' | ' + colored(fill * filledLength + '-' * (length - filledLength), 'red') + f' | {iteration}/{total}'
        log.canvas.replace_line('room', enemy_bar, 19)
        log.print_canvas()

    @staticmethod
    def ready_bar(iteration, total, line, color, string):
        length = 25
        if iteration > total:
            iteration = total
        # iteration = character.health
        # total = character.max_health
        filledLength = int(length * iteration // total)
        percent = ("{0:.1f}").format(100 * (iteration / total) if (iteration / total) != 1 else 100)
        if percent == '100.0': percent = "{0:.3g}".format(float(percent))
        fill = HEALTH_BAR
        _bar = colored(fill * filledLength + '-' * (length - filledLength), color)
        log.canvas.replace_line('room', _bar, line)
        log.print_canvas()

    def encounter(self):
        log.print_canvas(clear=True)

        winner = self.fight()
        if winner:
            if winner == self.data['player']:
                self.data['player'].gain_exp(self.data['enemy'].exp)
                self.data['player'].gold += self.data['enemy'].gold
                gained_items = grab_loot.grab_loot_low_level(low_level.list_of_weapons, low_level.list_of_helmets, low_level.list_of_armor, low_level.list_of_rest, 2, 5)
                log.add_to_log(f'You picked up: {gained_items}!', 'Info', 'useful')

                self.data['player'].items += gained_items
                return "enemy_killed"
            else:
                log.add_to_log("You lose gtfo", 'Announcer', 'surprise')
                sys.exit()
        return winner

    def fight(self):
        next_hit_p = 0
        next_hit_e = 0
        int_turn = 0
        hit = 100

        # self.enemy_health_bar(self.data['enemy'])


        while self.data['player'].health > 0 and self.data['enemy'].health > 0:
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())
                if chr(key) == 'f':
                    log.add_to_log(f"You try to flee!", 'Announcer', 'surprise')
                    if random() < .5:
                        time.sleep(0.5)
                        log.add_to_log(f"It worked. You managed to escape.", 'Announcer', 'surprise')
                        winner = None
                        break
                    else:
                        time.sleep(0.5)
                        log.add_to_log(f"It didn't work. {self.data['enemy'].name} gets a free hit.", 'Announcer', 'surprise')
                        self.enemy_melee_before.send(self, **self.data)
                        self.data['dmg'] = self.data['enemy'].hit(self.data['player'])
                        self.enemy_melee_after.send(self, **self.data)
                while msvcrt.kbhit():
                    msvcrt.getch()

            # self.enemy_health_bar(self.data['enemy'])
            int_turn += self.data['player'].int/3

            next_hit_p += self.data['player'].agi
            next_hit_e += self.data['enemy'].agi
            self.ready_bar(next_hit_p, hit, 2, 'green', 'attack')
            self.ready_bar(next_hit_e, hit, 20, 'green', 'attack')
            self.ready_bar(int_turn, hit, 1, 'blue', 'spell cast')
            for debuff in self.data['player'].debuffs:
                debuff.proc_debuff()
            for debuff in self.data['enemy'].debuffs:
                debuff.proc_debuff()

            if next_hit_p > hit:
                self.player_melee_before.send(self, **self.data)
                self.data['dmg'] = self.data['player'].hit(self.data['enemy'])
                self.player_melee_after.send(self, **self.data)
                next_hit_p -= hit

            if next_hit_e > hit:
                self.enemy_melee_before.send(self, **self.data)
                self.data['dmg'] = self.data['enemy'].hit(self.data['player'])
                self.enemy_melee_after.send(self, **self.data)
                next_hit_e -= hit


            if int_turn > hit:
                self.player_spell_before.send(self, **self.data)
                self.use_spell()
                self.player_spell_after.send(self, **self.data)
                int_turn -= hit


            log.print_canvas()
            time.sleep(self.tick_rate)
            if self.data['player'].health > 0:
                winner = self.data['player']
            else:
                winner = self.data['enemy']

        if winner:
            log.add_to_log(f"{winner.name} wins!", 'Announcer', 'surprise')
        return winner

    def use_spell(self):

        self.spell_menu.print_room()
        spell = None
        log.canvas.replace_line('room', "Press 'r' to skip.", 1, clear=True)
        # self.enemy_health_bar(self.data['enemy'])
        log.print_canvas()
        while not spell:
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())
                spell = self.spell_menu.use_key(chr(key))

                log.canvas.replace_line('room', "Press 'r' to skip.", 1)
                # self.enemy_health_bar(self.data['enemy'])
                log.print_canvas()
                while msvcrt.kbhit():
                    msvcrt.getch()

                if spell:
                    if spell[1]:
                        self.data['spell_name'] = spell[0].name
                        self.player_spell_during.send(self, **self.data)
                        spell = 'skip'
                    else:
                        spell = spell[0]
                    break

        self.exit_room.print_room()
        # self.enemy_health_bar(self.data['enemy'])
        if spell == 'skip':
            return
        spell.cast(self.data['enemy'])
