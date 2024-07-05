import random

class Word:
    def __init__(self):
        self.__word = input("Please enter a word: ")
        self.__protector = print('x' * 100)
        
    def get_word(self):
        return self.__word

    
class Computer_word:
    def __init__(self):
        self.__computer_words = ['hello', 'car', 'dog', 'cat', 'hat']
    def get_computer_word(self):
        return random.choice(self.__computer_words)

    
class Game:
    def __init__(self, word):
        self.__character = []
        self.__guessed_characters = set()
        self.__word = list(word)
        self.__remaining_guesses = len(word) * 2
        self.__covered_word = ['x'] * len(word)

    def input_character(self):
        self.__character = input('Please enter a character: ')

    def play_human(self):
        while self.__remaining_guesses > 0 and 'x' in self.__covered_word:
            self.input_character()
            if self.__character in self.__guessed_characters:
                print('You have guessed this, try again')
                self.__remaining_guesses -= 1
            elif self.__character in self.__word:
                self.__guessed_characters.add(self.__character)
                for index, char in enumerate(self.__word):
                    if char == self.__character:
                        self.__covered_word[index] = self.__character
                print("You guessed correctly")
            else:
                self.__guessed_characters.add(self.__character)
                self.__remaining_guesses -= 1 
            print(f'\nYou have {self.__remaining_guesses} guesses left\nThe word currently looks like this: {self.__covered_word}\n')
        if self.__word == self.__covered_word:
            print("Player 2, you win!")
        else:
            print("Player 1, you win!")

class Computer_Game(Game):
    def __init__(self, computer_word):
        super().__init__(computer_word)

    def play_computer(self):
        super().play_human()  

try:
    game_choice = int(input("Enter 1 to play against a friend or enter 2 to play against the computer: "))
    if game_choice == 1:
        word1 = Word()
        game = Game(word1.get_word())
        game.play_human()
    elif game_choice == 2:
        word2 = Computer_word()
        game = Computer_Game(word2.get_computer_word())
        game.play_computer()
    else:
        print("The value you have entered is not valid, i.e., not a 1 or 2. Try again!")
except ValueError:
    print('The value you entered is not a number. Try again!')



















