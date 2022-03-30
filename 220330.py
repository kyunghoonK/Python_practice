# 각종 정렬

# 왼쪽 정렬
"{0:<15}".format("Hello")

# 오른쪽 정렬
"{0:>15}".format("Hello")

# 가운데 정렬
"{0:^15}".format("Hello")

# 공백 채우기
"{0:=^10}".format("Hi")

# 소수점 표현하기
y = 3.4213567
"{0:0.4f}".format(y)

# f열 문자 포매팅
name = 'Mason'
age = '27'
f'나의 이름은 {name}입니다. 나이는 {age}세 입니다.'

# 딕셔너리 활용
set1 = {'name1' : 'gavi', 'age' : 20}
f'그의 이름은 {set1["name1"]} 입니다. 그의 나이는 {set1["age"]}살 입니다.'