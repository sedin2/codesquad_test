import os
import random

def open_File(file_name, format):
    file = open(file_name, format, encoding = 'UTF-8')
    return file

def close_File(file_name):
    file_name.close()

def write_File(file_name):
    for i in range(0, 20):
        if i == 0:
            text = input(str(i+1) + "팀의 이름을 입력하세요> ")
            file_name.write(text + " 팀 정보\n")
        elif i < 10:
            text = input(str(i) + "번 타자 정보 입력> ")
            file_name.write(str(i) + "번 " + text + "\n")
        elif i == 10:
            text = input(str(i-8) + "팀의 이름을 입력하세요> ")
            file_name.write(text + " 팀 정보\n")
        else:
            text = input(str(i-10) + "번 타자 정보 입력> ")
            file_name.write(str(i-10) + "번 " + text + "\n")
    print()
    print("팀 데이터 입력이 완료되었습니다.")
    
def read_File(file_name):
    try:
        for s in file_name:
            print(s.strip())
    except:
        print("오류")
    finally:
        print()

def file_Split(file_name):
    tmp = []
    try:
        for s in file_name:
            tmp.append(s.replace(',',' ').split(maxsplit=4))
    except:
        print("오류")
    return tmp

def data_Split(data_list):
    tmp_data = []
    for i in range(len(data_list)):
        if i == 0 or i == 10:
            team_Name(data_list, i, tmp_data)
        else:
            team_Player(data_list, i, tmp_data)             
    return tmp_data

def team_Name(data_list, i, tmp_data):
    tmp = ""
    for j in range(0, len(data_list[i])-2):
        tmp += data_list[i][j] + " "
    tmp_data.append(tmp)

def team_Player(data_list, i, tmp_data):
    for j in range(1, len(data_list[i])):
        tmp_data.append(data_list[i][j])

