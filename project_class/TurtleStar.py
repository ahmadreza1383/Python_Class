# import for turtle
import turtle
import TurtleRandom
 

for i in range(20):

    TurtleRandom.random_f_star()

    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(5):

        turtle.forward(20)
        
        turtle.right(144)
    turtle.end_fill()

