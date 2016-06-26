def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    return inter(d1,d2),diff(d1,d2)
    
def inter(d1,d2):
    
    intsect = {}
    for key in d1.keys():
        if d2.has_key(key):
            intsect[key] = f(d1[key], d2[key])
    return intsect
    
def diff(d1,d2):
    
    diff = {} 
    for key in d1.keys(): # Iterate over keys in first dict 
        if (not d2.has_key(key)):
            diff[key] = (d1[key])  
    
    for key in d2.keys(): # Iterate over keys in second dict to get keys missing
        if (not d1.has_key(key)):
            diff[key] = (d2[key])
    return diff
