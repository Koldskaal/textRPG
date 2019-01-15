from .game_log import log

class Lifesteal:
    def __init__(self, player):
        self.type = 'post-hitting'
        self.player = player

    def activate(self, data):
        lifesteal = data['dmg']*0.5
        self.player.health += lifesteal
        log.add_to_log(f"You stole {lifesteal} health!", 'combat', 'positive')
