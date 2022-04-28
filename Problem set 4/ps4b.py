# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words('words.txt')
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    # Example:
    # >>> is_word(word_list, 'bat') returns
    # True
    # >>> is_word(word_list, 'asdf') returns
    # False
    # '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("../../../Downloads/bcfbf5fbdae3c9acacfa457c7ad5f46e_ps4/ps4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = '../../../Downloads/bcfbf5fbdae3c9acacfa457c7ad5f46e_ps4/ps4/words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words.copy()
        return copy_valid_words
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert (0 <= shift) and (shift < 26), 'not valid shift value'

        alphabet_lowers = string.ascii_lowercase
        alphabet_uppers = string.ascii_uppercase
        map_letters = {}
        #Loop over lower and uppercase characters, upper_or_lower becomes a string
        for upper_or_lower in (alphabet_lowers, alphabet_uppers):
            for letter in upper_or_lower:
                #if the index of letter + shift is greater than 26, get the difference between them to simulate starting at index 0; 'a' after 26
                if (upper_or_lower.index(letter) + shift) >= 26:
                    map_letters[letter] = upper_or_lower[abs((upper_or_lower.index(letter)+shift)-26)]
                #else simply map letter to the shifted character
                else:
                    map_letters[letter] = upper_or_lower[upper_or_lower.index(letter)+shift]
        return map_letters


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_dict = self.build_shift_dict(shift)
        shifted_text = ''
        punct = '!()-[]{};:\'\"\\,<>./?@#$%^&*_~ '

        for char in self.message_text:
            if char not in punct:
                new_char = shifted_dict[char]
                shifted_text += new_char
            else:
                new_char = char
                shifted_text += new_char

        return shifted_text

# ab = Message('hello there!')
# print(ab.apply_shift(1))
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        Message.__init__(self, text)
        self.shift = shift
        self.valid_words = load_words('words.txt')
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        copy_enc_dict = self.encryption_dict
        return copy_enc_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert 0 <= shift <= 26, 'not valid shift value'
        self.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)




class CiphertextMessage(PlaintextMessage):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.valid_words = load_words('words.txt')

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        message_list = Message.get_message_text(self)
        message_list2 = message_list.split(" ")
        counter = 0

        for shift in range(1,27):
            PlaintextMessage.change_shift(self, shift)
            for word in message_list2:
                print(word)









ab = CiphertextMessage('jelly sanitarian wallpapers watchwords')
ab.decrypt_message()
# if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    # #TODO: WRITE YOUR TEST CASES HERE
    #
    # #TODO: best shift value and unencrypted story
    #
    # pass #delete this line and replace with your code here
