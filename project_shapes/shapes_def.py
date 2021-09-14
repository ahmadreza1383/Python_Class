import turtle
from setting import MySetting
from setting import Standard
from ResultShapes import ResultShapes


if 'fun_list_Random' not in Standard:
    print('motaghayeri be esm random vogod nadarad')
    exit()

fun_list_Random = Standard['fun_list_Random']

if fun_list_Random['Assumption'] == True:
    

    def shapes(color = 'blue' , width = 60 , length = 60 , Left = 45 , NumberLeft = 1 , rotations = 4):
 
        for j in range(fun_list_Random['Number_of_prints']):

            turtle.fillcolor(color)
            turtle.begin_fill()
            for i in range(rotations):
                for f in range(NumberLeft):
                    turtle.forward(length)
                    turtle.left(Left)
                    turtle.forward(width)
                    turtle.left(Left)
            turtle.end_fill()        


if fun_list_Random['Assumption'] == False:
    def shapes(color = 'blue' , width = 60 , length = 60 , Left = 45 , NumberLeft = 1 , rotations = 4):
            
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(rotations):
            for f in range(NumberLeft):
                turtle.forward(length)
                turtle.left(Left)
                turtle.forward(width)
                turtle.left(Left)
        turtle.end_fill()
    
try:


        
    from widget import *


    shapes(color , width , length , Left , NumberLeft , rotations)

except:
    print('ehtemala yeki az maghadir moshkel darad ')
    exit()




# def shapes_turtle():
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for i in range(rotations):
#         for f in range(NumberLeft):
#             turtle.forward(length)
#             turtle.left(Left)
#             turtle.forward(width)
#             turtle.left(Left)
#     turtle.end_fill()
