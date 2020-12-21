def clock(gear, dir):
    if dir == 1:
        print('Clock')
        tmp = gear.pop(-1)
        gear.insert(0, tmp)
    else:
        print('Reverse')
        tmp = gear.pop(0)
        gear.append(tmp)


def rotate(gear, dir):
    # 여기 필요한거는
    # dir 에 맞춰서 시계방향회전, 반시계방향회전 구현
    # 시계방향은 [7]번째 빼서 [0]으로 붙이고,
    # 반시계방향은 [0]번째 빼서 [7]에 붙이면 됨
    # 맞닿은 이빨끼리 극 다르면 반대회전, 같으면 회전 노노

    # 1번 바퀴는 [2]번째가 2번 바퀴 [6]이랑 맞닿아있고,
    # 2번 바퀴는 [6]번째가 1번 바퀴 [2], [2]번째가 3번 바퀴 [6]이랑 맞닿음.
    # 3번 바퀴는 [6]번째가 2번 바퀴 [2], [2]번째가 4번 바퀴 [6]이랑 맞닿음.
    # 4번 바퀴는 [6]번째가 3번 바퀴 [2]랑 맞닿음.
    # 각 바퀴별로 함수를 따로 정의해주는 방법이 한가지 떠올랐고...
    # 만약 그렇게 안하면 어떻게 구현할까
    # 그냥 인덱스로 접근하면 될래나. 첫 번째 바퀴, 마지막 바퀴, 가운데 바퀴만 구분

    # 재귀함수로 구현한다... 예를 들어 rotate 에 3번 바퀴를 인자로 넣고
    # 톱니의 극을 비교해서 2번 바퀴와 4번 바퀴를 인자로 넣은 rotate 를 호출..
    # 이런 방식을 적용할 때 조심할 점은..
    # 2번 바퀴와 3번 바퀴가 다시 3번 바퀴를 인자로 넣은 rotate 를 호출하면 안됨.
    # 그럼 왼쪽으로 진행되는 반복문과 오른쪽으로 진행되는 반복문을 구현?

    tmpDir = -dir  # 인자로 들어온 바퀴와 반대로 회전해야함
    for i in range(gear, 0, -1):
        print('To the left')
        if gears[i][6] != gears[i-1][2]:  # 오른쪽 6번과 왼쪽 2번 극이 다르면
            clock(gears[i-1], tmpDir)  # 왼쪽을 회전
            tmpDir = -tmpDir  # 다음 왼쪽바퀴가 극이 다를 경우를 위해 회전방향변경
        else:
            break
    for j in range(gear, len(gears)-1):
        print('To the right')
        if gears[j][2] != gears[j+1][6]:  # 왼쪽 2번과 오른쪽 6번 극이 다르면
            clock(gears[j+1], tmpDir)  # 오른쪽을 회전
            tmpDir = -tmpDir  # 다음 왼쪽바퀴가 극이 다를 경우를 위해 회전방향변경
        else:
            break
    clock(gears[gear], dir)

    for x in gears:
        print(x)


gears = []
for _ in range(4):
    gears.append(list(input().strip()))

k = int(input())
for _ in range(k):
    gearNum, direction = map(int, input().split())
    rotate(gearNum-1, direction)

print(int(gears[0][0]) + int(gears[1][0])*2 + int(gears[2][0])*4 + int(gears[3][0])*8)

# 회전하는 모습을 표현하는 함수 rotate 를 정의하면 될래나 싶음
# 각 톱니바퀴의 0 번째가 12시 방향 이빨임
# gearNum 과 direction 을 입력받으면 바로 rotate 함수에 argument 로 입력
# 가장 신경써야할 부분은 바퀴사이의 연쇄작용이지 싶음.
# 1번부터 시작해도 바퀴 극이 다르다면 4번까지 영향이 미침.
# 3번부터 시작하면 왼쪽으로는 2, 1번. 오른쪽으로는 4번.
#