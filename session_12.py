#------------------------- وصل شدن به پکیج turtle ----------------------------
import turtle


#----------------------ساخت یک حلقه و چاپ یک 6 ضلعی-------------------------
for i in range(6):
    turtle.forward(100)
    turtle.right(60)

#----------------------ساخت یک حلقه و چاپ یک 8 ضلعی----------------------


for i in range(9):
    turtle.forward(100)
    turtle.right(40)

turtle.done()




#========================================================== ساخت شطرنج ====================================================




import turtle

sc = turtle.Screen()

pen = turtle.Turtle()

def draw():
    for x in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

if __name__ == "__main__" :
      
       
    # set turtle object speed
    pen.speed(100)
       
    # loops for board
    for i in range(8):
       
      # not ready to draw
      pen.up()

      # set position for every row
      pen.setpos(0, 30 * i)

      # ready to draw
      pen.down()
       
      # row
      
      for j in range(8):
       
        # conditions for alternative color
        if (i + j)% 2 == 0:
          col ='black'
       
        else:
          col ='white'
       
        # fill with given color
        pen.fillcolor(col)
       
        # start filling with colour
        pen.begin_fill()
       
        # call method
        draw()
        # stop filling
        pen.end_fill()
       
    # hide the turtle
    pen.hideturtle()


turtle.done()
