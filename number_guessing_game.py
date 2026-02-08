import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    
    print("숫자 맞히기 게임에 오신것을 환영합니다!")
    print("저는 1과 100사이의 숫자를 생각중입니다")
    
    while True:
        try:
            guess = int(input("추측을 입력하세요: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("1과 100사이의 숫자를 입력해주세요")
                continue
            
            if guess < number:
                print("너무나 낮습니다! 다시 시도해주세요.")
            elif guess > number:
                print("너무나 높습니다! 다시 시도해주세요.")
            else:
                print(f"축하합니다! {number}을/를 {attempts}시도만에 맞췄습니다!")
                break
                
        except ValueError:
            print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    number_guessing_game()
