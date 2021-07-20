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
        
        
        
        
        
#/////////////////////  setdefault   در صورت وجود هیچ کاری نمیکنه و اگه وجود نداشت مقدار رو اضافه میکنه
        
        
foods = {'pizza':20000 , 'soosis' :10000 , 'kalbas' : 15000}

foods.setdefault('pasta' , 20000)

foods.items()
for food , money in foods.items():
    if money >= 15000:
        print(food)

        
        
        
#///////////////////// از کانت برای گرفتن تعداد کاراکتر استفاده میکنیم
v = {'a' : 0 ,'e' : 0 ,'i' : 0 ,'o' : 0 ,'u' : 0 }

sentence = input('inter sentence : ')
for i , j in v.items():
    j = sentence.count(i)
    print(i , j)
