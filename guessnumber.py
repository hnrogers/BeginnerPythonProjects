# guessing game that uses a while loop to guess a random number 1 - 11

import random

answer = False
num = random.randint(1,11)

while answer != True:
    if int(input("Enter number (1 - 11): ")) == num:
        print("Correct! :)")
        answer = True
    else:
        print("Try again!")