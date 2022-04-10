# for문에 관하여
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

print()
print()

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first,last) in a :
    print(first + last)

print()
print()

# 다양한 for문의 응용(합격 불합격 판별)
marks = [90, 76, 55, 35, 60, 80]
number = 0
for score in marks :
    number = number + 1
    if score >= 60 :
        print("%d번 학생은 합격 입니다." %number)
    else :
        print("%d번 학생은 불합격 입니다." %number)

# range 사용
add = 0
for i in range(1,11) :
    add = add + i

print(add)

# range 사용2
results = [65, 45, 68, 75, 90]
for number in range(len(results)):
    if results[number] < 80 : continue
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))

# for문 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print(' ')

print()
print()

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)