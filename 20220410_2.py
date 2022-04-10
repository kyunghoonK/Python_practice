def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

a = add_many(1,2,3)
print(a)

print()
print()

# 여러 개의 입력값을 받는 함수
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

b = add_mul('add', 14,15,41)
print(b)

c = add_mul('mul', 14, 32, 11)
print(c)