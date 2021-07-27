number = int(input("number: "))

def Integers():
    result = 0
    for i in range(1 , number+1 , 2):
        result = i + result


    print(result)


Integers()
