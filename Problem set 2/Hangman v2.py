# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "../../../Downloads/ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for c in secret_word:
        if c in letters_guessed:
            pass
        else:
            return False
    return True





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    a = ''
    for c in secret_word:
        if c in letters_guessed:
            a += c
        else:
            a += '_ '
    return a




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    a = string.ascii_lowercase
    b = ''
    for c in a:
        if c not in letters_guessed:
            b += c
    return b
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    b = ''
    warning = 3
    vowels = 'aeioy'
    print('Welcome to the game of Hangman!\nI am thinking of a word that is', len(secret_word),
          'letters long')
    while True:
        if warning <= 0:
            print('too many wrong inputs. You lose 1 guess.')
            guesses -= 1
        if guesses <= 0:
            print('No more guesses left')
            print('The word was', secret_word)
            break
        print('----------------------------')
        print('You have', guesses, 'guesses left.\nAvailable letters: ', get_available_letters(b))
        user_input = input('Please guess a letter: ').lower()
        if user_input not in string.ascii_lowercase:
            warning -= 1
            print('Oops! That is not not a valid letter. You have', warning, 'warnings left')
            continue
        if user_input in b:
            warning -= 1
            print('This letter has already been guessed. You lose one warning')
            print(warning, 'warnings left')
            continue
        b += user_input
        if user_input in secret_word:
            print('Good guess!: ', get_guessed_word(secret_word, b))
        else:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, b))
            if user_input in vowels:
                guesses -= 2
                continue
            guesses -= 1
        if is_word_guessed(secret_word, b):
            print('Congratulations, you won!\n Your total score for this game is:', len(set(secret_word))*guesses)
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    a = 0
    if len(my_word) != len(other_word):
        return False
    for c in my_word:
        if c not in string.ascii_lowercase:
            if other_word[a] in my_word:
                return False
            a += 1
            continue
        if c not in other_word:
            return False
        else:
            if my_word[a] != other_word[a]:
                return False
        a += 1
    return True




def show_possible_matches(my_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace(' ', '')
    a = 0
    for s in wordlist:
        if match_with_gaps(my_word, s):
            print(s)
            a += 1
    if a == 0:
        print('There was no matching words')

show_possible_matches('a___e', wordlist)





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
