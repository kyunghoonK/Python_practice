# 사전 만들기

dict_eng = {"apple" : "사과", "peach" : "복숭아", "mango" : "망고"} # {key : value}

# 항목 추가
dict_eng["pear"] = "배"
print(dict_eng)

# 항목 삭제
del dict_eng["apple"]
print(dict_eng)

# 사전 
user_input = input("검색할 영어 단어를 입력하세요 >>> ")

if user_input in dict_eng :
    print(dict_eng[user_input])
else:
    print("검색하신 단어는 등록되어 있지 않습니다.")