from .game_log import log
from random import randint

spell_list = []

class BaseSpell:
    def __init__(self, player):
        self.name = 'Base Spell'
        self.caster = player
        self.mana_usage = 0
        self.damage = self.define_damage()
        self.heal = self.define_heal()
        self.duration = 1
        self.description = "Base for all spells. Does nothing."

        self.points = 3

        self.special_action = False

    def define_damage(self):
        return 0

    def define_heal(self):
        return 0

    def cast(self, target):
        log.add_to_log(f"You used {self.name} on {target.name}!", 'Combat', 'recked')

        target.health -= self.damage
        if self.damage != 0:
            if self.damage > 0:
                log.add_to_log(f"{target.name} lost {self.damage} hp ({self.name})", 'recked')
            elif self.damage < 0:
                log.add_to_log(f"{target.name} gained {self.damage} hp ({self.name})", 'Combat', 'positive')
        self.caster.health += self.heal
        if self.heal != 0:
            log.attach_to_log(f'({self.name})', 'positive')
        self.caster.mana -= self.mana_usage

    def level_up(self):
        self.damage = self.define_damage()
        self.heal = self.define_heal()

    def on_damage(self):
        pass


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

spell_list.append(BasicSpell)

class BasicHeal(BaseSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic Heal'
        self.mana_usage = 30
        self.description = f"A basic healing spell."

    def define_heal(self):
        return 10 + (self.caster.level * 4)

spell_list.append(BasicHeal)

class BasicDoT(BasicSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic DoT'
        self.mana_usage = 40
        self.damage = 1 + self.caster.level * 1 - 1
        self.duration = 15
        self.description = "A basic damage over time spell! Doesn't stack."

    def cast(self, target):
        if self not in target.debuffs:
            log.add_to_log(f"You used {self.name} on {target.name}!", 'Combat', 'recked')
            target.debuffs.append(self)
        self.afflicted = target
        self.turns_left = self.duration
        self.caster.mana -= self.mana_usage

    def proc_debuff(self):
        self.afflicted.health -= self.damage
        self.turns_left -= 1
        log.add_to_log(f"{self.afflicted.name} lost {self.damage} hp ({self.name})", 'Combat')
        if self.turns_left % 5 == 0:
            log.add_to_log(f"{self.turns_left} procs remaining!", 'Combat', 'recked')
        if self.turns_left == 0:
            self.afflicted.debuffs.remove(self)

    def define_damage(self):
        return 1 + self.caster.level * 1 - 1

spell_list.append(BasicDoT)

class ImaginationSpell(BaseSpell):
    def __init__(self, player, name, description):
        super().__init__(player)
        self.name = name
        self.mana_usage = 0
        self.description = description
        self.special_action = True

    def define_damage(self):
        return randint(-80+20*self.caster.level, 80+20*self.caster.level)

    def define_heal(self):
        return randint(-80+20*self.caster.level, 80+20*self.caster.level)
