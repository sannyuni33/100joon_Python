n = int(input())
heights = []
highest, res = 0, 0


def DFS(x, y, lst, h):
    print('start DFS')
    stack = [[x, y]]
    x = [1, 0, -1, 0]  # 우 하 좌 상 순서
    y = [0, -1, 0, 1]

    while len(stack) > 0:  # 스택이 안비니까 무한루프겠쥬?
        t = stack.pop()
        visited[t[0]][t[1]] = True
        print('searching four direction')
        for i in range(4):
            if 0 <= t[0]+x[i] < n and 0 <= t[1]+y[i] < n:  # 그래프 범위 안일때
                if lst[t[0]+x[i]][t[1]+y[i]] > h and not visited[t[0]+x[i]][t[1]+y[i]]:  # 물에 잠기지 않은 곳
                    stack.append([t[0]+x[i], t[1]+y[i]])
                else:  # 물에 잠긴곳
                    visited[t[0] + x[i]][t[1] + y[i]] = True


for _ in range(n):
    h = list(map(int, input().split()))
    heights.append(h)
    if max(h) > highest:
        highest = max(h)

for h in range(1, highest):
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