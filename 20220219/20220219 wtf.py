import turtle

def tree (x,y):
    turtle.color('peru')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(x-50,y+100)
    turtle.setheading(90)
    turtle.color('green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(50)
    turtle.right(30)
    turtle.forward(75)
    turtle.right(30)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(100)
    turtle.end_fill()



tree(100,100)
tree(0,0)
tree(-50,-50)

turtle.done()