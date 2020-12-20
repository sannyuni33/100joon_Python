def isWin(color, x, y):
    if board[x][y+1] == board[x][y+2] == board[x][y+3] == board[x][y+4] == color:
        if board[x][y+5] != color:
            print("→")
            return color, x+1, y+1
    elif board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4] == color:
        if board[x+5][y+5] != color:
            print("↘")
            return color, x+1, y+1
    elif board[x+1][y] == board[x+2][y] == board[x+3][y] == board[x+4][y] == color:
        if board[x+5][y] != color:
            print("↓")
            return color, x+1, y+1
    elif board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3] == board[x+4][y-4] == color:
        if board[x+5][y-5] != color:
            print("↙")
            return color, x+5, y-3
    else:
        return False


board = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if board[i][j] == 1:  # 흑돌을 찾았다
            print("Black stone,", i+1, j+1)
            res = isWin(1, i, j)
            if res:
                print("Black is winner!")
                print(res[0])
                print(res[1], res[2])
                exit()
        elif board[i][j] == 2:  # 백돌을 찾았다
            print("White stone,", i+1, j+1)
            res = isWin(2, i, j)
            if res:
                print("White is winner!")
                print(res[0])
                print(res[1], res[2])
                exit()
print(0)
# 제일 먼저 해야할 일은, 이중 for 문을 돌리면서 1 과 2를 찾는게 첫 순서.
# 흑돌 또는 백돌이 감지되면 얘부터 시작해서 5개가 연속해서 놓였는지의 여부를
# 판단하는 함수를 정의해주면 될 것 같다
# visited 를 쓰면 안될 것 같은게,
# 1 1 1 1
#     1
#     1
#     1
#     1
# 이런애가 있으면, 1 1 1 1 을 방문한걸로 해버리면 세로로 승리한것을 찾을 수 없음


# 6개 이상의 바둑알이 일렬로 놓여있으면 인정하면 안되는데 ...
# 예를들어 8행 3열 부터 -> 방향으로 2 2 2 2 2 2 2 이렇게 백돌이 놓이면
# 8행 3열에서부터 시작된 5개는 인정이 안되지만,
# 8행 5열에서부터 시작된 5개는 인정이 되버림. 8 8 / "8 8 8 8 8" <- 이거
# DFS 를 써야되나. ...............................................
# 