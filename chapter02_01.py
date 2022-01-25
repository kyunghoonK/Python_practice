#chapter02-1
#파이썬 완전 기초
#Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본 출력
print('Python start!')
print()
print("Python start!")

#separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='l')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')
print()

#end 옵션
print('welcome to', end=' ')
print('IT News', end='')
print('web site')
print()

# file 옵션
import sys
print('Learn Python',file=sys.stdout)

#format 사용(d : 3, s : 'python', f : 3.1445)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s - 자리수
print('%-10s' % ('nice')) 
print('{:10}'.format('nice'))
print()

print('%-10s' % ('nice')) 
print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))
print()

print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f

print('%1.8f' % (3.143535353535))#정수는 첫째, 소수는 여덟째 자리까지 출력
print('{:f}'.format(3.142323232))

print('%06.2f' % (3.141526353535))
print('{:06.2f}'.format(3.14159265))