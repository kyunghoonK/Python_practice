# BMI 계산
print("체질량 지수 BMI를 확인해 보세요!")

height = float(input("키를 입력하세요(단위 : m) >>> "))
weight = float(input("몸무게를 입력하세요 >>> "))

# bmi = 몸무게/키 * 키
bmi = round(weight / height ** 2, 1)

print("="*20)
print("BMI 결과")
print("="*20)
print()

if bmi < 18.5 :
    print("저체중 입니다.")
elif 18.5 <= bmi < 25 :
    print("정상 입니다.")
elif 25 <= bmi < 30 :
    print("경도 비만 입니다.")
elif 30 <= bmi < 35 :
    print("중도 비만 입니다.")
else :
    print("고도 비만 입니다.")

