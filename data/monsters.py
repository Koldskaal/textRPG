from .character import Character

"""
monster types: names up for debate
Giant:          High hp, low agi, high str.
Exoskeleton:    low hp, high armor, medium str, medium agi.
Warrior:        medium hp, medium armor, medium str, medium agi.
Mage:           low hp, low armor, medium agi, high int, focus spells.
    sub types:
Demon:          low hp, low armor, high str, high agi.
Colossus:       High hp, High armor, medium str, low agi.
Angel:          low hp, medium armor, medium int, has healing spells.
Barbarian:      medium hp, low armor, high str, medium agi.
Goblin:         low hp, low armor, low str, high agi.
Faery:          low hp, low armor, medium str, high agi, medium int, has spells.
"""
class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()

        self.name = 'Monster'
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'

        self.str = 3
        self.agi = 10

class Giant(Character):
    def __init__(self):
        super(Giant, self).__init__()

        self.name = "Giant"
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 1000
        self.armor = 5
        self.str = 50
        self.agi = 4
        self.int = 4
        self.gold = 1000

class Exoskeleton(Character):
    def __init__(self):
        super(Exoskeleton, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 50
        self.str = 15
        self.agi = 15
        self.int = 4
        self.gold = 1000

class Warrior(Character):
    def __init__(self):
        super(Warrior, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 250
        self.armor = 15
        self.str = 15
        self.agi = 15
        self.int = 15
        self.gold = 1000

class Mage(Character):
    def __init__(self):
        super(Mage, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 4
        self.agi = 15
        self.int = 50
        self.gold = 1000
        #subclasses with type spells

class Demon(Character):
    def __init__(self):
        super(Demon, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 50
        self.agi = 50
        self.int = 4
        self.gold = 1000

class Colossus(Character):
    def __init__(self):
        super(Colossus, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 1000
        self.armor = 50
        self.str = 15
        self.agi = 4
        self.int = 4
        self.gold = 1000

class Angel(Character):
    def __init__(self):
        super(Angel, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 15
        self.str = 4
        self.agi = 15
        self.int = 15
        self.gold = 1000
        #healing spells

class Barbarian(Character):
    def __init__(self):
        super(Barbarian, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 250
        self.armor = 5
        self.str = 50
        self.agi = 15
        self.int = 4
        self.gold = 1000

class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 4
        self.agi = 50
        self.int = 4
        self.gold = 1000

class Faery(Character):
    def __init__(self):
        super(Faery, self).__init__()

        self.name = ""
        self.Enemy = True
        self.exp = 10
        self.loot_table = 'table_x'
        self.health = 100
        self.armor = 5
        self.str = 15
        self.agi = 50
        self.int = 15
        self.gold = 1000
        #spells
