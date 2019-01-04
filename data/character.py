class Character:
    def __init__(self, health, mana, gold, armor=0):
        self.health = health
        self.mana = mana
        self.gold = gold
        self.armor = armor


class Player(Character):
    def __init__(self):
        super().__init__()
        # exps
