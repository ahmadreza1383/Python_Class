#///////////////////// check price food
    
    
foods = {'pizza':20000 , 'soosis' :10000 , 'kalbas' : 15000}

foods.items()
for food , money in foods.items():
    if money >= 15000:
        print(food)
