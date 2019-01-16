from .game_log import log
from .spells import ImaginationSpell
from random import choice, random, randint

talent_list = []

class BaseTalent:
    def __init__(self):
        self.name = "Base Talent"
        self.descrition = "A base description."

class Lifesteal(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Super Mega Ultra lifesteal"
        self.descrition = "50% lifesteal. What is not to love?"
        self.type = ['post-hitting-player']

    def activate(self, data):
        lifesteal = int(data['dmg']*0.5)
        data['player'].health += lifesteal
        log.attach_to_log(f"({self.name})", 'positive')

talent_list.append(Lifesteal())

class PowerOfImagination(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Power of Imagination"
        self.descrition = "Get a new random spell with a random effect every turn."
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

talent_list.append(PowerOfImagination())

class Reflect(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Reflect"
        self.descrition = "50% reflect. Refelct sorry..."
        self.type = ['post-hitting-enemy']

    def activate(self, data):
        refelct_dmg = int(data['dmg']*0.5)
        log.add_to_log(f"You reflected {refelct_dmg} damage!", 'combat', 'recked')
        data['enemy'].health -= refelct_dmg
        log.attach_to_log(f"({self.name})")

talent_list.append(Reflect())

class HitBack(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Hit 'em back'"
        self.descrition = "20% chance to get a free attack when hit."
        self.type = ['post-hitting-enemy']

    def activate(self, data):
        if random() < 0.2:
            dmg = int((1*data['player'].str**2)/(data['enemy'].armor+1*data['player'].str))
            log.add_to_log(f"You hit {data['enemy'].name} back for {dmg}!", 'combat', 'recked')
            data['enemy'].health -= dmg

talent_list.append(HitBack())
