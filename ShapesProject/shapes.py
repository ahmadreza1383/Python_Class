


#Array number


import turtle







# MySetting = {

#     'Shashli' : {

#     'color' : 'green',
#     'width' : 60,
#     'length': 60,
#     'Left' : 60,
#     'NumberLeft' : 1,
#     'rotations'  : 3,

#     },


#     'Rectangle':{

#     'color' : 'red',
#     'width' : 30,
#     'length': 60,
#     'Left' : 90,
#     'NumberLeft' : 1,
#     'rotations'  : 2,

#     }, 

#     'Square'   : {

#     'color' : 'blue',
#     'width' : 40,
#     'length': 40,
#     'Left' : 90,
#     'NumberLeft' : 1,
#     'rotations'  : 2,


#     },

#     'Triangle' :{

#     'color' : 'green',
#     'width' : 70,
#     'length': 70,
#     'Left' : 120,
#     'NumberLeft' : 1,
#     'rotations'  : 2,

#     },


# }

# ResultShapes =  MySetting['Rectangle']

# for i in range(ResultShapes['rotations']):
#     for f in range(ResultShapes['NumberLeft']):
#         turtle.forward(ResultShapes['length'])
#         turtle.left(ResultShapes['Left'])
#         turtle.forward(ResultShapes['width'])
#         turtle.left(ResultShapes['Left'])
    

# turtle.done()

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



