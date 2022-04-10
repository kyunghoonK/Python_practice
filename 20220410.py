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