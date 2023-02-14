# enter a series of 5 words for a madlib, using a while loop to fill list

words = []
i = 0

print("Welcome to Madlibs! You'll be making two sentences :)\n")

while i < 5:
    if i == 1 or i == 3:
        words.append(input("Enter noun: "))
    else:
        words.append(input("Enter adjective: "))
    
    i += 1

print("")
print(f"The {words[0]} part of {words[1]} is when you're feeling {words[2]}.")

print(f"I ate {words[3]} for breakfast and it tasted {words[4]}.")