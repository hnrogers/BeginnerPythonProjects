# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

import re

def stringIncrementer(txt):
    
    if re.match("\d+$", txt):
        og = re.search("(\d+$)", txt)
        og_str = str(og.group())
        
        zeroes = re.split("[1-9]+", og_str, maxsplit=2)[0]
        incremented_number = int(re.split(zeroes, og_str, maxsplit=1)[1])
        
        incremented_number += 1
        zeroes += str(incremented_number)
        
        return re.sub(og_str, zeroes, txt)
    else:
        return txt

print(stringIncrementer("h0ello0035"))
print(stringIncrementer("0005"))
print("trans rights!")
print()
