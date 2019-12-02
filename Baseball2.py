
def write_File():
    return 1
def open_File():
    return 1
WW
print("신나는 야구시합")
print("1. 데이터 입력")
print("2. 데이터 출력")
print()

num = int(input("메뉴선택 (1-2) "))

if num == 1:
    write_File()
elif num == 2:
    open_File()
else:
    print("1 or 2만 선택 해주세요")
    
