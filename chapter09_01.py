# chapter09_01
# 파일 읽기 및 쓰기

# 읽기 모드 r, 쓰기 모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로(' ../ , ./ ') <- 현재 폴더 위치부터 따져보는것
# 절대 경로('C:\Django\example..') <- 저장 장치의 루트 경로부터 따짐

# 파일 읽기(Read)
# 예제1

# 절대 경로
# f = open('C:\\python_basic\\resource\\it_news.txt')

# 상대 경로
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)

# 반드시 close
f.close()

print()
print()

# ----- 강의 <File Write(1-2)> -----
# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10Byte

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)  # 처음으로 돌아가
    c = f.read(20)
    print(c)

print()

# 예제4
# readline : 한 줄씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# -------강의 <File Write(1-3)> -------

# 파일 쓰기(write)

# 예제 1
with open('./resource/contents1.txt', 'w') as f:
    f.write('last time\n')

# 예제 2
with open('./resource/contents1.txt', 'a') as f:
    f.write('do not miss\n')

# 예제 3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제 4
with open('./resource/contents2.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)

