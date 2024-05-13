import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(3)
    t.color(color)
    t.begin_fill()
    for counter in range (1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup
    
t.bgcolor('#03dbfc') #background
t.speed('fastest') #speed
t.penup()
t.setup(800,600) #canvas

#feet
t.goto(-100, -150)
rectangle(50, 20, 'grey')
t.up()
t.goto(-30, -150)
rectangle(50, 20, 'grey')

#legs
t.goto(-30, -50)
rectangle(15, 100, 'grey')
t.up()
t.goto(-65, -50)
rectangle(15, 100, 'grey')

#body
t.goto(-90, 100)
rectangle(100, 150, 'grey')

#arms
t.up()
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.up()
t.goto(10, 70)
rectangle(60, 15, 'grey')

#head



    
