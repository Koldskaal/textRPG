from .game_log import log


class BaseSpell:
    def __init__(self, player):
        self.name = 'Base Spell'
        self.caster = player
        self.mana_usage = 0
        self.damage = self.define_damage()
        self.heal = self.define_heal()
        self.duration = 1
        self.descrition = "Base for all spells. Does nothing."

    def define_damage(self):
        return 0

    def define_heal(self):
        return 0

    def cast(self, target):
        target.health -= self.damage
        self.caster.health += self.heal
        self.caster.mana -= self.mana_usage

    def level_up(self):
        self.damage = self.define_damage()
        self.heal = self.define_heal()

class BasicSpell(BaseSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic Spell'
        self.mana_usage = 401
        self.damage = self.define_damage()
        self.duration = 111
        self.update_descrition()

    def define_damage(self):
        return 10111 + self.caster.level * 10 - 10

    def update_descrition(self):
        self.description = f"A basic damaging spell. It does {self.damage} damage and costs {self.mana_usage} mana. Use with care."

class BasicHeal(BaseSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic Heal'
        self.mana_usage = 30
        self.description = f"A basic healing spell."

    def define_heal(self):
        return 10 + (self.caster.level * 4)

class BasicDoT(BasicSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic DoT'
        self.mana_usage = 40
        self.damage = 1 + self.caster.level * 1 - 1
        self.duration = 15
        self.description = "A basic damage over time spell! Doesn't stack."

    def cast(self, target):
        target.debuffs.append(self)
        self.afflicted = target
        self.turns_left = self.duration
        self.caster.mana -= self.mana_usage

    def proc_debuff(self):
        self.afflicted.health -= self.damage
        log.add_to_log(f"{self.afflicted.name} lost another {self.damage} to {self.name} ({self.turns_left} turns left)!", 'Combat')
        self.turns_left -= 1
        if self.turns_left == 0:
            log.add_to_log(f"{self.afflicted.name} lost another {self.damage} to {self.name}!", 'Combat')
            self.afflicted.debuffs.remove(self)

    def define_damage(self):
        return 1 + self.caster.level * 1 - 1
