# 구구단

print(" !! 구구단 프로그램 출력 !!")

app_off="아니오"
while app_off == "아니오":
    num = int(input("구구단 몇 단을 출력할까요? : "))

    for i in range(1,10):
        print(f'{num} X {i} = {num*i}')

    app_off = input("프로그램을 종료하시겠습니까? 네 / 아니오 : ")
    print("=" * 50)

print("프로그램이 종료되었습니다.")