import turtle as t
import random

def com_choice():
    rand_choice = random.randint(0,2)
    com.shape(images[rand_choice])
    return com_list[rand_choice]


def result_print(user_c, com_c):
    global user_score, com_score
    t.clear()
    t.goto(0,-100)
    if user_c == com_c:
        t.write("무승부", False, "center", ("", 50))
    elif winning_case[user_c] == com_c:
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False, "center", ("", 50))
        t.write("승", False, "center", ("", 50))
    else:
        com_score += 1
        com_pen.clear()
        com_pen.write(com_score, False, "center", ("", 50))
        t.write("패", False, "center", ("", 50))


def rock(x, y):
    user.shape(rock_gif)
    com = com_choice() # 컴퓨터 선택 - 랜덤 선택
    result_print("rock", com) # 승부 결과 판정

def scissors(x, y):
    user.shape(scissors_gif)
    com = com_choice() # 컴퓨터 선택 - 랜덤 선택
    result_print("scissors", com)# 승부 결과 판정

def paper(x, y):
    user.shape(paper_gif)
    com = com_choice() # 컴퓨터 선택 - 랜덤 선택
    result_print("paper", com)# 승부 결과 판정

# 기본 설정
t.bgcolor("lavender")
t.title("가위바위보 게임")
t.ht()
t.up()

rock_gif = "images/rock.gif"
scissors_gif = "images/scissors.gif"
paper_gif = "images/paper.gif"

# t.addshape(이미지 파일 경로)
t.addshape(rock_gif)
t.addshape(scissors_gif)
t.addshape(paper_gif)

images = [rock_gif, scissors_gif, paper_gif]
com_list = ["rock", "scissors", "paper"]
winning_case = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
user_score = 0
com_score = 0

# 유저 선택 이미지
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-200, 200)
user.write("나의 선택", False, "center", ("",30))
user.goto(-200, -100)
user.shape(rock_gif)


# 컴퓨터 선택 이미지
com = t.Turtle()
com.up()
com.speed(0)
com.goto(200, 200)
com.write("컴퓨터 선택", False, "center", ("",30))
com.goto(200, -100)
com.shape(rock_gif)

# 유저 점수 펜
user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-200, 100)
user_pen.write(user_score, False, "center", ("", 50))

# 컴퓨터 점수 펜
com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(200, 100)
com_pen.write(com_score, False, "center", ("", 50))

t.onscreenclick(rock, 1) # 마우스 좌 클릭
t.onscreenclick(scissors, 2) # 마우스 휠 클릭
t.onscreenclick(paper, 3) # 마우스 우 클릭











t.done()