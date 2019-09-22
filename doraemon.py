import turtle

t = turtle.Turtle()


def penup():
    t.penup()


def goto(e, y):
    t.goto(e)


def pendown():
    t.pendown()


def fd(e):
    t.forward(e)


def seth(e):
    t.seth(e)


def circle(e):
    t.circle(e)


def fillcolor(e):
    t.fillcolor(e)


def begin_fill():
    t.begin_fill()


def end_fill():
    t.end_fill()


def lt(e):
    t.lt(e)


def home():
    t.home()


def tracer(x, y):
    t.tracer(x, y)


def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def eyes():
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)


def beard():
    my_goto(-37, 135)
    seth(165)
    fd(60)

    my_goto(-37, 125)
    seth(180)
    fd(60)

    my_goto(-37, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)


def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    my_goto(-10, 158)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def pensize(param):
    t.pensize(param)


def black_eyes():
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)


def face():
    fd(183)
    fillcolor('#ffffff')
    begin_fill()
    lt(45)
    circle(120, 100)

    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()


def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def doraemon():
    head()
    scarf()
    face()
    nose()
    mouth()
    beard()
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(-1000, 10)

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print (pos())
    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    home()