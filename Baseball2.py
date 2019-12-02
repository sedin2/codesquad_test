import os

def write_File(file_name):
    file = open(file_name, 'wt', encoding = 'UTF-8')
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
    file.close()
    print()
    print("팀 데이터 입력이 완료되었습니다.")
    
def open_File():
    return 1

while(True):
    print("신나는 야구시합")
    print("1. 데이터 입력")
    print("2. 데이터 출력")
    print()
    
    num = int(input("메뉴선택 (1-2) "))

    if num == 1:
        write_File('baseball.txt')
    elif num == 2:
        open_File()
    elif num == 4:
        break
    else:
        print("1 or 2만 선택 해주세요")
    
