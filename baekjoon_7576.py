x, y = map(int, input().split())
tomatoBox = []
for _ in range(y):
    tomatoBox.append(list(map(int, input().split())))

firstQ = []
secondQ = []
res = 0
for i in range(y):
    for j in range(x):
        if tomatoBox[i][j] == 1:
            firstQ.append([i, j])

while True:
    while firstQ:
        t = firstQ.pop(0)
        toFind = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우

        if t[0] == 0:
            toFind.remove([-1, 0])
        elif t[0] == y-1:
            toFind.remove([1, 0])

        if t[1] == 0:
            toFind.remove([0, -1])
        elif t[1] == x-1:
            toFind.remove([0, 1])

        while toFind:
            f = toFind.pop(0)
            if tomatoBox[t[0]+f[0]][t[1]+f[1]] == 0:
                tomatoBox[t[0]+f[0]][t[1]+f[1]] = 1
                secondQ.append([t[0]+f[0], t[1]+f[1]])

    if not secondQ:
        break
    else:
        firstQ, secondQ = secondQ, firstQ  # 두 개의 큐를 맞바꿔서 다음 큐를 쓰도록 함
        res += 1

for x in tomatoBox:
    if 0 in x:
        print(-1)
        exit()
print(res)

# 이 문제의 알고리즘 분류에는 BFS 가 있음. 요걸 참조해보자
# 이중 for 문을 돌다가 1을 발견하면 BFS 를 수행..
# 근데 1이 여러군데 있을 수 있는데 맨 처음 나온 1에서 BFS 를 한 번 해서 끝내면 X

# '1일이 지나는 상황' 을 구현해야 할 듯
# 이거를 구현해놓고 while 반목문을 돌림.
# 한 번 돌때마다 결과값을 1씩 더해준다.
# 근데 while 문이 끝나고 나서도 tomatoBox 에 0 이 남아있다면 결과값은 -1 이 된다.
