# 코드스쿼드 온라인 문제 Step-1

## 1단계 : 간단 야구 게임 구현하기

## 1단계 클린 코딩
    * 함수 기반으로 구현
    * 함수의 이름, 매개변수, 반환 값을 고려
    
## 요구사항

#### (1) 게임이 시작되면 "첫 번째 타자가 타석에 입장했습니다." 메시지와 함께 경기를 진행한다.
    * 첫 번째 요구사항 def **game_Start()** 함수 구현
	<pre>
	def game_Start():
	print("신나는 야구 게임!")
	print("첫 번째 타자가 타석에 입장했습니다.")
	print()
	</pre>
    
#### (2) 경기가 진행되면 랜덤하게 스트라이크 / 볼 / 안타 / 아웃 네 가지 중 한 결과가 출력된다.
    * 두 번째 요구사항 def **play_Game()** 함수 구현
    <pre>
    import random
    
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
    </pre>
    0, 1, 2, 3 4개의 랜덤 숫자를 이용해 스트라이크/ 볼/ 안타/ 아웃 4가지 Action을 구현
    
    * 출력 하는 def ** play_Check()** 함수 구현
    <pre>
    def play_Check(check):
    if check == 0:
        print("스트라이크!")
    elif check == 1:
        print("볼!")
    elif check == 2:
        print("안타! 다음 타자가 타석에 입장했습니다.")
    elif check == 3:
        print("아웃! 다음 타자가 타석에 입장했습니다.")
    </pre>
    play_Game()에서 랜덤한 4가지 중 1개를 check 변수에 받아와 값 비교
    
#### (3) (2)의 결과의 아래 줄에 누적된 스트라이크(S), 볼(B), 아웃(O) 상황을 출력한다.
    * 세 번째 요구사항 def **play_Show()** 함수 구현
    <pre>
    def play_Show(action_list):
    print(str(action_list[0]) + "S " + str(action_list[1]) + "B " + str(action_list[2]) + "H " + str(action_list[3]) + "Out ")
    print("")
    </pre>
    현재 볼 카운트 상황을 담은 action_list를 이용하여 출력
    
#### (4) 스트라이크가 3회 누적되면 1 아웃이다.
    * 네 번째 요구사항 def **play_Check()** 함수 수정
    <pre>
    def play_Check(action_list, check):
    if check == 0 and action_list[0] <3:
        print("스트라이크!")
        return 0
    elif check == 0 and action_list[0] == 3:
        print("스트라이크!")
        print("아웃! 다음 타자가 타석에 입장했습니다.")
        action_list[3] += 1                                 #3스트 1아웃 추가
        return 3
    </pre>
    현재 볼 카운트 상황을 담은 action_list와 play_Game()에서 랜덤한 4가지 중 1개를 받아온 check를 이용해
    3스트라이크 누적되면 1아웃 구현
    
#### (5) 볼이 4회 누적되면 1 안타가 된다.
    * 다섯 번째 요구사항 def **play_Check()** 함수 수정
    <pre>
    def play_Check(action_list, check):
    elif check == 1 and action_list[1] < 4:
        print("볼!")
        return 1
    elif check == 1 and action_list[1] == 4:
        print("볼!")
        print("안타! 다음 타자가 타석에 입장했습니다.")
        action_list[check+1] += 1                           #4볼 1안타 추가
        return 2
    </pre>
    현재 볼 카운트 상황을 담은 action_list와 play_Game()에서 랜덤한 4가지 중 1개를 받아온 check를 이용해
    4볼 누적되면 1안타 구현
    
#### (6) (4)와 (5)의 경우를 포함한 안타 또는 아웃의 경우 "다음 타자가 타석에 입장했습니다." 메시지와 함께 경기가 이어진다.
    * 여섯 번째 요구사항 def **play_Check()** 함수 수정
    <pre>
    print("아웃! 다음 타자가 타석에 입장했습니다.")     # 3스트라이크 시 다음 타자 입장
    print("안타! 다음 타자가 타석에 입장했습니다.")     # 4볼 시 다음 타자 입장
    </pre>
    play_Check()함수에 추가하여 구현
    
#### (7) 다음 타자의 차례에서 현재의 안타, 아웃 카운트는 유지되고, 스트라이크와 볼 카운트는 초기화된다.
    * 일곱 번째 요구사항 def **play_Init()** 함수 구현
    <pre>
    def play_Init(action_list):
    action_list[0] = 0
    action_list[1] = 0
    </pre>
    현재 볼 카운트 상황을 담은 action_list의 [0]번, [1]번 인덱스 값을 0으로 초기화
    
#### (8) 3 아웃이 될 경우 전체 안타수를 출력하고 경기가 종료된다.
    * 여덟 번째 요구사항 def **play_Finish()** 함수 구현
    <pre>
    def play_Finish(action_list):
    print("최종 안타수: " + str(action_list[2]))
    print("GAME OVER")
    </pre>
    현재 볼 카운트 상황을 담은 action_list의 안타가 담겨 있는 [2]번 인덱스 값을 출력