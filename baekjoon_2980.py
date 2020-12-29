sig, road = map(int, input().split())
signals = []
for _ in range(sig):
    dis, red, green = map(int, input().split())
    signals.append([dis, red, green])
signals.append([0, 0, 0])

t = signals[0][0]
for i in range(sig):
    tmpT = t  # 이 위치의 신호등 신호 알아낼 때 쓰는 변수
    while tmpT > 0:
        tmpT -= signals[i][1]+signals[i][2]  # 한 싸이클씩 뺌(다시 빨강 시작)
    if tmpT+signals[i][2] < 0:  # 빨간불, 0하고 비교하지 말고 절댓값하고?
        t += -(tmpT+signals[i][2])  # 남은 빨간불 시간만큼 대기
    # else 는 초록불이니까 그냥 가면 됨.
    if signals[i+1][0] == 0:
        break
    else:
        t += signals[i+1][0] - signals[i][0]  # 여태까지 온 시간
t += road - signals[-2][0]
print(t)
# 신호등이 계속해서 빨강, 초록으로 바뀌고 있는것을 어떻게 구현하냐가 문제
# 첫 번째 신호등은 거리가 3. 빨+파 = 10이고, 빼면 -7이 됨.
# 여기서 빨을 더하면 -2.
# 두 번째 신호등은 거리는 5인데 여기까지 오려면 시간이 3+2+2 = 7 걸림.
# while tmpT > 0 으로 싸이클을 계속 빼다보면 -1이 됨.
# 여기다가 빨을 더하면 1
# 실제로 시뮬레이션 하면 첫 번째 신호등에선 빨간불 2초, 두 번째 신호등은 초록불임

# 만약에 첫 번째 신호등이 빨간불 6초, 초록불 4초면 여기서 3초 대기해야함.
# -10은 그대로고 -7에다가 6을 더하면 -1이 되는데, 이걸로 하면 안됨.
# 초록불만큼을 더해야하나?
