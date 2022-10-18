# 비밀번호 잠금 헤제 프로그램

lock = """
Locked
비밀번호를 입력하세요
     [      ]
"""

unlock = """
unlock
잠금 해제
"""

wrong_password = """
비밀번호가 틀렸습니다.
다시 입력하세요.
"""

print(lock)

user_input = input("비밀번호를 입력해 주세요 >>> ")

while user_input != 'A1234!' :
    print(wrong_password)
    user_input = input("잘못된 비밀번호 입니다. 다시 입력해 주세요 >>> ")

print("잠금이 해제되었습니다.")
print(unlock)
