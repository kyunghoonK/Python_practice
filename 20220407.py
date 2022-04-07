# if문 예제1
bag = ['books', 'pencilcase', 'money']

if 'money' in bag:
    print('커피를 사먹으세요')
else:
    print('커피를 마실 수 없습니다.')

# if문 예제2
pocket = ['card', 'cellphone', 'pencil']
cash = True
if cash in pocket:
    print('주머니에서 현금을 꺼내세요.')
elif cash:
    print('현금을 내세요.')
else :
    print('구매불가')

# while문 예제1
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")