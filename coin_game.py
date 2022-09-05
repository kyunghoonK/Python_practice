import random

head = """
(앞면)
"""

tail = """
(뒷면)
"""

print("동전 던지기 게임에 오신 것을 환영합니다.")

computer = random.randint(0,1)
choice = int(input("앞면일까요? 뒷면일까요? 0:앞면, 1:뒷면 : "))

print("동전 결과 : ")
if computer == 0:
    print(head)
else:
    print(tail)

print("나의 선택 : ")
if choice == 0:
    print(head)
else:
    print(tail)

print("게임 결과 : ")
if computer == choice :
    print("적중!!")
else:
    print("아쉽네요. 틀렸습니다.")