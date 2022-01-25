# chapter03_3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>인덱싱')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>슬라이싱')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>리스트 연산')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print('>>>>>값비교')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정
print('>>>>리스트수정')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 끝에다가 추가
print('a - ', a)
a.sort() # 크기 순으로 정렬해줌(오름차순)
print('a - ', a)
a.reverse() # 역순으로 출력
print('a - ', a)
print('a -', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a -', a.pop())
print('a - ', a)
print('a -', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 4 라는 값이 몇개 있나요?
ex = [8, 9]
a.extend(ex) # 연장
print('a - ', a)

# 삭제 : remove, pop, del

# 반목문 활용
while a:
    data = a.pop()
    print(data)








