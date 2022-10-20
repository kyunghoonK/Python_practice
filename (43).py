# 프랙탈 나무 그리기

import turtle as t

t.setheading(90)


def tree(length):
    t.forward(length)
    t.left(50)
    tree()# 가지 그리기
    t.right(100)
    tree()# 가지 그리기
    t.left(50)
    t.backward(length)