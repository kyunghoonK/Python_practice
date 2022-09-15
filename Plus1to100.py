# 1 ~ 100까지의 합

sum_100 = 0

for i in range(1,101):
    sum_100 += i

print(f'1부터 100까지의 합 : {sum_100}')

# 1 ~ 100까지의 짝수의 합

sum_even = 0

for i in range(2, 101, 2):
    sum_even += i

print(f'1부터 100까지 짝수의 합 : {sum_even}')