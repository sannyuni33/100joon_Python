while 1:
    res = 0
    x, y = map(int, input().split())
    if x == y == 0:
        break
    matrix = [list(map(int, input().split())) for i in range(y)]
    checkMat = [[0 for _ in range(x)] for _ in range(y)]  # 카운팅이 된 땅인지 아닌지를 판단

    print(matrix)

    for i in range(x):
        for j in range(y):
            if matrix[j][i] and not checkMat[j][i]:
                #  여기서 bfs 돌리고, res +=1
                print(i, j, "체크함요")

# BFS 를 써서 푸는 문제.
# 0, 0 인덱스부터 시작해서 1인 놈을 찾으면 bfs 돌리고, 끝나면 섬의 개수를 1 카운트.
# 섬 하나 찾고나서 두 번째 섬 찾으려고 할 때
# 첫 번째 섬에 포함된 땅이면 안될 것임. 얘를 체크해줄 수단이 필요.
#