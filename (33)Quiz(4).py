import random

eng_word = [
    ["orbit", "궤도"],
    ["gravity", "중력"],
    ["laboratory", "실험실"],
    ["oxygen", "산소"],
    ["nutrient", "영양소"],
    ["satellite", "위성"],
    ["galaxy", "은하계"],
    ["germ", "미생물"],
    ["planet", "행성"],
    ["ethics", "윤리학"],
    ["culture shock", "문화 충격"],
    ["ad", "광고"]
    ]

quiz_on = True
score = 0
quiz_num = 0

while quiz_on:
    # 4지선다 보기 항목
    multi_choice = random.sample(eng_word, 4)
    answer_index = random.randint(0,3) # 0, 1, 2, 3

    print(f"문제{quiz_num}번) {multi_choice[answer_index][0]}의 뜻은?")

    # 보기 출력
    for i in range(4):
        print(f"{i+1}. {multi_choice[i][1]}")

    print()
    user_input = int(input("정답을 입력해 주세요. (종료: 0) >>>  "))

    # 정답 확인
    if user_input == 0:
        quiz_on = False
        print("퀴즈가 종료되었습니다.")
        print(f"총 {quiz_num-1}문제 중 {score}문제를 맞추셨습니다.")
    elif user_input == answer_index + 1 :
        score += 1
        print("정답입니다.")
    else:
        print(f"오답입니다. 정답은 {answer_index + 1}번 입니다. ")
    print()