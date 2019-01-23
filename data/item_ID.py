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
        player.armor += armor
    if str != None:
        player.str += str
    if int != None:
        player.int += int
    if agi != None:
        player.agi += agi
    if hp != None:
        player.health += hp
    if mp != None:
        player.mana += mp

items = {
#weapons
'axe of blood': {'type': 'weapon', 'ATT': 100, 'str': 100, 'agi': 100, 'int': 100, 'price': 100000},#'spell': 'Basic Spell'
"wooden sword": {'type': 'weapon', 'ATT': 2, 'str': 2, 'price': 1},
"iron sword": {'type': 'weapon', 'ATT': 4, 'str': 4, 'price': 3},
"steel sword": {'type': 'weapon', 'ATT': 6, 'str': 6, 'price': 5},
"wodden dagger": {'type': 'weapon', 'ATT': 1, 'str': 1, 'agi': 1, 'price': 1},
"iron dagger": {'type': 'weapon', 'ATT': 2, 'str': 2, 'agi': 2, 'price': 3},
"steel dagger": {'type': 'weapon', 'ATT': 3, 'str': 3, 'agi': 3, 'price': 5},
"make-shift flint spear": {'type': 'weapon', 'ATT': 3, 'str': 2, 'hp': 20, 'price': 3},
"stone mace": {'type': 'weapon', 'ATT': 5, 'str': 3, 'agi':-2, 'price': 3},
"stone warhammer": {'type': 'weapon', 'ATT': 8, 'str': 7, 'agi':-4, 'price': 6},
"quarterstaff": {'type': 'weapon', 'ATT': 3, 'str': 2, 'int': 2, 'price': 10},
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
"health potion": {'type': 'potion', 'price': 100, "description": "A pultrice of red liquid, that when consumed, restores 100 health"},
"mana potion": {'type': 'potion', 'price': 100, "description": "A pultrice of blue liquid, that when consumed restores 100 mana. Side effects include a blue tongue"},
}
