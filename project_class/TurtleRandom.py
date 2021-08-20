import turtle

from random import randint



def random_f():

    turtle.bgcolor('black')
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(randint(-200,0),randint(0,200))
    turtle.pendown()
random_f()


def random_f_star():

    turtle.bgcolor('black')
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(randint(-300,0),randint(0,300))
    turtle.pendown()
random_f()