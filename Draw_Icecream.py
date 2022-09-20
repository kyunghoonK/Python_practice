# 아이스크림 그리기

import turtle as t

t.bgcolor("black")
t.color("yellow")

# 콘 그리기(역삼각형 그리기)
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.right(360/3)
t.end_fill()

# 원 그리기
t.forward(100)
t.color("green")
t.begin_fill()
t.circle(100) # 반지름
t.end_fill()

# 원 그리기
t.goto(120,120) # goto(x좌표, y좌표) - 특정지점으로 이동
t.color("pink")
t.begin_fill()
t.circle(70) # 반지름
t.end_fill()

# 별 모양 그리기
t.color("black")
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()