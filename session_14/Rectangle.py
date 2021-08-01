width = int(input("please Inter Width: "))
length = int(input("please Inter Length: "))

import turtle

def Rectangle(width , length):
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    def Environment():
        return (width + length) * 2

    def Area():
        return width * length

    return Environment() , Area()


result = Rectangle(width , length)

print(f' Environment : {result[0]} and Area : {result[1]} ')

turtle.done()
