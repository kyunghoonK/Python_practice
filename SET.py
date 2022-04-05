# 집합 자료형
s1 = set([5, 6, 7, 13, 34, 45, 58])
s2 = set([4, 22, 54, 13, 34, 45, 88])
s3 = set([24, 13, 22, 77, 44, 99, 120])

print(s1)
print(s2)
print(s3)
print()
# 교집합
print(s1 & s2)
print(s1.intersection(s3))
print()

# 합집합
print(s1 | s2)
print(s1.union(s3))
print()

# 차집합
print(s1 - s2)
print(s1.difference(s3))
print()

# 집합에 추가(1개)
s1.add(6000)
print(s1)
print()

# 집합에 추가(여러개)
s2.update([9000, 8000, 5000])
print(s2)
print()

# 집합에서 특정값 제거
s2.remove(9000)
print(s2)
