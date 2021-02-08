def BFS(mat):
    queue, visited = [], [[False for _ in range(m)] for _ in range(n)]
    x, y = [0, 1, 0, -1], [1, 0, -1, 0]
    queue.append([0, 0])
    visited[0][0], phase = True, 1

    while len(queue) > 0:
        tmp = queue.pop(0)
        row, col = tmp[0], tmp[1]
        for i in range(4):
            tmpX, tmpY = row+x[i], col+y[i]
            if 0 <= tmpX < n and 0 <= tmpY < m and not visited[tmpX][tmpY] and int(mat[tmpX][tmpY]):
                queue.append([tmpX, tmpY])
                visited[tmpX][tmpY] = True

    print(phase)


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
ans = 0


print(matrix)
BFS(matrix)
# BFS 를 돌리고 한 칸 이동할때마다 1 더하기. n, m 도달할때까지
# 네 방향 모두 이동 가능해야 함. 꼬불꼬불 미로일수도 있으니깐
# BFS 로 쭈우우우욱 탐색을 하다가 다음에 (N, M)이 들어올 예정이면 마무리

