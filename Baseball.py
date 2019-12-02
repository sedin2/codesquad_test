import random

def game_Start():
    print("신나는 야구 게임!")
    print("첫 번째 타자가 타석에 입장했습니다.")

def play_Game(action_list):
    action = random.randrange(0, 4)
    
    if action == 0:
        action_list[action] += 1
    elif action == 1:
        action_list[action] += 1
    elif action == 2:
        action_list[action] += 1
    elif action == 3:
        action_list[action] += 1
        
    return action

def play_Check(check):
    if check == 0:
        print("스트라이크!")
    elif check == 1:
        print("볼!")
    elif check == 2:
        print("안타! 다음 타자가 타석에 입장했습니다.")
    elif check == 3:
        print("아웃! 다음 타자가 타석에 입장했습니다.")

def play_Show(action_list):
    print(str(action_list[0]) + "S " + str(action_list[1]) + "B " + str(action_list[2]) + "H " + str(action_list[3]) + "Out ")
    print("")

glist = [0, 0, 0, 0] # 스트 / 볼 / 안타 / 아웃 카운트 하는 list
random_check = 0
play_check = 0


game_Start()

# 0,1,2,3 -> 스트라이크 / 볼 / 안타/ 아웃 -> 체크에 넣음
random_check = play_Game(glist)

#랜덤으로 나온것 출력
play_Check(random_check) 

play_Show(glist)


