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

glist = [0, 0, 0, 0]

game_Start()
play_Game(glist)

