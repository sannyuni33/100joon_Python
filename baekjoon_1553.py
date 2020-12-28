mat = []
for _ in range(8):
    row = list(map(int, input()))
    mat.append(row)


# 7X8 격자를 1X2 도미노로 채우는 방법의 수를 센다...
# 도미노는 회전할 수 있고 ... 한 번 사용된 도미노는 사용 불가..
#