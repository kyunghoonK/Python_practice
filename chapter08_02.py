# Chapter08-2
# 파이썬 외장 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
import sys
print(sys.argv)
print()
print()

# 예제2 - 강제 종료
# sys.exit()

# 예제 3 - 파이썬 패키지 위치
print(sys.path)

print()
print()

# pickle : 객체 파일 읽기,쓰기
import pickle

# 예제4 - 쓰기
f = open("test.obj", 'wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj,f)
f.close()

print()
print()

# 예제5 - 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()
