# 도박 게임
import random
money = int(input('배팅할 금액을 입력하세요. (스테이지 진행 중 금액 변경은 불가능 합니다.) : '))

print("STAGE 1 (x2)")
print("""
[1]   [2]
""")

S2 = """
[1]  [2]  [3]
"""

stage1_AS = random.randint(1,2)
stage1 = int(input("다음 두 상자 중 임의 상자 하나를 선택하라 : "))
if stage1_AS == stage1 :
    money *= 2
    print("승리!",money)
    next_level = input("다음 단계로 이동하시겠습니까? 성공시 3배, 실패시 0원. y or n >>> ").lower()
    if next_level == 'y':
        print('다음 단계로 이동합니다.')
        print(S2)
        stage2_AS = random.randint(1,3)
        stage2 = int(input("다음 세 상자 중 하나를 선택하라 : "))
        if stage2_AS == stage2 :
            money *= 3
            print("승리!", money)
        else :
            money = 0
            print('패배', money)
    else :
        print(f'게임이 종료되었습니다. 총금액{money}원')
else :
    money = 0
    print("패배",money)