# 숫자 up * down 게임

import random

print("숫자 맞추기 게임(1~100)")

answer = random.randint(1,100)
user_answer = 0
attempt = 0

while user_answer != answer:
    user_answer = int(input("정답을 입력하세요. : "))
    attempt += 1
    
    if user_answer > answer :
        print("down")
    else :
        print("up")
    
    print()

print(f"정답입니다.{attempt}번만에 맞췄습니다.")