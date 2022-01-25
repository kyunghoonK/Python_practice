# chapter03_02
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")
print('I\'m Boy')
print('a \t b')
print('a \n b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

#Row String 
raw_s1 = r'D:\tpython\test'
print(raw_s1)
print()

# 멀티라인 입력 방법
# 역슬러시 사용
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)

#문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"


print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #str_o1 안에 y 라는 알파벳이 있어?
print('n' in str_o1)
print('P' not in str_o2)#str_o2 안에 P가 없니?

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) #시작 글자를 대문자로 바꿔주는 함수
print("endwith?: ", str_o2.endswith("s")) # 끝 글자가 s 로 끝나?
print("replace", str_o1.replace("thon", "Good")) # thon부분을 Good로 바꿔줘 
print("sorted: ", sorted(str_o1))
print("split: ",str_o4.split(' ')) # 단어별, 문장별로 분리


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 가 있다면 반복할 수 있다.

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"


# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) # 5부터 끝까지
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1)-1])# str_s1[:10]
print(str_s1[1:9:2])
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로