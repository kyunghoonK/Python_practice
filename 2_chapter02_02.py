# 2_Chapter02_02
# 객체 지향 프로그래밍(OOP) -> 코드으 재사용, 코드 중복방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim kyung hoon
    Date : 2022.08.05
    """
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self.details.get('price')))


# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'silver', 'horsepower' : 300, 'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring (주석 단거 보여주기)
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
