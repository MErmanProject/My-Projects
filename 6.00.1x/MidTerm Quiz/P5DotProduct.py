def dotProduct(listA, listB):  
    result = 0  
    count = 0  
    for num in listA:  
        result += listA[count] * listB[count]  
        count +=1  
    return result 

    