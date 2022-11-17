from turtle import *
from random import randint



finish = 200

colormode(255)
t1 = Turtle()
t1.shape("turtle")
t1.color(randint(0,255),randint(0,255),randint(0,255))
t1.penup()
t1.goto(-200,-10)
t1.pendown()

t2 = Turtle()
t2.shape("turtle")
t2.color(randint(0,255),randint(0,255),randint(0,255))
t2.penup()
t2.goto(-200,-30)
t2.pendown()
t3 = Turtle()
t3.shape("turtle")
t3.color(randint(0,255),randint(0,255),randint(0,255))
t3.penup()
t3.goto(-200,-50)
t3.pendown()

t5 = Turtle()
t5.shape("turtle")
t5.color(randint(0,255),randint(0,255),randint(0,255))
t5.penup()
t5.goto(-200,-70)
t5.pendown()

def razmetka():
    t = Turtle()
    for i in range(1,21):
        t.penup()
        t.goto(-200+i*25,10)
        t.pendown()
        t.goto(-200+i*25,-50)
    t.hideturtle()
razmetka()

def catch1(x,y):
    t1.write('xe-xe', font=('Arial',15,'normal'))
    t1.fd(randint(5,15))
 

t1.onclick(catch1)
while t1.xcor() < finish and t2.xcor()<finish :
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
# begin_fill()

# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
