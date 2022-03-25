import random

# 1~100 사이의 정수값 생성
random_number = random.randint(1, 100)

##################################################################################
# random.ramdom()           ->  0.0 ~ 0.999999 사이의 실수값
# random.uniform(a,b)       ->  a와 b 사이의 실수값
# random.randint(a,b)       ->  a와 b 사이의 정수값
# random.randrange(a,b)     ->  a와 b 사이의 정수값
# random.randrange(a)       ->  0과 a 사이의 정수값
# random.choice(type)       ->  type(문자열,리스트,튜플,range 값 입력 후 무작위 추출)
##################################################################################

game_count = 1

while True:
    try:
        my_number = int(input("1에서 100사이의 값을 입력하세요 : "))
        
        if my_number > random_number:
            print("더 작은 숫자입니다.")
        elif my_number < random_number:
            print("더 큰 숫자입니다.")
        elif my_number == random_number:
            print(f"딩동댕~!!! {game_count}번째에 맞췄습니다.")              # f-string 3.6부터 적용
            break

        game_count = game_count + 1
        
    except:
        print("오류 발생. 숫자를 입력해주세요.")
    
    
