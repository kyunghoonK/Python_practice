# 문제1) 10번 찍어 넘어가는 나무(while문)
treehit = 0
while treehit < 10 :
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10 :
        print("나무가 넘어 갑니다.")

print()
print()

# 문제2) 숫자 맞추기 게임(while문)
prompt = "틀렸습니다. 다시 맞춰 보세요."
number = 0
print("숫자를 맞춰보세요.(1 이상 10 이하의 정수)")
while number != 8 :
    number = int(input("답 : "))
    if number > 8 :
        print(prompt)
        print("Hint : down")
    if number < 8 :
        print(prompt)
        print("Hint : up")
    if number == 8 :
        print("정답!")

print()
print()

# 문제3) 커피 자판기 프로그램을 만들어보세요.(while문)
coffee = 10
while True :
    money = int(input("돈을 넣어주세요(300원) : "))
    if money == 300 :
        print("커피가 나옵니다.")
        coffee = coffee - 1
    elif money > 300 :
        print("커피가 나옵니다.")
        print("거스름돈 %d원 입니다." %(money - 300))
        coffee = coffee - 1
    else :
        print("금액이 부족합니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

print()
print()

# 20 이하의 홀수만 출력하는 프로그램을 만들어보세요.
a = 0
while a < 20 :
    a = a + 1
    if a % 2 == 0 : continue
    print(a)
