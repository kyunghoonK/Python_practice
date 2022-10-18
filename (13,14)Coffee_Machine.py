menu = """
     - 메 뉴 -
1. 아메리카노 2000원
2. 카페라떼 3000원
3. 카페모카 3500원
4. 레몬 에이드 4000원
"""
print(menu)
print("="*30)

price = 0
coffee = int(input('커피 종류를 선택하세요. 번호 입력 >>> '))
num = int(input('몇 잔을 드릴까요 >>> '))

if coffee == 1 :
    price = 2000
elif coffee == 2 :
    price = 3000
elif coffee == 3 :
    price = 3500
elif coffee == 4 :
    price = 4000
else :
    print("메뉴를 잘못 고르셨습니다.")

total = int(input(f'총 금액은 {price*num}입니다. 돈을 투입하여 주세요. >>> '))

if total > (price*num) :
    print(total,f"원 받았습니다. 거스름 돈은 {total-(price*num)}입니다.")
    change_1000 = (total-(price*num)) // 1000
    remain_1000 = (total-(price*num)) % 1000
    change_500 = remain_1000 // 500
    remain_500 = remain_1000 % 500
    change_100 = remain_500
    print(f'1000원 지폐 {change_1000}장, 500원 동전 {change_500}개, 100원 동전{change_100}개')
elif total == (price*num) :
    print('이용해 주셔서 감사합니다.')
else :
    print('금액이 부족합니다.')