# Chapter03_04
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서 o, 중복o, 수정x, 삭제x) # 불변

# 선형

a = ()
b = (1,) # 하나일 때는 끝에 , 를 써야한다
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ',d[-1])
print('d - ',e[-1])
print('d - ',e[-1][1])
print('d - ',list(e[-1][1]))

# 수정 X
# d[0] = 1500 (에러 발생)

# 슬라이싱
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자 3이 들어있는 위치가 어디냐
print('a - ', a.count(2))

# 패킹 & 언팩킹(Packing, and unpacking)

# 패킹
t = ('apple', 'MS', 'google', 'amazon')

print()
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


#패킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)