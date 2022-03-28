# 1번
print('='*10, '1번시작', '='*10)
a = "20220328Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]

print(year)
print(day)
print(weather)

print()

# 2번
print('='*10, '2번시작', '='*10)
b = "I eat %d apples." %6
print(b)

print()

# 3번
print('='*10, '3번시작', '='*10)
number = 10
days = 'six'
c = "I eat %d apples. So I was sick %s days." %(number, days)
print(c)

print()

# 4번
print('='*10, '4번시작', '='*10)
d = "애플의 주식이 %d%% 하락하였습니다." %4
print(d)

print()

# 5번
print('='*10, '5번시작', '='*10)

e = "I eat {0} bananas".format(5)
print(e)