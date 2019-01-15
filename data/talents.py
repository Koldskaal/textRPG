from .game_log import log
from .spells import ImaginationSpell
from random import choice

class Lifesteal:
    def __init__(self, player):
        self.type = 'post-hitting'
        self.player = player

    def activate(self, data):
        lifesteal = data['dmg']*0.5
        self.player.health += lifesteal
        log.add_to_log(f"You stole {lifesteal} health!", 'combat', 'positive')


class PowerOfImagination:
    def __init__(self, player):
        self.type = 'pre-spell'
        self.player = player

        self.prev_spell = None

    def generate_spell(self):
        spell_names = {
            'Hadouken!': 'You have probably never heard of this move before but it is a blue fireball.',
            'Kamehamehaaaaaaaaaaa!': 'This will look badass, I swear. I just hope he gives me enough time to pull it off.',
            'Avada Kedavra Minor': 'They are supposed to die to this but I am not too sure.',
            'The power of the force': 'They will be pushed a little.'
            }

        name, descrition = choice(list(spell_names.items()))
        return ImaginationSpell(self.player, name, descrition)

    def activate(self, data):
        if self.prev_spell:
            self.player.spells.remove(self.prev_spell)
        self.prev_spell = self.generate_spell()
        self.player.spells.append(self.prev_spell)
