#///////////////////// foods.items() = pizza and 20000

foods = {'pizza':20000 , 'soosis' :10000 , 'kalbas' : 15000}

foods.items()
for i , j in foods.items():
    print(j , i)
    
    
    
    
    
    
    
    #///////////////////// check to money
    
    
    foods = {'pizza':20000 , 'soosis' :10000 , 'kalbas' : 15000}

foods.items()
for food , money in foods.items():
    if money >= 15000:
        print(food)
