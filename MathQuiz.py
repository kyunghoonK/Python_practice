# 수학 퀴즈 게임

import random
import time

print("기초 수학 퀴즈")
print()

playing = True
score = 0
count = 0

start_time = time.time()
while playing:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    num3 = random.randint(1,20)

    answer = num1 * num2 - num3
    user_input = int(input(f"{num1} * {num2} - {num3} = "))
    count += 1


    if answer == user_input:
        score += 1
        print(f"정답 입니다. 현재 점수는 {score}입니다.")
    else:
        playing = False
        print(f"아쉽네요. 정답은 {answer}였습니다.")

end_time = time.time()
print(f'총 {count}문제를 {round(end_time - start_time)}초만에 해결하셨습니다!')
print("Math Quiz가 종료되었습니다.")