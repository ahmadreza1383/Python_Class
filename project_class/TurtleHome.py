import turtle

def home():
   
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        
        turtle.forward(90)
        turtle.right(90)
    turtle.end_fill()

    turtle.fillcolor('green')
    turtle.begin_fill()

    for i in range(3):
        turtle.forward(90)
        turtle.left(120)
    turtle.end_fill()


home()
turtle.done()