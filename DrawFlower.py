# 꽃잎 그리기 - 함수활용

import turtle as t
import random

t.speed(0)

def petal(size, angle): # 꽃 잎 한장 그리는 함수
    for i in range(2):
        t.circle(size, angle) #(반지름, 각도)
        t.left(180-angle)

def draw_flower(petal_num, petal_size, petal_angle):
    t.color("pink")
    t.begin_fill()
    for i in range(petal_num):
        petal(petal_size, petal_angle)
        t.left(360/petal_num)
    t.end_fill()

    t.goto(0,-30)
    t.color("hotpink")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.ht()
t.bgcolor("black")

petal_num = random.randint(4, 10)
petal_size = random.randint(50, 120)
petal_angle = random.randint(90, 130)

draw_flower(petal_num, petal_size, petal_angle)
