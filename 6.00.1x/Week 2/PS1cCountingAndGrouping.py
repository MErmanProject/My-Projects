def item_order(order) :
    from re import findall
    salad = 0
    hamburger = 0
    water = 0

    salad=len(findall('(?=salad)',order))      
    hamburger=len(findall('(?=hamburger)',order))
    water=len(findall('(?=water)',order))
    order = 'salad:' +str(salad)+ ' hamburger:' +str(hamburger)+ ' water:' +str(water)
   
    return order
