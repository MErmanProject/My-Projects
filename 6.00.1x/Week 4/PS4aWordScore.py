# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

#runOnce = False
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
KeepRun = True
getInp1 = ''
getInp2 = ''
MyHand = {}
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "C:\Users\MNasty\Documents\MITx\ProblemSet4\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    result = 0
    for letter in word: #gets each letter in the word
        result += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        return (result*len(word)) + 50
    else:
        return result*len(word)

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,             # print all on the same line                                                
    print        
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    UpdateDict = hand.copy()
    
    for letter in word:
      if UpdateDict[letter] > 1:
        UpdateDict[letter] -= 1
      else:
        del UpdateDict[letter]
        
    return UpdateDict            
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    match = ''
    count = 1
    Updatehand = hand.copy()
    if len(word) <= 1:
        return False
    for letter in word: 
        if letter in Updatehand and Updatehand[letter] > 0:
            Updatehand[letter] -= 1    
        else:
            return False
    
    for myStr in wordList:
        for letter in wordList[count-1]:
            match +=letter
        if word == match:
            return True
        match = ''
        
        if count  == len(wordList):
            return False
        else:
            count += 1
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    result = 0
    for letter in hand:
        result += hand[letter]
    return result
        

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a ".".
      

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0 # Keep track of the total score
    getword = ''
    CurrHand = hand.copy() 
    while calculateHandlen(CurrHand) > 0: # As long as there are still letters left in the hand:
        print "Current Hand: ", displayHand(CurrHand)
        getword=(raw_input('Enter word, or a "." to indicate that you are finished: ')) # Ask user for input
        if getword == '.': # If the input is a single period:
            break # End the game (break out of the loop)
        else: # Otherwise (the input is not a single period):
            if isValidWord(getword, hand, wordList) == False: # If the word is not valid:
                print "Invalid word, please try again." # Reject invalid word (print a message followed by a blank line)
                print
            else: # Otherwise (the word is valid):
                score += getWordScore(getword,n)                
                print "" + str(getword) + "" + " earned "  + str(getWordScore(getword,n)) + " points. Total: " + str(score)  # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                CurrHand=updateHand(CurrHand,getword)# Update the hand 
                print      
    if getword == '.':
        print "Goodbye! Total score: " + str(score) # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(CurrHand) == 0:
        print "Run out of letters. Total score:" + str(score)
    playGame(wordList)

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    bestscore = 0# Create a new variable to store the maximum score seen so far (initially 0)

    bestword = ''# Create a new variable to store the best word seen so far (initially None)  

    for word in wordList: # For each word in the wordList

        if isValidWord(word, hand, wordList) == True: # If you can construct the word from your hand
            
                if getWordScore(word,n) > bestscore: # Find out how much making that word is worth/# If the score for that word is higher than your best score
                    bestscore = getWordScore(word,n) # Update your best score, and best word accordingly
                    bestword = str(word)

        
    if bestword != '':
        return bestword # return the best word you found.
    else:
        return None

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0 # Keep track of the total score
    getword = ''
    CurrHand = hand.copy() 
    while calculateHandlen(CurrHand) > 0: # As long as there are still letters left in the hand:
        print "Current Hand: ",
        displayHand(CurrHand)

        getword = compChooseWord(CurrHand, wordList, n)  # Get computer word
        if getword == None: # no words available
            break # End the game (break out of the loop)
        else: # Otherwise (the input is not a single period):
                
                score += getWordScore(getword,n)
                print              
                print '"' + str(getword) + '"' + " earned "  + str(getWordScore(getword,n)) + " points. Total: " + str(score)  # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                CurrHand=updateHand(CurrHand,getword)# Update the hand 
                print
    print      
    print "Total Score: " + str(score) + " points."
    return

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    global KeepRun   
    global MyHand
    global HAND_SIZE
    global getInp1 
    global getInp2 
    KeepRun2 = True

    if getInp1 == 'e' and (getInp2 == 'u' or getInp2 == 'c' or getInp2 == ''): #This is the condition where the loop needs to be reset because if you rerun from environment it will always exit
        getInp1 = ''
        #getInp2 = ''
        #return 
    
    while KeepRun == True:

        if getInp1 == 'e':
            MyHand={}
            #KeepRun = False
            #getInp1 == ''
            break
        else:
         
            getInp1=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                
            if getInp1 == 'n':
                MyHand = dealHand(HAND_SIZE) #deals the hand to MyHand
                KeepRun2 = True
                while KeepRun2 == True:
                    getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                    #print
                    if getInp2 == 'u':
                        playHand(MyHand,wordList,HAND_SIZE)
                        KeepRun2 = False
                    elif getInp2 == 'c':
                        compPlayHand(MyHand,wordList,HAND_SIZE)
                        KeepRun2 = False        
                    else:
                        print "Invalid command."
                        #getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                
        
            elif getInp1 == 'r': #no hand has been dealt yet
                    KeepRun2 = True
                    if len(MyHand) > 0: 
                        while KeepRun2 == True:
                            getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                            print
                            if getInp2 == 'u':
                                playHand(MyHand,wordList,HAND_SIZE)
                                KeepRun2 = False
                            elif getInp2 == 'c':
                                compPlayHand(MyHand,wordList,HAND_SIZE)
                                KeepRun2 = False     
                            elif getInp1 == 'e' and (getInp2 == 'u' or getInp2 == 'c'): #This is the condition where the loop needs to be reset because if you rerun from environment it will always exit
                                MyHand={}
                                #getInp1 = ''
                                #getInp2 = ''
                                break   
                            else:
                                print "Invalid command."
    
                    else: #previous hand has been played                    
                        print "You have not played a hand yet. Please play a new hand first!"
                  
            elif getInp1 == 'e' and (getInp2 == 'u' or getInp2 == 'c' or getInp2 == ''): #This is the condition where the loop needs to be reset because if you rerun from environment it will always exit
                MyHand={}
                #getInp1 = ''
                #getInp2 = ''
                break
            else:
                print "Invalid command."        
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
