# 딕셔너리
a = {1 : 'a'}
a[2] = 'b'
a['name'] = 'pey'
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)

# 딕셔너리 활용
spo = {
    'name' : 'cho',
    'age' : 24,
    'backnumber' : 11
}
print(spo['age'])

# 딕셔너리 관련 함수
me = {
    'name' : 'kim',
    'phone' : '010-1234-2233',
    'birth' : '970229'
}

# key 값 출력
print(me.keys())

for k in me.keys():
    print(k)

print(list(me.keys()))

# value 값 출력
print(me.values())

# key, value 쌍으로 출력
print(me.items())

# key로 value 값 얻기
print(me.get('name'))
print(me['name'])

# key가 딕셔너리 안에 있는지 조사
print('name' in me)
print('address' in me)

# 03_05-------------------------------------------