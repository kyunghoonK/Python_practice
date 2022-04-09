# Chapter08_01
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 실습

# 절대값
# abs()
print(abs(-3))
print()

# all, any : iterable 요소 검사(참, 거짓) (모두 참이어야 True가 나온다)
print(all([1,2,3])) # and
print(any([1,2,0])) # or
print()

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))
print()

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)
print()

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
# 람다식으로
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))
print()

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))
print()

# Len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))
print()

# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))
print()

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x:abs(x),[1,-3,2,0,-5,6])))

# pow : 제곱값 반환
print(pow(2,10))
print()

# range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))
print()

# round : 반올림
print(round(6.5781, 2))
print(round(5.6))
print()

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))
print()

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))
print()

# type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))
print()

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,60])))
print(type(list(zip([10,20,30],[40,50,60]))[0]))
print(type(list(zip([10,20,30],[40,50,60]))[0]))
