def kyunghoon(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("1 ~ 10 =", kyunghoon(1, 10, 2))
print("2 ~ 10 =", kyunghoon(2, 10, 2))

def calcscore(name, *score, **option):
    print("성명:", name)
    sum = 0
    for s in score:
        sum += s
    print("총점 :", sum)
    if (option['avg'] == True):
        print("평균 :", sum / len(score))

calcscore("김일번", 88, 96, 76, avg = True)
calcscore("김이번", 90, 82, 92, 70, avg = False)
