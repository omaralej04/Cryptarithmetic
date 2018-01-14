# Cryptarithmetic Solver -- Brute Force Method
import random

# Using the brute force iterations of a random assortment of left side (before) letter values.
def assignValues(letters):
    num = len(letters)
    possible = list(range(10))  # All values are [0,9]
    count = 0
    val = {"0" : 0}             # Creating a dicitonary for the letter/value combos
    for each in letters:
        pick = random.sample(possible,1)    # Each number can only be used once, so I sample then remove from the available pool.
        possible.remove(pick[0])
        val[each] = pick[0]
        count += 1
    return possible, val

codeText = "WHAT + WAS + THY == CAUSE"      # Puzzle Text

before = codeText.split(" == ")[0]          # String Play
after = codeText.split(" == ")[1]
beforeLetters = set("".join(before.split(" + ")))
afterLetters = set(after)

beforeWords = before.split(" + ")
afterLength = len(after)

# Flip words
wordAfter = after[::-1]                     # Set up the words so they are backwards so I can index in the typical direction.
wordsBefore = [""]*len(beforeWords)
for i, each in enumerate(beforeWords):
    wordsBefore[i] = each[::-1]
    zeros = afterLength - len(each)         # Add zeros to fill in empty places in higher places. "0" is in the dict as 0
    wordsBefore[i] += "0"*zeros

for iter in range(1000000):
    available, Vals = assignValues(beforeLetters)   # Random Start
    carry = 0                                       # No carry in first iteration (one's place)
    for i in range(afterLength):
        sum = carry
        for j in range(len(beforeWords)):           # Add and carry
            sum += Vals[wordsBefore[j][i]]
        new = sum % 10
        carry = sum // 10
        if wordAfter[i] in Vals:                    # If we should know this result since the 'letter' exists in the before text.
            if new != Vals[wordAfter[i]]:               # If we should know the value, check.
                break
        else:
            if new in available:                    # if it's a new 'letter', can we assign it to a unique number value?
                Vals[wordAfter[i]] = new
                available.remove(new)
                if i == afterLength - 1 and new != 0: # Have we reached it end?
                    print("We Did it!!!")
                    del Vals["0"]
                    print(Vals)
                    exit()
            else:
                break
