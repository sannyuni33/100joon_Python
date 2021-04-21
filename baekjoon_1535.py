n = int(input())
lList = list(map(int, input().split()))
jList = list(map(int, input().split()))

matrix = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(n):  # 행(+2) 및 기쁨
    for j in range(99):  # 열(+3) 및 체력
        if lList[i] <= j+1:
            if jList[i] + matrix[i][j+2-lList[i]] > matrix[i][j+2]:
                matrix[i+1][j+2] = jList[i] + matrix[i][j+2-lList[i]]
            else:
                matrix[i+1][j+2] = matrix[i][j+2]
        else:
            matrix[i + 1][j + 2] = matrix[i][j + 2]
print(matrix[-1][-1])

# 요거는 배낭알고리즘이다. 체력이 무게, 기쁨이 가치라고 생각하면 될듯요.
# 근데 체력이 0이 되면 안된다는게 변수로 작용할래나?
# 배낭 문제로 치면 가방을 꽉채우면 안된다는 뜻이니깐요. 1이 남아있어야 한다는 말?
# 그럼 무게/가치 2차원 배열에서 0열 + 1열도 0으로 채우면 되는거 아이가?

# 맞았당! 76 ms