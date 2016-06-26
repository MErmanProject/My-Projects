class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
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
        
        self.dict = {}
        count = 0
        letter = ""
        num = 0
        for i in range(0,len(string.ascii_lowercase)):
            count = i + shift
            if count > 25:
                count -= len(string.ascii_lowercase)
            letter=string.ascii_lowercase[count]
            self.dict.update({string.ascii_lowercase[i]:letter})
            num += 2
        
        count = 0
        num = 1

        for i in range(0,len(string.ascii_uppercase)):
            count = i + shift
            if count > 25:
                count -= len(string.ascii_uppercase)
            letter=string.ascii_uppercase[count]
            self.dict.update({string.ascii_uppercase[i]:letter})
            num += 2
        
        return self.dict #lowercase followed by uppercase---ex: 'a':'d', 'A':'D'
                 

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
        myDict = self.build_shift_dict(shift)
        myStr = ""
        for char in self.message_text:
            if char not in (string.ascii_lowercase or string.ascii_uppercase): #char is some other thing
                myStr += char
            elif char in string.ascii_lowercase: #char is lowercase letter, return shifted letter, even starting with 0
                myStr += myDict[char] #will return the shifted letter by using the normal letter as the key
            else:
                myStr += myDict[char]

        return myStr
        
        