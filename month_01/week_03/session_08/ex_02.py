# random number buyu duriin utga 

import random

roll_dice = random.randint(1, 6)
print(roll_dice)


is_heads = random.choice([True, False])
print("You flipped heads: " + str(is_heads))

# 4 shirheg hoolnii tsugluulga list uusgeed tuuniigee randomoor hevleh 

hool_list = ['shultui hool', 'tsuiwan', 'guriltai shul', 'chanasan mah']
is_hool_list = random.choice(hool_list)
print("Your food is: " + is_hool_list)