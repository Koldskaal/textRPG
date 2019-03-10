from .game_log import log
from .spells import ImaginationSpell
from random import choice, random, randint
from blinker import signal

talent_list = []

class BaseTalent:
    player_melee_before = signal('player_melee_before')
    player_melee_after = signal('player_melee_after')

    enemy_melee_before = signal('enemy_melee_before')
    enemy_melee_after = signal('enemy_melee_after')

    player_spell_before = signal('player_spell_before')
    player_spell_after = signal('player_spell_after')
    player_spell_during = signal('player_spell_during')

    enemy_spell_before = signal('enemy_spell_before')
    enemy_spell_after = signal('enemy_spell_after')

    def __init__(self):
        self.name = "Base Talent"
        self.descrition = "A base description."

class Lifesteal(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Super Mega Ultra lifesteal"
        self.descrition = "50% lifesteal. What is not to love?"

        self.player_melee_after.connect(self.activate)

    def activate(self, sender, **data):
        if self in data['player'].talents:
            for talent in data['player'].talents:
                if talent == self:
                    lifesteal = int(data['dmg']*0.5)
                    data['player'].health += lifesteal
                    log.attach_to_log(f"({self.name})", 'positive')

talent_list.append(Lifesteal())

class PowerOfImagination(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Power of Imagination"
        self.descrition = "Get a new random spell with a random effect every turn."
        self.spell_names = {
            'Hadouken!': 'You have probably never heard of this move before but it is a blue fireball.',
            'Kamehamehaaaaaaaaaaa!': 'This will look badass, I swear. I just hope he gives me enough time to pull it off.',
            'Avada Kedavra Minor': 'They are supposed to die to this but I am not too sure.',
            'The power of the force': 'They will be pushed a little.'
            }
        self.prev_spell = None

        self.player_spell_before.connect(self.activate)

    def generate_spell(self, player):
        name, descrition = choice(list(self.spell_names.items()))
        # descrition += "\nPress 'q' to reroll and shoot. If you have the balls."

        return ImaginationSpell(player, name, descrition)

    def activate(self, sender, **data):
        if self in data['player'].talents:
            if self.prev_spell:
                data['player'].spells.remove(self.prev_spell)
            self.prev_spell = self.generate_spell(data['player'])
            data['player'].spells.append(self.prev_spell)
            if data.get('spell_name', '') in self.spell_names.keys():
                self.prev_spell.cast(data['enemy'])

talent_list.append(PowerOfImagination())

class Reflect(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Reflect"
        self.descrition = "50% reflect. Refelct sorry..."

        self.enemy_melee_after.connect(self.activate)

    def activate(self, sender, **data):
        if self in data['player'].talents:
            refelct_dmg = int(data['dmg']*0.5)

            data['enemy'].health -= refelct_dmg
            log.add_to_log(f"{data['enemy'].name} lost {refelct_dmg} hp. ({self.name})", 'combat', 'recked')

talent_list.append(Reflect())

class HitBack(BaseTalent):
    def __init__(self):
        super().__init__()
        self.name = "Hit 'em back'"
        self.descrition = "Add 20% chance to get a free attack when hit."

        self.chance = 0.2

        self.enemy_melee_after.connect(self.activate)

    def activate(self, sender, **data):
        if self in data['player'].talents:
            chance = 0
            for talent in data['player'].talents:
                if talent == self:
                    chance += self.chance
            if random() < chance:
                dmg = int((1*data['player'].str**2)/(data['enemy'].armor+1*data['player'].str))
                log.add_to_log(f"You hit {data['enemy'].name} back for {dmg}!", 'combat', 'recked')
                data['enemy'].health -= dmg

talent_list.append(HitBack())

"""
Blood magic - uses hp instead of mana is set to 0
Epherial Armor - maximum hp is set to 1. Mana is lost before hp
Equilibrium - When you have auto attacked, your next spell does 10% more damage. When you've cast a spell, your next auto attack does 10% more damage
Elemental addict - Lifesteal applies to mana instead of hp
Physical manipulation - spell damage hits for + 1*str (on spell cast, not dot ticks lol OP)

"""
