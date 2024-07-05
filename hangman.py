# Printing a starting message to give users an understanding of which player guesses and which player selects the word and how many tries.
print('''
      Hello players, this is Hangman.

      Player 1, you will be asked to enter a word.

      Player 2, you will be asked to enter letters in order to guess the word. You will have 2 tries for every letter in the word Player 1 selects.

      Good luck!
      ''')

# Function to pick the word that Player 1 selects.
def get_word():
    return input("Player 1, enter a word: ").lower()

# Function to define the number of guesses Player 2 gets.
def number_of_guesses(word):
    return 2 * len(word)

# Stores the word selected by Player 1 as a list of characters.
player_1_word = list(get_word())

# Stores the number of guesses Player 2 has.
num_of_guesses = number_of_guesses(player_1_word)

# Prints the placeholder for the word and informs players about how many guesses they have.
the_word = ['x'] * len(player_1_word)
print("Word to guess:", ' '.join(the_word))
print("Number of allowed guesses:", num_of_guesses)

#create empty list for guess
guess = set()
remaining_guesses = num_of_guesses

#while they still have guesses and they havent guessed every letter
while remaining_guesses > 0 and 'x' in the_word:
    #tell the user how many guesses they have left
    print(f'you have {remaining_guesses} left, use them wisely')
    print('The word currently looks like this:', ' '.join(the_word))
    letter_guess = input("player 2, guess a letter: ").lower()
    #if the letter has been guessed before, ask them to guess again
    if letter_guess in guess:
        print("you guessed that already, try again!")
    #if the letter hasnt been guessed before
    else:
        #add the letter to the guess set
        guess.add(letter_guess)
        #if the letter is in the word, tell them and output the word with xs covering letters and the letter they guessed in the correct place.
        if letter_guess in player_1_word:
            print('you guessed a correct letter!')
            #you match the letter to the index of the word list:
            for index,char in enumerate(player_1_word):
                #if the character in player1's word is = the letter that player 2 guessed.
                if char == letter_guess:
                    #add the letter that player 2 guessed to the word placeholder
                    the_word[index] = letter_guess
        else:
            print('wrong letter, try again...')
    #decrementing the remaining guesses
    remaining_guesses = remaining_guesses - 1

print('no more guesses')
#if the word guessed in the end was correct, player 2 win message
if the_word == player_1_word:
    print('''
          
          well done player2, you win!!
          
          ''')
#if the word guessed in the end was incorrect, player 1 win message and display player1's word
else:
    print(f'''
          
          well done player1, you win!!
          the word was {''.join(player_1_word)}
          try again next time
          
          ''')
    
        
    
                
  


            

    





    






      
    

