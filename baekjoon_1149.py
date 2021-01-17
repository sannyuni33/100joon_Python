# n = int(input())
# costList = []
# for _ in range(n):
#     r, g, b = map(int, input().split())
#     costList.append([r, g, b])
#
# init = [costList[0][1]+costList[1][0], costList[0][0]+costList[1][1],
#         costList[0][0]+costList[1][2], costList[0][2]+costList[1][0],
#         costList[0][2]+costList[1][1], costList[0][1]+costList[1][2]]
#
# dp = [min(init)]
# lastColor = init.index(min(init)) % 3
#
# print('초기값:', dp[0], lastColor)
#
# if n > 2:
#     for i in range(2, n):
#         if lastColor == 0:  # 이전집이 빨간색
#             if dp[-1] + costList[i][1] < dp[-1] + costList[i][2]:
#                 tmp = dp[-1] + costList[i][1]
#                 lastColor = 1
#             else:
#                 tmp = dp[-1] + costList[i][2]
#                 lastColor = 2
#
#         elif lastColor == 1:  # 이전집이 초록색
#             if dp[-1] + costList[i][0] < dp[-1] + costList[i][2]:
#                 tmp = dp[-1] + costList[i][0]
#                 lastColor = 0
#             else:
#                 tmp = dp[-1] + costList[i][2]
#                 lastColor = 2
#
#         elif lastColor == 2:  # 이전집이 파란색
#             if dp[-1] + costList[i][0] < dp[-1] + costList[i][1]:
#                 tmp = dp[-1] + costList[i][0]
#                 lastColor = 0
#             else:
#                 tmp = dp[-1] + costList[i][1]
#                 lastColor = 1
#         print(i+1, '번째 집까지:', tmp, lastColor)
#         dp.append(tmp)
#
# print(dp[-1])

# 몇 번 집까지 칠했을때 최솟값을 구하고, 거기에 차근차근 더하기
# 역시 DP 문제
# 생각해야할 부분은 양 옆 집과 색깔이 같으면 안된다는 것

# 초기값을 잘못해줬남.
# 1번 2번 집을 가지고 초기값을 정하는 경우의 수는 6가지

# 5
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3
# 이런 입력이 들어오면 정답은 1+2+1+2+1 = 7 이지만
# 2+1+2+1+2=8이 정답으로 나오고, 그 이유는 맨 처음 두 집의 최소값을
# 정할때 2+1이 1+2 보다 앞 인덱스에 있어서 그렇게 됨.
# index(min()) 말고 다른 방법으로 최솟값을 찾아야 하지 싶음

# n번째 집을 이 색깔로 칠했을 때 비용이 얼마냐를 구하면?
# n번째 집을 빨강으로 칠하면 이전에 초록, 파랑으로 칠한것중 적은값과 더하기
# 초록, 파랑도 마찬가지. (자신과 다른색깔로 칠한것중 최소값)
# 일단 다 구한다음에 최소를 찾으니까 위에 코드랑을 확실히 다름

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))