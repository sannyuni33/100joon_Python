n = int(input())
heights = []
highest, res = 0, 0


def DFS(x, y, lst, h):
    # print('start DFS')
    stack = [[x, y]]
    x = [1, 0, -1, 0]  # 우 하 좌 상 순서
    y = [0, -1, 0, 1]

    while len(stack) > 0:
        t = stack.pop()
        visited[t[0]][t[1]] = True
        for i in range(4):
            if 0 <= t[0]+x[i] < n and 0 <= t[1]+y[i] < n:  # 그래프 범위 안일때
                if lst[t[0]+x[i]][t[1]+y[i]] > h and not visited[t[0]+x[i]][t[1]+y[i]]:  # 물에 잠기지 않은 곳
                    visited[t[0] + x[i]][t[1] + y[i]] = True
                    stack.append([t[0]+x[i], t[1]+y[i]])
                # else:  # 물에 잠긴곳
                #     visited[t[0] + x[i]][t[1] + y[i]] = True


for _ in range(n):
    h = list(map(int, input().split()))
    heights.append(h)
    if max(h) > highest:
        highest = max(h)

for h in range(0, highest):
    numOfSZ = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and heights[i][j] > h:
                DFS(i, j, heights, h)  # 하나의 안전영역 탐색
                numOfSZ += 1
            else:
                visited[i][j] = True  # 방문은 안했지만 잠겼으니까 방문안할꺼
    if res < numOfSZ:
        res = numOfSZ
print(res)

# 81% 퍼에서 틀려버림. 반례가 뭘까아아아요
# 비가 쌓이는 높이를 0부터 시작했더니 맞았음.... 근데 시간이 4828 ms 인데 어케 줄이지?
# 17~18 라인에서 같은 위치가 스택에 여러번 들어가는듯 싶음. 저번에도 이랬는데