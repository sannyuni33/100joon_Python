class turtle:
    def __init__(self):
        self.spot = [0, 0]  # x 축, y 축
        self.dirQ = ['up', 'right', 'down', 'left']  # 방향 표시 큐
        self.xTrack = [0]
        self.yTrack = [0]

    def move(self, direction, fb):  # 방향은 네 방향, 전진, 후진 있으니까
        if direction == 'up':
            self.spot[1] += fb
        elif direction == 'right':
            self.spot[0] += fb
        elif direction == 'down':
            self.spot[1] += -fb  # 방향이 아래인데, B 들어오면 위로 가니까
        elif direction == 'left':
            self.spot[0] += -fb  # 방향이 왼쪽일때도 마찬가지
        print('거북이 현 위치:', self.spot)
        self.xTrack.append(self.spot[0])
        self.yTrack.append(self.spot[1])

    def turnRight(self):
        tmp = self.dirQ.pop(0)
        self.dirQ.append(tmp)

    def turnLeft(self):
        tmp = self.dirQ.pop()
        self.dirQ.insert(0, tmp)


t = int(input())
res = []
for _ in range(t):
    tt = turtle()
    path = input()
    for x in path:
        if x == 'F':
            print('go forward')
            tt.move(tt.dirQ[0], 1)
        elif x == 'R':
            print('turn right')
            tt.turnRight()
        elif x == 'L':
            print('turn left')
            tt.turnLeft()
        elif x == 'B':
            print('go backward')
            tt.move(tt.dirQ[0], -1)
    base = [min(tt.xTrack), max(tt.xTrack)]
    height = [min(tt.yTrack), max(tt.yTrack)]
    res.append((base[1]-base[0])*(height[1]-height[0]))

for r in res:
    print(r)

# 경로를 포함할 수 있는 가장 작은 직사각형...
# x 축 이동 경로, y 축 이동 경로로 해서 직사각형의 밑변, 높이 길이를 구해주면 되겠다.
# 다만 음수방향으로 진행한 경로와 양수방향으로 진행한 경로가 공존할 수 있으니
# 그 부분을 어떻게 계산해야할지 고민해야함.

# F로 갔던경로를 B로 빠꾸한다고 해서 경로가 지워지진 않음(예제 입력3)

# 약 30분 고민 후 각 사분면에서의 가로방향 max 값과 세로방향 max 값을 구하고
# 반대되는 사분면의 max 값과 더해줘서 직사각형의 밑변과 높이를 구하면 어떨까라는 생각이 듦.
# 그렇게하면 거북이가 지금 어느 사분면에 위치하는지의 데이터가 필요함

# 사분면을 나눌것도 없이
# 그냥 x y 축 각각의 max 값 min 값을 가지고 밑변 높이 길이를 구하는게 더 간결할 듯.
# 전략은 이렇게 세우고, 그럼 x y 축 각각의 max 값 min 값 구하려면 뭐가 필요한지 생각

# 거북이의 현재 좌표와 방향 필요, 클래스를 만들자

# 2064ms 로 맞긴했는데, 더 효율적으로 만들수는 없을까?