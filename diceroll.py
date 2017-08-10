import random
import os

# added a random seed for extra entropy
foo = random.SystemRandom().randint(0,9999999999999)

# seed our random
random.seed(foo)

# ask questions about dice once
dice_type = int(input('How many sides does your dice have?'))
dice_qty = int(input('How many dice are you rolling?'))
dice_rolls = int(input('How many times are you rolling the dice?'))

# holds each printed dice list
dicelist = []

# loop condition
going = True

# rolls each die
while going:
    for rolls in range(0, dice_rolls):
        print('Roll ' + str(rolls) + ':')
        for dice in range(0, dice_qty):
            nexter = str(random.randint(0, int(dice_type)))
            dicelist.append(nexter)
        print(dicelist)
        dicelist.clear()
    going = int(input('1 to roll again, 0 to quit.'))

