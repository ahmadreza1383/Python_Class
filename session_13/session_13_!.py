GetInput = int(input("Enter Number: "))
def Action(number):
    result = 1
    for i in range(1 , number+1 , 1):
        result = i * result
        print(result)
    
Action(GetInput)
