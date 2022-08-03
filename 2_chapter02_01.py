# 2_Chapter02_01
# 객체 지향 프로그래밍(OOP) -> 코드으 재사용, 코드 중복방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'silver', 'horsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)