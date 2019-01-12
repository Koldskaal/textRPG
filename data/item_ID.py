"""
general rules:
H:0001-1000    : helmets
A:0001-1000    : armours
W:0001-0500     : weapons
W:0500-1000  : shields
C:0001-1000    : consumeables
"""
def equip_item(self, item):
    if armor != None:
        self.armor += armor
    if str != None:
        self.str += str
    if int != None:
        self.int += int
    if agi != None:
        self.agi += agi
    if hp != None:
        self.health += hp
    if mp != None:
        self.mana += mp

items = {
#weapons
'axe of blood': {'type': 'weapon', 'str': 100, 'agi': 100, 'int': 100, 'price': 100000},#'spell': 'Basic Spell'
"wooden sword": {'type': 'weapon', 'str': 2, 'price': 1},
"iron sword": {'type': 'weapon', 'str': 4, 'price': 3},
"steel sword": {'type': 'weapon', 'str': 6, 'price': 5},
"wodden dagger": {'type': 'weapon', 'str': 1, 'agi': 1, 'price': 1},
"iron dagger": {'type': 'weapon', 'str': 2, 'agi': 2, 'price': 3},
"steel dagger": {'type': 'weapon', 'str': 3, 'agi': 3, 'price': 5},
"make-shift flint spear": {'type': 'weapon', 'str': 2, 'hp': 20, 'price': 3},
"stone mace": {'type': 'weapon', 'str': 3, 'agi':-2, 'price': 3},
"stone warhammer": {'type': 'weapon', 'str': 7, 'agi':-4, 'price': 6},
"quarterstaff": {'type': 'weapon', 'str': 2, 'int': 2, 'price': 10},
#helmets
'wizard hat': {'type': 'helmet', 'armor': 0, 'int': 2, 'price': 10},
'tinfoil hat': {'type': 'helmet', 'armor': 0, 'price': 1},
"wooden bucket": {'type': 'helmet', 'armor': 1, 'price': 1},
"woooden simple helmet": {'type': 'helmet', 'armor': 2, 'price': 2},
"iron simple helmet": {'type': 'helmet', 'armor': 3, 'price': 3},
"steel simple helmet": {'type': 'helmet', 'armor': 4, 'price': 4},
"iron helmet": {'type': 'helmet', 'armor': 4, 'price': 4},
"steel helmet": {'type': 'helmet', 'armor': 5, 'price': 5},
#armors
'linen rags': {'type': 'armor', 'armor': 1, 'price': 3},
"iron breastplate": {'type': 'armor', 'armor': 7, 'price': 20},
"steel breastplate": {'type': 'armor', 'armor': 9, 'price': 30},
"iron chainmail": {'type': 'armor', 'armor': 4, 'price': 15},
"steel chainmail": {'type': 'armor', 'armor': 6, 'price': 25},
#rings
"gold ring": {'type': 'ring', 'armor': 1, 'price': 250},
"silver ring": {'type': 'ring', 'hp': 20, 'price': 250},
'emerald ring': {'type': 'ring', 'agi': 1, 'price': 250},
'ruby ring': {'type': 'ring', 'str': 1, 'price': 250},
'sapphire ring': {'type': 'ring', 'int': 1, 'price': 250},
#misc
"ruby": {'type': 'sellable', 'price': 100},
"worn-out bedroll": {'type': 'consumable', 'price': 50},
#potions
"health potion": {'type': 'potion', 'price': 100},
"mana potion": {'type': 'potion', 'price': 100},
}