def sim_File(file_name, team_list):
    player_cnt1 = 1
    player_cnt2 = 1
    score_cnt1 = 0
    score_cnt2 = 0
    team_score1 = [0, 0, 0, 0]
    team_score2 = [0, 0, 0, 0]
    file_name.write(team_list[0] + " VS " + team_list[19] + " 시합을 시작합니다.\n")
    file_name.write("\n")
    print(team_list[0] + " VS " + team_list[19] + " 시합을 시작합니다.\n")
    print("")
    for i in range(1, 7):
        team_score1[3] = 0
        team_score2[3] = 0
        if team_score1[2] >= 4:
            score_cnt1 += team_score1[2] - 3
            team_score1[2] = 0
        else:
            team_score1[2] = 0

        if team_score2[2] >= 4:
            score_cnt2 += team_score2[2] - 3
            team_score2[2] = 0
        else:
            team_score2[2] = 0
            
        file_name.write(str(i) + "회초 " + team_list[0] +" 공격\n")
        file_name.write("\n")
        while(True):
            file_name.write(str(player_cnt1) + "번 " + team_list[(2*player_cnt1)-1] + "\n")
            if team_score1[3] == 3:
                break
            action1 = play_Game(team_list, player_cnt1, team_score1, 1)
            if action1 == 0 and team_score1[0] < 3:
                file_name.write("스트라이크!\n")
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")             
            elif action1 == 0 and team_score1[0] == 3:
                file_name.write("스트라이크!\n")
                file_name.write("아웃! 다음 타자가 타석에 입장했습니다.\n")
                team_score1[3] += 1
                team_score1[0] = 0
                team_score1[1] = 0
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
                if team_score1[3] == 3:
                    player_cnt1 += 1
                    if player_cnt1 == 10:
                        player_cnt1 = 1
                    break
                else:
                    player_cnt1 += 1
                    if player_cnt1 == 10:
                        player_cnt1 = 1
            elif action1 == 1 and team_score1[1] < 4:
                file_name.write("볼!\n")
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
            elif action1 == 1 and team_score1[1] == 4:
                file_name.write("볼!\n")
                file_name.write("안타! 다음 타자가 타석에 입장했습니다.\n")
                team_score1[2] += 1
                team_score1[0] = 0
                team_score1[1] = 0
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
                player_cnt1 += 1
                if player_cnt1 == 10:
                    player_cnt1 = 1                
            elif action1 == 2:
                file_name.write("안타! 다음 타자가 타석에 입장했습니다.\n")
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
                team_score1[0] = 0
                team_score1[1] = 0
                player_cnt1 += 1
                if player_cnt1 == 10:
                    player_cnt1 = 1
            elif action1 == 3 and team_score1[3] < 3:
                file_name.write("아웃!\n")
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
                player_cnt1 += 1
                if player_cnt1 == 10:
                    player_cnt1 = 1
            elif action1 == 3 and team_score1[3] == 3:
                file_name.write("아웃!\n")
                team_score1[0] = 0
                team_score1[1] = 0
                file_name.write(str(team_score1[0]) + "S " + str(team_score1[1]) + "B " + str(team_score1[3]) + "Out\n")
                file_name.write("\n")
                player_cnt1 += 1
                if player_cnt1 == 10:
                    player_cnt1 = 1
                break
            
        file_name.write(str(i) + "회말 " + team_list[19] +" 공격\n")
        file_name.write("\n")
        while(True):
            file_name.write(str(player_cnt2) + "번 " + team_list[(2*player_cnt2)+18] + "\n")
            if team_score2[3] == 3:
                break
            action2 = play_Game(team_list, player_cnt2, team_score2, 2)
            if action2 == 0 and team_score2[0] < 3:
                file_name.write("스트라이크!\n")
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
            elif action2 == 0 and team_score2[0] == 3:
                file_name.write("스트라이크!\n")
                file_name.write("아웃! 다음 타자가 타석에 입장했습니다.\n")
                team_score2[3] += 1
                team_score2[0] = 0
                team_score2[1] = 0
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
                if team_score2[3] == 3:
                    player_cnt2 += 1
                    if player_cnt2 == 10:
                        player_cnt2 = 1
                    break
                else:
                    player_cnt2 += 1
                    if player_cnt2 == 10:
                        player_cnt2 = 1
            elif action2 == 1 and team_score2[1] < 4:
                file_name.write("볼!\n")
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
            elif action2 == 1 and team_score2[1] == 4:
                file_name.write("볼!\n")
                file_name.write("안타! 다음 타자가 타석에 입장했습니다.\n")       
                team_score2[2] += 1
                team_score2[0] = 0
                team_score2[1] = 0
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
                player_cnt2 += 1
                if player_cnt2 == 10:
                    player_cnt2 = 1                
            elif action2 == 2:
                file_name.write("안타! 다음 타자가 타석에 입장했습니다.\n")
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
                team_score2[0] = 0
                team_score2[1] = 0
                player_cnt2 += 1
                if player_cnt2 == 10:
                    player_cnt2 = 1
            elif action2 == 3 and team_score2[3] < 3:
                file_name.write("아웃!\n")
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
                player_cnt2 += 1
                if player_cnt2 == 10:
                    player_cnt2 = 1
            elif action2 == 3 and team_score2[3] == 3:
                file_name.write("아웃!\n")
                team_score2[0] = 0
                team_score2[1] = 0
                file_name.write(str(team_score2[0]) + "S " + str(team_score2[1]) + "B " + str(team_score2[3]) + "Out\n")
                file_name.write("\n")
                player_cnt2 += 1
                if player_cnt2 == 10:
                    player_cnt2 = 1
                break
        
    file_name.write("경기 종료\n")
    file_name.write("\n")
    file_name.write(team_list[0] + " VS " + team_list[19] + "\n")
    if score_cnt1 == score_cnt2:
        file_name.write("무승부 !\n")
        print("무승부 !\n")
    else:
        file_name.write(str(score_cnt1) + " : "+ str(score_cnt2) + "\n")
        print(str(score_cnt1) + " : "+ str(score_cnt2) + "\n")
    file_name.write("Thank you!\n")

    #스트라이크: (1 - h) / 2 - 0.05
    #볼: (1 - h) / 2 - 0.05
    #안타: h, 0.1 < h < 0.5
    #아웃: 0.1
    
def play_Game(team_list, player_cnt, team_score, top_bottom):
    action = random.randrange(0, 1000)
    if top_bottom == 1:
        h = float(team_list[2*player_cnt])
    elif top_bottom == 2:
        h = float(team_list[(2*player_cnt)+19])
        
    if action >= (100 + (h*1000)) + (((1-h)/2 - 0.05)*1000) and action < 1000:
        team_score[0] += 1
        return 0
    elif action >= 100 + (h*1000) and action < (100 + (h*1000)) + (((1-h)/2 - 0.05)*1000):
        team_score[1] += 1
        return 1
    elif action >= 100 and action < 100 + (h*1000):
        team_score[2] += 1
        return 2
    elif action >= 0 and action < 100:
        team_score[3] += 1
        return 3

sim = []
sim2 = []

while(True):
    print("신나는 야구시합")
    print("1. 데이터 입력")
    print("2. 데이터 출력")
    print("3. 시합 시작")
    print("4. 종료")
    print()
    
    num = int(input("메뉴선택 (1-4) "))

    if num == 1:
        tmp = open_File('baseball.txt', 'wt')
        write_File(tmp)
        close_File(tmp)
    elif num == 2:
        tmp = open_File('baseball.txt', 'rt')
        read_File(tmp)
        close_File(tmp)
    elif num == 3:
        tmp = open_File('baseball.txt', 'rt')
        sim = file_Split(tmp)
        close_File(tmp)
        sim2 = data_Split(sim)
        tmp = open_File('simulation.txt', 'wt')
        sim_File(tmp, sim2)
        close_File(tmp)
    elif num == 4:
        break
    else:
        print("1~4만 선택 해주세요")
    
