import os

def open_File(file_name, format):
    file = open(file_name, format, encoding = 'UTF-8')
    return file

def close_File(file_name):
    file_name.close()

def write_File(file_name):
    for i in range(0, 20):
        if i == 0:
            text = input(str(i+1) + "팀의 이름을 입력하세요> ")
            file.write(text + " 팀 정보\n")
        elif i < 10:
            text = input(str(i) + "번 타자 정보 입력> ")
            file.write(str(i) + "번 " + text + "\n")
        elif i == 10:
            text = input(str(i-8) + "팀의 이름을 입력하세요> ")
            file.write(text + " 팀 정보\n")
        else:
            text = input(str(i-10) + "번 타자 정보 입력> ")
            file.write(str(i-10) + "번 " + text + "\n")
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

def game_Sim(file_name):
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
        sim = game_Sim(tmp)
        close_File(tmp)
        sim2 = data_Split(sim)
        print(sim2)
    elif num == 4:
        break
    else:
        print("1~4만 선택 해주세요")
    
