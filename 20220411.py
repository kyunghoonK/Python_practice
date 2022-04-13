# 예외 처리
menu = ['사과', '바나나', '오렌지']

try:
    #실행할 코드
    user_input = int(input("0:사과, 1:바나나, 2:오렌지 >> "))
    order = menu[user_input]
except:
    #예외가 발생할 때 처리할 코드
    print("잘못된 주문입니다.")
#except IndexError:
#    print("메뉴에 없는 번호 입니다.")
#except ValueError:
#    print("번호로 입력해 주세요.")   
else:
    #예외가 발생하지 않고, 정상 실행되었을 때
    print(f"{order}주스를 주문하였습니다.")
finally:
    #항상 실행
    print("이용해 주셔서 감사합니다.")