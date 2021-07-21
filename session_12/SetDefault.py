#/////////////////////  setdefault   در صورت وجود هیچ کاری نمیکنه و اگه وجود نداشت مقدار رو اضافه میکنه
        
        
foods = {'pizza':20000 , 'soosis' :10000 , 'kalbas' : 15000}

foods.setdefault('pasta' , 20000)

foods.items()
for food , money in foods.items():
    if money >= 15000:
        print(food)
