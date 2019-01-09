from termcolor import colored
import os

try:

    WALL_CHAR_UP_DOWN = colored('▒', 'yellow')
    WALL_CHAR_LEFT_RIGHT = colored('▒', 'yellow')
    PLAYER_CHAR = colored('■', 'white', attrs=['bold'])
    MONSTER_CHAR = colored('Θ', 'green', attrs=['bold'])
    DOOR_CHAR = colored('|', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_NEXT = colored('▐', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_PREV = colored('▌', 'yellow', attrs=['bold'])
    print(PLAYER_CHAR)
    SHOP_STAND = colored('▲', 'cyan', attrs=['bold'])
except UnicodeEncodeError:
    WALL_CHAR_UP_DOWN = colored('x', 'yellow')
    WALL_CHAR_LEFT_RIGHT = colored('x', 'yellow')
    PLAYER_CHAR = colored('P', 'white', attrs=['bold'])
    MONSTER_CHAR = colored('M', 'green', attrs=['bold'])
    SHOP_STAND = colored('S', 'cyan', attrs=['bold'])
    DOOR_CHAR = colored('|', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_NEXT = colored(']', 'yellow', attrs=['bold'])
    DOOR_CHAR_OPEN_PREV = colored('[', 'yellow', attrs=['bold'])
