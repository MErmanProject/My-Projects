import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    num=0
    for i in range(numTrials):
        mylist=[]
        b=['r','r','r','r','g','g','g','g']
        for a in range(3):
          ball=random.choice(b)
          b.remove(ball)
          mylist.append(ball)
        if ('r' in mylist and 'g' not in mylist) or ('g' in mylist and 'r' not in mylist):
            num+=1
    
    return float(num)/numTrials