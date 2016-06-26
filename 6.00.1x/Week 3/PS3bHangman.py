def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    Check = '' #Creates and empty string to check against secretWord
    for i in secretWord[:]: #loops for each letter in the secretWord
         if lettersGuessed.count(i) > 0: #Checks to see if you have guessed this letter
            Check += i #adds that letter to the Check string
    if len(Check) == len(secretWord): #Must be the word since its the same length
        return True
    else: #strings are not the same length, word cannot be the same.
        return False 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Check = '' #Creates and empty string to check against secretWord
    for i in secretWord[:]: #loops for each letter in the secretWord
         if lettersGuessed.count(i) > 0: #Checks to see if you have guessed this letter
            Check += i #adds that letter to the Check string
         else:
            Check += "_ "
    return Check

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    Avail = string.ascii_lowercase
    Check = ""
    for i in Avail[:]:
        if i not in lettersGuessed:
            Check += i
    return Check

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    NumGuesses=8
    LettersGuessed=""
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long." 
    print "-------------"

    while NumGuesses > 0: #They Still Have Guesses Left

        print "You have " +str(NumGuesses) + " guesses left."
        print "Available letters: " + getAvailableLetters(LettersGuessed)
        Guess = GetLetter().lower()
        
        if Guess[:] in LettersGuessed[:]: #Guessed a duplicate letter
            print "Oops! You've already guessed that letter:" + getGuessedWord(secretWord, LettersGuessed)
            print "------------"
            
        elif Guess[:] in secretWord: #the letter is in the word
            LettersGuessed +=Guess
            if isWordGuessed(secretWord,LettersGuessed) == True: #Game is over, secret word has been guessed
                print "Good guess: " + secretWord
                print "------------"
                print "Congratulations, you won!"
                return
            else: #word has not been guessed yet
                print "Good guess: " + getGuessedWord(secretWord,LettersGuessed)
                print "------------" 
                                        
        else: #Guess is not in word
            LettersGuessed +=Guess
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, LettersGuessed)
            print "------------"
            NumGuesses -= 1 #loses a guess
               
    if NumGuesses == 0:
         print "Sorry, you ran out of guesses. The word was " + secretWord + "."

def GetLetter():
    Guess=raw_input("Please guess a letter: ")
    return  Guess

