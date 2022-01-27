# Chapter05_01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lamda)

# 함수 정의 방법
# def fuction_name(parameter):
# code

# 예제1
def first_func(w1):
    print("Hello, ", w1)

word = "Goodboy"

first_func(word)

# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)


# 예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z =func_mul(10)

print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

q = func_mul2(20)

print(type(q), q, list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


p = func_mul2(30)

print(type(p), p, set(q))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs

# *agrs(언팩킹)
def args_func(*args): # 매개변수 명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-------')

args_func('Lee')
args_func('Lee', 'Park')    
args_func('Lee', 'Park', 'Kim')

# kwargs(언팩킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('--------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
# func_in_func(1000) <- 따로 실행 불가