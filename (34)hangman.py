import random

eng_words = ['space', 'puppy', 'soccer']

answer = random.choice(eng_words)
guess_letters = list("_" * len(answer))
life = 3

game_over = False

while not game_over:

    print(f"남은 기회: {'❤' * life}번")
    user_guess = input("한 글자씩 추측해 보세요 >>> ").lower()
    
    if len(user_guess) == 1 and user_guess.isalpha():
        # 철자 확인하기
        for i in range(len(answer)):
            if answer[i] == user_guess:
                guess_letters[i] = user_guess
        print(guess_letters)
        print()

        if "_" not in guess_letters:
            game_over = True

            print("성공!!")
        
        if user_guess not in answer:
            life -= 1
            if life == 0 :
                game_over = True
                print(f"실패!! 정답은 {answer}입니다.")
    else:
        print("알파벳 하나 씩 입력해 주세요")