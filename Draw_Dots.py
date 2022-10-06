import turtle as t
import random

size = 50 # 전역변수 : 함수 밖에서 저의 된 변수
color = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

def draw_dot(x,y): # 지역 변수 : 함수 안에서 정의된 변수
    t.up()
    t.goto(x, y)
    t.dot(size)

def draw_triangle(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(360/3)
    t.end_fill()

def draw_square(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(random.randint(0, 360))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(360/4)
    t.end_fill()

def rand_color():
    t.color(random.choice(color))

def size_up():
    global size # 전역 변수를 변경하고 싶을 때는 global을 사용해야해요
    size += 10

def size_down():
    global size
    if size > 10 :
        size -= 10

t.bgcolor("ivory")
t.speed(0)
t.onscreenclick(draw_dot, 1) # 마우스 왼쪽 버튼 클릭 시
t.onscreenclick(draw_triangle, 2) # 휠 클릭
t.onscreenclick(draw_square, 3) # 마우스 오른쪽 버튼 클릭 시
t.onkeypress(rand_color, "space") # 스페이스바 클릭 시
t.onkeypress(size_up, "Up") # 사이즈 크게
t.onkeypress(size_down, "Down") # 사이즈 작게
t.listen()

t.done()