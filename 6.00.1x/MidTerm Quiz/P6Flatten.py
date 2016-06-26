def flatten(aList):  
    myList = []  
    for el in aList:  
        if isinstance(el, list) or isinstance(el, tuple):  
            myList.extend(flatten(el))  
        else:  
            myList.append(el)  
    return myList  
