# 홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연원일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
'''
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
'''

# 주민등록자리 뒷자리의 첫 번째 숫자로 성별을 판별하는 프로그램을 작성해라

'''
pin_num = input("주민등록번호를 입력하세요(ex)9811301234567 : ")
print(pin_num[6]) #9701121271113
'''

# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자

'''
a = "a:b:c:d"
b = a.replace(":", "#")

print(a)
print(b)
'''

# [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
'''
c = [1, 3, 5, 4, 2]

c.sort()
c.reverse()

print(c)
'''

# ['Life', 'is', 'too', 'short'] 라는 리스트를 Life is too short라는 문자열로 만들어 출력해 보자.

'''
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
'''

# (1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력하세요.
'''
a = (1,2,3,)
a = a + (4,)
print(a)
'''