import turtle as t
import random

t.shape("turtle")                     #모양을 거북이로 바꾼다.
t.pensize(5)                          #펜의 굵기를 5로 한다.
t.up()
t.goto(-250,-250)                     #이 좌표로 이동.
t.down()

for x in range(4):                    #거북이의 집을 만들어준다.
    t.fd(500)
    t.lt(90)

t.up()
t.home()
t.down()
t.speed(3)
t.goto(0,-250)
t.goto(250,0)
t.goto(0,250)
t.goto(-250,0)
t.goto(0,-250)
t.home()

