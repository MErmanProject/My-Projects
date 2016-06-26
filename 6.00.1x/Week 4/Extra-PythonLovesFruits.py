import string

def nfruits(Dict, MyStr):
    '''Assumes Dict is non-empty dictionary containing type of fruit and its quantity(length < 10)
    MyStr is a pattern of the fruits eaten on the way in the form of a string.
    '''
    
    if len(Dict) >= 10: #Dict is too long
        print "Please limit the Dictionary length to under 10 fruits!"
        return
    else:
        Count = 0 
        for letter in MyStr: #gets each letetr in MyStr
            Count += 1
            Dict[letter] -= 1 #lowers the number of that type of fruit by one
            if Count != len(MyStr):
                BuyFruits(letter, Dict)
        
    return MaxFruit(Dict)  #calls function MaxFruit to get maximum number of fruits   
            
            

def BuyFruits(FruitEaten, Dict): #runs each time he consumes a fruit so 
          
          for key in Dict:
              if key != FruitEaten: #the letter does not equal the type of fruit eaten
                Dict[key] += 1 #adds one to the type of fruit
        
def MaxFruit(Dict): #returns the max number of fruits
        Count = 0
        for key in Dict:
            if Dict[key] > Count:
                Count=Dict[key]
              
        return Count   