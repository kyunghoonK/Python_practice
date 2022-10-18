import turtle as t
import time
import random
t.bgcolor("pink")
t.ht()
t.up()
t.write("숫자 기억하기 게임을 시작합니다.", False, "center",("", 30))
time.sleep(3)
t.clear()

num_times = int(t.textinput("숫자 기억하기 게임", "몇 개의 숫자로 진행하시겠습니까?"))

num = ""
for x in range(num_times):
    rand_num = random.randint(1, 50)
    t.write(rand_num, False, "center", ("", 70))
    num += str(rand_num)
    num += " "
    time.sleep(1)
    t.clear()

user_input = t.textinput("숫자 기억 게임", "기억한 숫자를 입력하세요") # t.textinput(제목, 질문)

if user_input == num.strip():
    t.write("정답입니다.", False, "center", ("", 30))
else:
    t.write("오답입니다.", False, "center", ("", 30))
    t.goto(0, -50)
    t.write(f"정답은 {num}입니다.",False, "center", ("", 30))
    t.goto(0,-100)
    t.write(f"입력하신 수는 {user_input}입니다.",False, "center", ("", 30))