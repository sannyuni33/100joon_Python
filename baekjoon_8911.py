t = int(input())
paths, res = [], []
for _ in range(t):
    paths.append(input())


# 경로를 포함할 수 있는 가장 작은 직사각형...
# x 축 이동 경로, y 축 이동 경로로 해서 직사각형의 밑변, 높이 길이를 구해주면 되겠다.
# 다만 음수방향으로 진행한 경로와 양수방향으로 진행한 경로가 공존할 수 있으니
# 그 부분을 어떻게 계산해야할지 고민해야함.
#