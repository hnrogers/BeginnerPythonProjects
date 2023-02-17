import random
import re
from WordGuessWords import words

def get_valid_word(words):
    
    current_word = random.choice(words)

    while re.search("[-, ]", current_word):
        current_word = random.choice(words)
        
    return current_word

def hangman(word):
    underscore_format = ["_"] * (len(valid_word))
    previous_guesses = []
    turns_remaining = 6
    
    while turns_remaining > 0 and "_" in underscore_format:
        print("")
        print(*underscore_format, sep=" ")
        print(*previous_guesses, sep=", ")
        print("Wrong gusses: " + str(turns_remaining) + "/6")
        
        user_guess = input("Guess a letter: ")
        
        if user_guess[0] in previous_guesses or not user_guess:
            print("Invalid selection!")
            
        else:
            previous_guesses.append(user_guess[0])
            
            if previous_guesses[-1] not in word:
                turns_remaining -= 1
            
            else:
                i = 0
                while i < len(underscore_format):
                    
                    if word[i] == user_guess[0]:
                        underscore_format[i] = user_guess[0]
                    
                    i += 1
    
    if "_" not in underscore_format:
        print("\nYou win!")
    else:
        print("\nYou lose!")
                            
valid_word = get_valid_word(words)
hangman(valid_word)
print(valid_word)