# computer guesses number that you provide
# while loop with a match/case statement!

import random

answer = input("Enter number: ")
low = 1
high = 100
guess = ""

while guess.lower() != "c":
    n = random.randint(low, high)
    guess = input(f"Is {n} too high (h), too low (l), or correct (c)? ")
    
    match guess.lower():
        case "h":
            high = n - 1
        case "l":
            low = n + 1
        case "c":
            print("Yay!")
            break
        case _:
            print(f"Invalid input! ('h', 'l', 'c')")
    