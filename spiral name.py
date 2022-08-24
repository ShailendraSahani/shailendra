import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=['red','green','yellow']
your_name=turtle.textinput("enter your name","what is your name?")
for x in range(100):
    t.pencolor(colors[x%3])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.left(92)
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))
    t.speed()
    