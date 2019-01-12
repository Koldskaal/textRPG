class BasicSpell:
    def __init__(self, player):
        self.name = 'Basic Spell'
        self.mana_usage = 10
        self.damage = 10
        self.target = 'enemy'
        self.caster = player

    def cast(self, target):
        target.health -= self.damage
        self.caster.mana -= self.mana_usage

class BasicHeal(BasicSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic Heal'
        self.mana_usage = 10
        self.damage = -10
        self.target = 'player'

class Dot:
    def __init__(self):
        self.name = 'Basic Heal'
        self.mana_usage = 10
        self.damage = -10
        self.target = 'player'
