# 꽃잎 그리기 - 함수활용

import turtle as t
import random

t.speed(0)
t.ht()
t.bgcolor("forestgreen")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# 꽃잎 한장 표현
def petal():
    for i in range(2):
        t.circle(150, 110)
        t.left(70)

# 꽃 만들기
def draw_flower():
    t.color(random_color()) # t.color(r,g,b) 0 ~ 255
    t.begin_fill()
    for i in range(6):
        petal()
        t.left(360/6)
    t.end_fill()
    # 꽃 수술 표현
    t.goto(0,-30)
    t.color(random_color())
    t.begin_fill()
    t.circle(30)
    t.end_fill()

draw_flower()