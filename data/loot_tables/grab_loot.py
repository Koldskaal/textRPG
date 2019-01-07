from random import choice
from random import randint
#import low_level# for testing

def grab_loot_low_level(list_of_weapons, list_of_helmets, list_of_armour, list_of_rest, min_loot, max_loot):
    looted = []
    weapons = 0
    helmets = 0
    armour = 0

    NID = randint(min_loot,max_loot)
    for drop in range(NID):
        chosen = choice([list_of_weapons, list_of_helmets, list_of_armour, list_of_rest])
        if weapons < 2:
            if chosen == list_of_weapons:
                weapons += 1
                looted.append(choice(chosen))
            else:
                if helmets < 1:
                    if chosen == list_of_helmets:
                        helmets += 1
                        looted.append(choice(chosen))
                else:
                    if armour < 1:
                        if chosen == list_of_armour:
                            armour += 1
                            looted.append(choice(chosen))
                    else:
                        looted.append(choice(list_of_rest))
        else:
            if helmets < 1:
                if chosen == list_of_helmets:
                    helmets += 1
                    looted.append(choice(chosen))
            else:
                if armour < 1:
                    if chosen == list_of_armour:
                        armour += 1
                        looted.append(choice(chosen))
                else:
                    looted.append(choice(list_of_rest))

    return looted
