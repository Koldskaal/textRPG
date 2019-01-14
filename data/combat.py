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



def health_bar(p, e):
    length = 10
    iteration = e.health
    total = e.max_health
    filledLength = int(length * iteration // total)
    percent = ("{}").format(100 * (iteration / float(total)))
    fill = HEALTH_BAR
    enemy_bar = e.name + ' | ' + colored(fill * filledLength + '-' * (length - filledLength), 'red') + f' | {iteration}/{total}'
    log.canvas.replace_line('room', enemy_bar, 20)
    log.print_canvas()

def use_spell(player, enemy, exit_room):
    spell_menu = CombatSpellMenu(player)
    spell_menu.print_room()
    spell = None
    while not spell:
        health_bar(player,enemy)
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            spell = spell_menu.use_key(chr(key))
            health_bar(player,enemy)
            # print(log.canvas.areas['room']['popup'])
            while msvcrt.kbhit():
                msvcrt.getch()

            if spell:
                break

    exit_room.print_room()
    health_bar(player,enemy)
    if player.mana < spell.mana_usage:
        log.add_to_log(f"Not enough mana for {spell.name}.", 'Combat', 'useful')
        return
    target = player if spell.target == 'player' else enemy
    spell.cast(target)
    log.add_to_log(f"You used {spell.name} on {target.name}!", 'Combat', 'recked')
    if spell.damage < 0:
        log.add_to_log(f"{target.name} healed for {abs(spell.damage)} hp.", 'Combat', 'positive')
    else:
        log.add_to_log(f"{target.name} took {spell.damage} damage.", 'Combat', 'recked')

def fight(p, e, exit_room):
    next_hit_p = 0
    next_hit_e = 0
    int_turn = 0
    hit = 50

    while True:

        def hitting(att, _def):
            a_name = att.name if att.name != p.name else 'You'
            d_name = _def.name if _def.name != p.name else 'You'

            att.mana += att.int

            dmg = att.str + choice([randint(0,int(att.str*0.1)),-randint(0,int(att.str*0.1))]) - _def.armor
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
            # log.add_to_log("-"*40, 'Combat')

        int_turn += p.int
        next_hit_p += p.agi
        next_hit_e += e.agi
        for debuff in p.debuffs:
            debuff.proc_debuff()
        for debuff in e.debuffs:
            debuff.proc_debuff()

        if next_hit_p > hit:
            hitting(p, e)
            health_bar(p,e)
            next_hit_p -= hit
            if e.health <= 0:
                winner = p
                break

        if next_hit_e > hit:
            hitting(e, p)
            health_bar(p,e)
            next_hit_e -= hit
            if p.health <= 0:
                winner = e
                break

        if int_turn > hit:
            use_spell(p, e, exit_room)
            health_bar(p,e)
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

if __name__ == '__main__':
    import character
    if sys.stdin.isatty():
        import colorama
        colorama.init(convert=True)
    p = character.Player()
    e = character.Monster()
    e.health = 100
    e2 = character.Monster()
    e2.health = 120
    e3 = character.Monster()
    e3.health = 150
    encounter(p,e)# for testing
    log.add_to_log(p.levelcap)
    encounter(p,e2)
    log.add_to_log(p.levelcap)
    encounter(p,e3)
    log.add_to_log(p.levelcap)
