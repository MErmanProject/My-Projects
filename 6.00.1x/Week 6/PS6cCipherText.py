class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass 
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    
 
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass
        wordcount = 0
        totalwords = 0
        shift = 0
        NewMsg = ""
        Msg = self.message_text
        #apply each shift and track the number of words counted
        for i in range(0,len(string.ascii_lowercase)):
           
            Msg=self.apply_shift(i+1)
            splitMsg=(Msg.split(' '))         
            wordcount = 0
            for x in range(0,len(splitMsg)): 
                myel=splitMsg[x]
                if is_word(self.valid_words,myel) == True:
                    wordcount+=1
            if wordcount > totalwords:
                totalwords = wordcount
                if i < 25:
                    shift = i   
                else: shift = 0
                NewMsg= " ".join(splitMsg)
                
        return (shift+1, NewMsg)  