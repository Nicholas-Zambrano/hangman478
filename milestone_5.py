import random

class Hangman():

    
    # here we pass the parameters word list and num lives
    def __init__(self,word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        # now going to initialise the attributes
        self.word = random.choice(word_list) # selecting a random word from the input word list passed as parameter
        #self.word_guessed = ["_" for x in self.word]  # initalising with "_" for each word
        self.word_guessed = self.initalise_word_guess(self.word)
        self.num_letters = self.count_unique(self.word)
        self.list_of_guesses = [] # list of guesses we tried, intially it's []
    # this creates a list of underscores for that word 
    def initalise_word_guess (self, word):
        result = ["_" for x in word]
        return result 

    def count_unique (self,word_list):
        unique_numbers = []
        count = 0

        for i in word_list:
            if i not in unique_numbers:
                count +=1
                unique_numbers.append(i)
        return count
    
    def check_guess(self,guess):
        guess = guess.lower()
        if(guess in self.word):
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):  # you could also use enumerate to keep track of index
                # iterating through the word, and check if that element = to the guess letter, if so replace it
                if(self.word[i] == guess):
                    self.word_guessed[i] = guess
            # once we replaced all the underscores with the guess, then we decrement the unique letters
            self.num_letters -= 1
            print(f"the number of unique letters: {self.num_letters}")
            print(f"number of lives: {self.num_lives}")
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while (True):
            guess = input("Guess a letter: ")
            if( not guess.isalpha()  or len(guess) != 1 ):
                print( "Invalid letter. Please, enter a single alphabetical character.")
            elif(guess in self.list_of_guesses):
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                # now append that valid guess to the list of guess
                (self.list_of_guesses).append(guess)
                print(self.list_of_guesses)
                break

def play_game(word_list):
    num_lives = 5
    game =Hangman(word_list, num_lives)
    while (True):
        if(game.num_lives == 0):
            print(f"You lost!")
            break

        # this is the win condition 
        elif(game.num_lives != 0 and (game.num_letters == 0)):
            print("Congrats you won !!")
            break
        else:
            game.ask_for_input()


# # this is checking our instance class 
word_list = ["grapes","strawberries","blueberries","banana","apple"]    

# for i in range(len(word_list)):
#     print (word_list[i])
# word = random.choice(word_list)
# # print(word)
# fst_game = Hangman(word_list=word_list)
# print(fst_game.word)
# print(fst_game.word_guessed)
# print(fst_game.num_letters)

# fst_game.ask_for_input()

play_game(word_list)