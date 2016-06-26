def getSublists(L, n):
    myList = []
    if len(L) == 1: #base case
        myList.append(L)
    else:
        listindx=0
        for numtimes in range(0,len(L)-n+1): #get this number of sublists
            myList.append(L[listindx:(listindx+n)])    
            listindx +=1
            
    return myList 
   