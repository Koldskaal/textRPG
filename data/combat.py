import time
from termcolor import colored
from random import choice,randint
import sys
import msvcrt

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

def health_bar(character):
    length = 10
    iteration = character.health
    total = character.max_health
    filledLength = int(length * iteration // total)
    percent = ("{}").format(100 * (iteration / float(total)))
    fill = HEALTH_BAR
    enemy_bar = character.name + ' | ' + colored(fill * filledLength + '-' * (length - filledLength), 'red') + f' | {iteration}/{total}'
    log.canvas.replace_line('room', enemy_bar, 20)

def ready_bar(iteration, total, line, color):
    length = 20
    if iteration > total:
        iteration = total
    # iteration = character.health
    # total = character.max_health
    filledLength = int(length * iteration // total)
    percent = ("{}").format(100 * (iteration / float(total)))
    fill = HEALTH_BAR
    _bar = colored(fill * filledLength + '-' * (length - filledLength), color)
    log.canvas.replace_line('room', _bar, line)


def use_spell(player, enemy, exit_room):
    data = {'player':player, 'enemy':enemy}
    activate(player, data, 'pre-spellcast')
    spell_menu = CombatSpellMenu(player)
    spell_menu.print_room()
    spell = None
    log.canvas.replace_line('room', "Press 'r' to skip.", 1, clear=True)
    health_bar(enemy)
    log.print_canvas()
    while not spell:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            spell = spell_menu.use_key(chr(key))

            log.canvas.replace_line('room', "Press 'r' to skip.", 1)
            health_bar(enemy)
            log.print_canvas()
            while msvcrt.kbhit():
                msvcrt.getch()

            if spell:
                if spell[1]:
                    data['spell_name'] = spell[0].name
                    activate(player, data, 'mid-spellcast')
                    spell = 'skip'
                else:
                    spell = spell[0]
                break

    exit_room.print_room()
    health_bar(enemy)
    if spell == 'skip':
        return
    spell.cast(enemy)

def fight(p, e, exit_room):
    next_hit_p = 0
    next_hit_e = 0
    int_turn = 0
    hit = 50
    data = {'enemy': e, 'player': p}
    health_bar(e)
    ready_bar(int_turn, hit, 1, 'blue')

    while True:
        def hitting(att, _def):
            a_name = att.name if att.name != p.name else 'You'
            d_name = _def.name if _def.name != p.name else 'You'

            att.mana += att.int

            # dmg = att.str + choice([randint(0,int(att.str*0.1)),-randint(0,int(att.str*0.1))]) - _def.armor
            dmg = int((1*att.str**2)/(_def.armor+1*att.str))
            dmg_col = colored(str(dmg), 'red', attrs=['bold'])
            log.add_to_log(f"{a_name} {'attack' if a_name == 'You' else 'attacks'} {d_name}!", 'Combat')

            _def.health -= dmg
            health_col = colored(str(_def.health), 'green', attrs=['bold'])
            max_health = colored(str(_def.max_health), 'green', attrs=['bold'])
            log.add_to_log(f"{d_name} took {dmg} damage.", 'Combat', 'bad' if _def.name == p.name else 'default')
            if _def.health <= 0:
                log.add_to_log(f"WOAH! That {d_name} looks to be in agony!", 'Announcer', 'surprise')
                if att.health > att.max_health*0.8:
                    log.add_to_log(f"What a blow out!", 'Announcer', 'surprise')
            return dmg
            # log.add_to_log("-"*40, 'Combat')
        health_bar(e)
        int_turn += p.int//2
        ready_bar(int_turn, hit, 1, 'blue')
        next_hit_p += p.agi
        ready_bar(next_hit_p, hit, 2, 'green')
        next_hit_e += e.agi
        for debuff in p.debuffs:
            debuff.proc_debuff()
        for debuff in e.debuffs:
            debuff.proc_debuff()

        if next_hit_p > hit:
            data['dmg'] = hitting(p, e)
            activate(p, data, 'post-hitting-player')
            next_hit_p -= hit
            if e.health <= 0:
                winner = p
                break

        if next_hit_e > hit:
            data['dmg'] = hitting(e, p)
            activate(p, data, 'post-hitting-enemy')
            next_hit_e -= hit
            if p.health <= 0:
                winner = e
                break

        if int_turn > hit:
            use_spell(p, e, exit_room)
            int_turn -= hit
            if e.health <= 0:
                winner = p
                break

        log.print_canvas()
        time.sleep(0.2)

    log.add_to_log(f"{winner.name} wins!", 'Announcer', 'surprise')
    return winner

def encounter(p, e, exit_room):
    log.print_canvas(clear=True)
    e.bind_stats(lambda: health_bar(e))
    winner = fight(p, e, exit_room)
    if winner == p:
        p.gain_exp(e.exp)
        p.gold += e.gold
        gained_items = grab_loot.grab_loot_low_level(low_level.list_of_weapons, low_level.list_of_helmets, low_level.list_of_armor, low_level.list_of_rest, 2, 5)
        log.add_to_log(f'You picked up: {gained_items}!', 'Info', 'useful')

        p.items += gained_items
        return "enemy_killed"
    else:
        log.add_to_log("You lose gtfo", 'Announcer', 'surprise')
        sys.exit()
