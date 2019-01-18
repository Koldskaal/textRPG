from termcolor import colored
import os


use_unicode = True

WALL_CHAR_UP_DOWN = colored('▒', 'yellow')
WALL_CHAR_LEFT_RIGHT = colored('▒', 'yellow')
PLAYER_CHAR = colored('■', 'white', attrs=['bold'])
MONSTER_CHAR = colored('Θ', 'green', attrs=['bold'])
DOOR_CHAR = colored('|', 'yellow', attrs=['bold'])
DOOR_CHAR_OPEN_NEXT = colored('▐', 'yellow', attrs=['bold'])
DOOR_CHAR_OPEN_PREV = colored('▌', 'yellow', attrs=['bold'])

SHOP_STAND = colored('▲', 'cyan', attrs=['bold'])

BORDER_UP_DOWN = '─'
BORDER_LEFT_RIGHT = '│'
BORDER_CORNER_UP_LEFT = '┌'
BORDER_CORNER_UP_RIGHT = '┐'
BORDER_CORNER_DOWN_LEFT = '└'
BORDER_CORNER_DOWN_RIGHT = '┘'
BORDER_INLINE = '═'
BORDER_INLINE_THIN = '─'

HEALTH_BAR = '■'
MANA_BAR = '■'


try:
    print(PLAYER_CHAR)
    if not use_unicode:
        raise UnicodeEncodeError('for switching', u'', 42, 43, 'to switch char set')
except UnicodeEncodeError:
    WALL_CHAR_UP_DOWN = colored('x', 'yellow')
    WALL_CHAR_LEFT_RIGHT = colored('x', 'yellow')
    PLAYER_CHAR = colored('P', 'white', attrs=['bold'])
    MONSTER_CHAR = colored('M', 'green', attrs=['bold'])
    SHOP_STAND = colored('S', 'cyan', attrs=['bold'])
    DOOR_CHAR = colored('|', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_NEXT = colored(']', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_PREV = colored('[', 'yellow', attrs=['bold'])

    BORDER_UP_DOWN = '-'
    BORDER_LEFT_RIGHT = '|'
    BORDER_CORNER_UP_LEFT = '+'
    BORDER_CORNER_UP_RIGHT = '+'
    BORDER_CORNER_DOWN_LEFT = '+'
    BORDER_CORNER_DOWN_RIGHT = '+'
    BORDER_INLINE = '-'
    BORDER_INLINE_THIN = '-'

    HEALTH_BAR = '|'
    MANA_BAR = '|'
