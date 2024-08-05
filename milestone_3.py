import random

word_list = ["grapes","strawberries","blueberries","banana","apple"]
    
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess = guess.lower()
    if(guess in word):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    # the 'True' causes the while loop to run continuously
    while(True):
        guess = input("Guess a letter: ")
        if(len(guess)== 1 and guess.isalpha()):
            break
        print("Invalid letter. Please, enter a single alphabetical character.")    

    # calling the check_guess function and passing our input 'guess'
    # we call outside the loop, because the guess was valid 
    check_guess(guess)

ask_for_input()
