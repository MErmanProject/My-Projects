import itertools
def dict_invert(d):
    #{v:k for k,v in d.item}
    lastval =0
    myval = 0
    count = 0
    list=[]
    dictcopy=d.copy() #make a copy so we can iterate over the copy
    d.clear()
    for k,v in dictcopy.iteritems(): #look through the keys
        if lastval !=v or v == 0:  
            for k1,v1 in dictcopy.iteritems():
                if v == 0:
                    list.append(k1)
                    break
                if v == v1 and v != lastval: #if first value equals the second value
                    myval=v
                    list.append(k1)
                    count +=1  
            if count > 1: #need to get list values
                list.sort()
                d[myval]=list #switches values with keys
                list=[]
                count = 0
            else:
                d[myval]=list
                list=[]
                count = 0 
            lastval=v
    return d