n = int(input())
costList = []
for _ in range(n):
    r, g, b = map(int, input().split())
    costList.append([r, g, b])

init = [costList[0][1]+costList[1][0], costList[0][0]+costList[1][1],
        costList[0][0]+costList[1][2], costList[0][2]+costList[1][0],
        costList[0][2]+costList[1][1], costList[0][1]+costList[1][2]]

dp = [min(init)]
lastColor = init.index(min(init)) % 3

print('초기값:', dp[0], lastColor)

if n > 2:
    for i in range(2, n):
        if lastColor == 0:  # 이전집이 빨간색
            if dp[-1] + costList[i][1] < dp[-1] + costList[i][2]:
                tmp = dp[-1] + costList[i][1]
                lastColor = 1
            else:
                tmp = dp[-1] + costList[i][2]
                lastColor = 2

        elif lastColor == 1:  # 이전집이 초록색
            if dp[-1] + costList[i][0] < dp[-1] + costList[i][2]:
                tmp = dp[-1] + costList[i][0]
                lastColor = 0
            else:
                tmp = dp[-1] + costList[i][2]
                lastColor = 2

        elif lastColor == 2:  # 이전집이 파란색
            if dp[-1] + costList[i][0] < dp[-1] + costList[i][1]:
                tmp = dp[-1] + costList[i][0]
                lastColor = 0
            else:
                tmp = dp[-1] + costList[i][1]
                lastColor = 1
        print(i+1, '번째 집까지:', tmp, lastColor)
        dp.append(tmp)

print(dp[-1])
# 몇 번 집까지 칠했을때 최솟값을 구하고, 거기에 차근차근 더하기
# 역시 DP 문제
# 생각해야할 부분은 양 옆 집과 색깔이 같으면 안된다는 것

# 초기값을 잘못해줬남.
# 1번 2번 집을 가지고 초기값을 정하는 경우의 수는 6가지
#