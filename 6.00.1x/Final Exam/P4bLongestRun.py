def longestRun(L):
    
    
    startpos = 0
    endpos = 0
    myList=[]
    numtimes = 0
    listindx = 0
    
    if len(L) == 1:
        return 1

    while numtimes < len(L)-1: # number of times its starting through
              
        if L[listindx+1] >= L[listindx]:
            if startpos == 0 and endpos == 0:
                startpos = listindx
                endpos = listindx+1
            else:
                endpos = listindx+1
        else:
            startpos=0
            endpos=0
        if len(myList) > 0:
            if (endpos-startpos) >= len(myList[0]):
                myList=[]
                myList.append(L[startpos:endpos+1])
        else:
            if (endpos-startpos) > 0:
                myList=[]
                myList.append(L[startpos:endpos+1])
        listindx += 1
        numtimes +=1
    if len(myList) == 0:
        return 1
    else:
        return len(myList[0])  
    