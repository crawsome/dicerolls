import random
import time
from statistics import mean


class DiceRoller:
    # added a random seed for extra entropy
    ourseed = random.SystemRandom().randint(0, 9999999999999)
    ourseed2 = random.SystemRandom().randint(0, 9999999999998)

    # seed our random
    random.seed(999999999999999999999 - ourseed + ourseed2)

    # dice globals
    dice_type = 0
    dice_qty = 0
    dice_rolls = 0

    # mode global
    mode = ' '

    # loop condition
    going = True

    # tries on average until 5 same numbers
    count = 0

    # computing the average

    # holds each printed dice list
    dicelist = []

    # list for holding rollcount
    rolllist = []

    # list for holding the times
    timelist = []

    # title presentation
    title = '  _____  _             _____ _        _       ' \
            '\n |  __ \(_)           / ____| |      | |       ' \
            '\n | |  | |_  ___ ___  | (___ | |_ __ _| |_ ___  ' \
            '\n | |  | | |/ __| _ \  \___ \| __/ _` | __/ __| ' \
            '\n | |__| | | |_( |__/  ____) | || (_| | |_\__ \\' \
            '\n |_____/|_|\___\___| |_____/ \__\__,_|\__|___/'

    diceimage = '\n\t\t\t   _______' \
                '\n\t\t\t  /\ o o o\ ' \
                '\n\t\t\t /o \ o o o\_______' \
                '\n\t\t\t<    >------>   o /|' \
                '\n\t\t\t \ o/  o   /_____/o|' \
                '\n\t\t\t  \/______/     |oo|' \
                '\n\t\t\t        |   o   |o/' \
                '\n\t\t\t        |_______|/' \
                '\n\t\t\t'

    #supports rolls up to 9 right now
    dice = ['---------\n|       |\n|   o   |\n|       |\n---------',
            '---------\n|o      |\n|       |\n|      o|\n---------',
            '---------\n|o      |\n|   o   |\n|      o|\n---------',
            '---------\n|o     o|\n|       |\n|o     o|\n---------',
            '---------\n|o     o|\n|   o   |\n|o     o|\n---------',
            '---------\n|o     o|\n|o     o|\n|o     o|\n---------',
            '---------\n|o     o|\n|o  o  o|\n|o     o|\n---------',
            '---------\n|o  o  o|\n|o     o|\n|o  o  o|\n---------',
            '---------\n|o  o  o|\n|o  o  o|\n|o  o  o|\n---------',
            '---------\n|o  o  o|\n|o o o o|\n|o  o  o|\n---------',
            '---------\n|o o o o|\n|o  o  o|\n|o o o o|\n---------',
            '---------\n|o o o o|\n|o o o o|\n|o o o o|\n---------',
            '---------\n|o o o o|\n|o ooo o|\n|o o o o|\n---------',
            '---------\n|o ooo o|\n|o o o o|\n|o ooo o|\n---------',
            '---------\n|o ooo o|\n|o ooo o|\n|o ooo o|\n---------']

    def printdice(self, diceint):
        print(self.dice[diceint])

    def askdice(self):
        self.dice_type = int(input('How many sides does your dice have?'))
        self.dice_qty = int(input('How many dice are you rolling?'))
        self.dice_rolls = int(input('How many times are you rolling the dice?'))

    def askmode(self):
        print('Mode A: Game Dice Rolling')
        print('Mode B: Continuous Roll counting and Yhatzee time measurement')
        print('Mode C: TBA')
        mode = input('Which Mode do you want to use?')

        self.askdice()

        if mode == 'A' or mode == 'a':
            self.regular_roll()
        elif mode == 'B' or mode == 'b':
            self.yahtzee_roll()
        elif mode == 'C' or mode == 'c':
            pass

    def yahtzee_roll(self):
        # rolls each die
        while self.going:
            t0 = time.time()
            for rolls in range(0, self.dice_rolls):
                self.count += 1
                # print('Roll ' + str(rolls + 1) + ':')
                for dice in range(0, self.dice_qty):
                    nextroll = random.randint(0, int(self.dice_type))
                    self.dicelist.append(nextroll)
                print(self.dicelist)
                # if all entries are the same
                # if len(set(dicelist)) == 1 (and len(dicelist) >= 5):
                if len(set(self.dicelist)) == 1:
                    t1 = time.time()
                    print('YAHTZEE!')
                    self.rolllist.append(self.count)
                    self.timelist.append(t1 - t0)
                    print(self.count, 'attempts')
                    print('{0:.2f}'.format(t1 - t0), 'time')
                    print('The average attempts for this session: ', '{0:.2f}'.format(mean(self.rolllist)))
                    print('The average time taken for this session: ', '{0:.2f}'.format(mean(self.timelist)))
                    self.count = 0
                    break
                self.dicelist.clear()
            self.going = int(input('1 to roll again, 0 to quit.'))

    def regular_roll(self):
        while self.going:
            for rolls in range(0, self.dice_rolls):
                self.count += 1
                # print('Roll ' + str(rolls + 1) + ':')
                for dice in range(0, self.dice_qty):
                    nextroll = random.randint(0, int(self.dice_type))
                    self.dicelist.append(nextroll)
                for die in self.dicelist:
                    self.printdice(die-1)
                # if all entries are the same
                # if len(set(dicelist)) == 1 (and len(dicelist) >= 5):
                self.dicelist.clear()
            self.going = int(input('1 to roll again, 0 to quit.'))

    def titlescreen(self):
        print(self.title, self.diceimage)


# main procedure

# create our dice roller object
our_roller = DiceRoller()

# display title screen
our_roller.titlescreen()

# ask info about mode
our_roller.askmode()
