import random

word_list = ["grapes","strawberries","blueberries","banana","apple"]
    
word = random.choice(word_list)
  
# storing the random word in a variable 'word'
guess = input("Enter a single letter: ")

# validate user input
if(len(guess) == 1 and guess.isalpha()):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    # print( word)
