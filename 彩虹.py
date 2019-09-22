import turtle

pen = turtle.Pen()
turtle.bgolor('black')
sides = 7
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
for x in range(360):
    pen.pencolor(colors[x % sides])
    pen.forward(x * 3 / sides + x)
    pen.left(360 / sides + 1)
    pen.width(x * sides / 200)
