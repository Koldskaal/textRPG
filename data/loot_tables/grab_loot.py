from random import choice
from random import randint
#import low_level for testing

def grab_loot_low_level(list_of_equipment,list_of_rest,min_loot, max_loot):
    looted = []
    equipment = 0

    NID = randint(min_loot,max_loot)
    for drop in range(NID):
        chosen = choice([list_of_equipment, list_of_rest])
        if equipment < 2:
            if chosen == list_of_equipment:
                equipment += 1
                looted.append(choice(chosen))
            else:
                looted.append(choice(list_of_rest))
        else:
            looted.append(choice(list_of_rest))
    return looted
