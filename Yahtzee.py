##This program uses Python to simulate the game of Yahtzee.

#Yahtzee counts the number of tries it takes to roll 
#a group of dice till they all match the same number.

#This code consists of a function that simulates rolling a group 
#of dice and another function that keeps count of the tries.

import random


def roll_dice():
    number = random.randint(1, 7)
    return number

def keep_rolling():
    dice_one = roll_dice()
    dice_two = roll_dice()
    dice_three = roll_dice()
    dice_four = roll_dice()
    count = 1

    while(not(dice_one == dice_two) and not(dice_two == dice_three) and not(dice_three == dice_four)):
        dice_one = roll_dice()
        dice_two = roll_dice()
        dice_three = roll_dice()
        dice_four = roll_dice()
        
        count += 1

    return count

name = input("What is your name? ")
no_of_tries = keep_rolling()

print("Congratulations " + name + "! You got a Yahtzee in " + str(no_of_tries) + " tries.")
