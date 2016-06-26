from ps4a import *
import time
MyHand = {}
#
#
# Problem #6: Computer chooses a word
#
#
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
#
# Problem #8: Playing a game
#
#

def playGame4(wordList):
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
    global MyHand
    global HAND_SIZE
    KeepRun = True
    KeepRun2 = True
    getInp1 = ''
    getInp2 = ''
    hand = False
    while KeepRun == True:
        getInp1=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        if getInp1 == 'n':
            hand = dealHand(HAND_SIZE) #deals the hand to MyHand
            
            while KeepRun2:

                    getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                    #print
                    if getInp2 == 'u':
                        playHand(hand,wordList,HAND_SIZE)
                        KeepRun2 = False
                    elif getInp2 == 'c':
                        compPlayHand(hand,wordList,HAND_SIZE)
                        KeepRun2 = False
                    else: 
                        getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                        print
        
        elif getInp1 == 'r': #no hand has been dealt yet
                if hand: 

                    getInp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                    print
                    if getInp2 == 'u':
                        playHand(hand,wordList,HAND_SIZE)
                    elif getInp2 == 'c':
                        compPlayHand(hand,wordList,HAND_SIZE)
                    else: 
                        print "Invalid command."

                else: #previous hand has been played                    
                    print "You have not played a hand yet. Please play a new hand first!"              
        
        elif getInp1 == 'e':
                #MyHand={}    
                break
        else:
            print "Invalid command."

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    
