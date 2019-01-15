from .game_log import log
from .spells import ImaginationSpell
from random import choice, random, randint

class Lifesteal:
    def __init__(self):
        self.type = ['post-hitting-player']

    def activate(self, data):
        lifesteal = int(data['dmg']*0.5)
        data['player'].health += lifesteal
        log.add_to_log(f"You stole {lifesteal} health!", 'combat', 'positive')


class PowerOfImagination:
    def __init__(self):
        self.type = ['pre-spellcast', 'mid-spellcast']
        self.spell_names = {
            'Hadouken!': 'You have probably never heard of this move before but it is a blue fireball.',
            'Kamehamehaaaaaaaaaaa!': 'This will look badass, I swear. I just hope he gives me enough time to pull it off.',
            'Avada Kedavra Minor': 'They are supposed to die to this but I am not too sure.',
            'The power of the force': 'They will be pushed a little.'
            }
        self.prev_spell = None

    def generate_spell(self, player):
        name, descrition = choice(list(self.spell_names.items()))
        descrition += "\nPress 'q' to reroll and shoot. If you have the balls."

        return ImaginationSpell(player, name, descrition)

    def activate(self, data):
        if self.prev_spell:
            data['player'].spells.remove(self.prev_spell)
        self.prev_spell = self.generate_spell(data['player'])
        data['player'].spells.append(self.prev_spell)
        if data and data.get('spell_name', '') in self.spell_names.keys():
            self.prev_spell.cast(data['enemy'])

class Reflect:
    def __init__(self):
        self.type = ['post-hitting-enemy']

    def activate(self, data):
        refelct_dmg = int(data['dmg']*0.5)
        data['enemy'].health += refelct_dmg
        log.add_to_log(f"You reflected {refelct_dmg} damage!", 'combat', 'recked')

class HitBack:
    def __init__(self):
        self.type = ['post-hitting-enemy']

    def activate(self, data):
        if random() < 0.2:
            dmg = int((1*data['player'].str**2)/(data['enemy'].armor+1*data['player'].str))
            data['enemy'].health += dmg
            log.add_to_log(f"You hit {data['enemy'].name} back for {dmg}!", 'combat', 'recked')
