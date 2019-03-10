from .game_log import log
from random import randint, random
import pygame
pygame.mixer.init()
spell_list = []

spell_hit_sound = pygame.mixer.Sound('data/sounds/DmgSpell1.ogg')

debuff_hit_sound = pygame.mixer.Sound('data/sounds/debuffspell.ogg')

heal_sound = pygame.mixer.Sound('data/sounds/pickup.ogg')

class BaseSpell:
    def __init__(self, player):
        self.name = 'Base Spell'
        self.caster = player
        self.mana_usage = 0
        self.damage = self.define_damage()
        self.heal = self.define_heal()
        self.duration = 1
        self.description = "Base for all spells. Does nothing."

        self.types = ['damage', 'heal', 'buff', 'debuff']

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
            spell_hit_sound.play()
            if self.damage > 0:
                log.add_to_log(f"{target.name} lost {self.damage} hp ({self.name})", 'Combat', 'bad')
            elif self.damage < 0:
                log.add_to_log(f"{target.name} gained {self.damage} hp ({self.name})", 'Combat', 'positive')
        self.caster.health += self.heal
        if self.heal != 0:
            heal_sound.play()
            if self.heal > 0:
                log.attach_to_log(f'({self.name})', 'positive')
            elif self.heal < 0:
                log.attach_to_log(f'({self.name})', 'recked')
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

        self.types = ['damage']

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

        self.types = ['heal']

    def define_heal(self):
        return 10 + (self.caster.level * 4)

spell_list.append(BasicHeal)

class BasicDoT(BasicSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Basic DoT'
        self.mana_usage = 40
        self.damage = self.caster.level * 1
        self.duration = 15
        self.description = "A basic damage over time spell! Doesn't stack."

        self.types = ['damage', 'debuff']

    def cast(self, target):
        if self not in target.debuffs:
            debuff_hit_sound.play()
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
            log.add_to_log(f"{self.turns_left} ticks remaining! ({self.name})", 'Combat', 'recked')
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

        self.types = ['damage', 'heal']

    def define_damage(self):
        return randint(-80+20*self.caster.level, 80+20*self.caster.level)

    def define_heal(self):
        return randint(-80+20*self.caster.level, 80+20*self.caster.level)

class Freeze(BaseSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Freeze'
        self.mana_usage = 40
        self.duration = 1
        self.description = "Freeze up the enemy. 25% chance of causing a status effect."

        self.types = ['damage', 'debuff']

    def define_damage(self):
        return self.caster.level * 10 + 25

    def cast(self, target):
        super().cast(target)
        if random() <= 0.25:
            if self not in target.debuffs:
                self.afflicted = target
                log.add_to_log(f"{self.afflicted.name} got frozen! ({self.name})", 'Combat', 'cyan')
                self.afflicted.debuffs.append(self)
            self.afflicted.temp_agi = self.afflicted.agi
            self.afflicted.agi = 0
            self.turns_left = self.duration * 15

    def proc_debuff(self):
        self.turns_left -= 1
        if self.turns_left == 0:
            log.add_to_log(f"{self.afflicted.name} is no longer frozen! ({self.name})", 'Combat', 'recked')
            self.afflicted.debuffs.remove(self)
            self.afflicted.agi = self.afflicted.temp_agi

spell_list.append(Freeze)

class DrainLife(BaseSpell):
    def __init__(self, player):
        super().__init__(player)
        self.name = 'Drain life'
        self.mana_usage = 60
        self.duration = 1
        self.description = "Drain the hp of the opponent. Damage and heal at the same time but the mana cost is a little expensive."

        self.types = ['damage', 'heal']

    def define_damage(self):
        return self.caster.level * 10 + 5

    def define_heal(self):
        return int((self.caster.level * 10 + 5)*0.6)

spell_list.append(DrainLife)
