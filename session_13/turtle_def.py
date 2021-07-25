import turtle
laki = turtle.Turtle()

#create for

def draw_square(a):

    for i in range(4):
        laki.forward(a)
        laki.left(90)

a = 140
for i in range(50):
    a -= 3
    draw_square(a)



turtle.done()
