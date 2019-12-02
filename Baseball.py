import random

def game_Start():
    print("신나는 야구 게임!")
    print("첫 번째 타자가 타석에 입장했습니다.")
    print()

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

def play_Check(action_list, check):
    if check == 0 and action_list[0] <3:
        print("스트라이크!")
        return 0
    elif check == 0 and action_list[0] == 3:
        print("스트라이크!")        
        action_list[3] += 1                                 #3스트 1아웃 추가
        if action_list[3] < 3:                              #아웃 3개 미만 일 때    
            print("아웃! 다음 타자가 타석에 입장했습니다.") #다음 타자 입장
            return 3
        else:
            return 4                                        #3아웃 일 때 
    elif check == 1 and action_list[1] < 4:
        print("볼!")
        return 1
    elif check == 1 and action_list[1] == 4:
        print("볼!")
        print("안타! 다음 타자가 타석에 입장했습니다.")     #다음 타자 입장
        action_list[check+1] += 1                           #4볼 1안타 추가
        return 2 
    elif check == 2:
        print("안타! 다음 타자가 타석에 입장했습니다.")
        return 2
    elif check == 3 and action_list[3] < 3:
        print("아웃! 다음 타자가 타석에 입장했습니다.")
        return 3
    elif check == 3 and action_list[3] == 3:
        print("아웃!")
        return 4                                            #3아웃 일 때

def play_Show(action_list):
    print(str(action_list[0]) + "S " + str(action_list[1]) + "B " + str(action_list[3]) + "Out ")
    print("")

def play_Init(action_list):
    action_list[0] = 0
    action_list[1] = 0

def play_Finish(action_list):
    print("최종 안타수: " + str(action_list[2]))
    print("GAME OVER")
    
    
glist = [0, 0, 0, 0]                                        # 스트 / 볼 / 안타 / 아웃 카운트 하는 list
random_check = 0
play_check = 0

game_Start()                                                # 게임 시작

while(True):
    
    random_check = play_Game(glist)                         # 0,1,2,3 -> 스트라이크 / 볼 / 안타/ 아웃 -> 체크에 넣음
    play_check = play_Check(glist, random_check)            # 3스트 4볼 안타 3아웃 체크
    
    if play_check == 0 or play_check == 1:                  # 스트, 볼 나왔는데 3스트, 4볼 미만 일 때
        play_Show(glist)
    elif play_check == 2 or play_check == 3:                # 스트, 볼 나왔는데 3스트, 4볼 일 때
        play_Init(glist)
        play_Show(glist)
    elif play_check == 4:                                   # 3아웃 일 때 게임 종료
        play_Init(glist)
        play_Show(glist)
        play_Finish(glist)
        break

    


