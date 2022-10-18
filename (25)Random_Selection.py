# 랜덤 뽑기
import random
import time

name = input("참가자들의 이름을 입력해 주세요. 예) 철수 영희 >>> ").split()

print(f"총 {len(name)}명이 참가하셨습니다.")

winner = random.choice(name)

print("오늘 선택된 사람은 .... ")
time.sleep(3)
print(f"{winner}님 입니다.")