# Chapter03_05
# 파이썬 딕션어리
# 범용적으로 많이 사용
# 딕셔너리 자료형(순서X, 키중복X, 수정O, 삭제O)

# 선언
a = {'name': 'kim', 'phone': '01033337777', 'birth': '970112'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade= 'A',
    Status=True
) # 이게 깔끔한 방법임

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 존재X -> 에러
print('a - ', a.get('name')) # 존재X -> None
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ',f.get('City'))
print('f - ',f.get('Age'))


# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(_iter_)에서 사용 가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) # 무작위로 하나 추출
print('f - ', f)

print()

print('a - ', 'birth2' in a) # a에 birth2 라는게 있니?
print('d - ', 'City' in d)

# 수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904') # 수정
print('a - ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)





