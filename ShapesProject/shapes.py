

import turtle



from setting import MySetting


ResultShapes =  MySetting['Shashli']

turtle.fillcolor(ResultShapes['color'])
turtle.begin_fill()
for i in range(ResultShapes['rotations']):
    for f in range(ResultShapes['NumberLeft']):
        turtle.forward(ResultShapes['length'])
        turtle.left(ResultShapes['Left'])
        turtle.forward(ResultShapes['width'])
        turtle.left(ResultShapes['Left'])
turtle.end_fill()



