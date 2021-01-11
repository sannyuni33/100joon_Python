n = int(input())

matrix = [[0]*10 for i in range(n)]
matrix[0] = [1 for i in range(10)]

for i in range(1, n):
    sum = 0
    for j in range(10):
        for k in range(j+1):
            matrix[i][j] += matrix[i-1][k]
            sum += matrix[i-1][k]

if n == 1:
    print(10)
else:
    print(sum % 10007)


# n = int(input())
# dp = [10, 55]  # 두 번째 요소까지는 점화식 공식을 따르지 않음
# toSubtract = [10-i for i in range(9)]
# print(toSubtract)
# for _ in range(n-2):
#     tdp = dp[-1]
#     res = tdp  # 이전 DP 값 먼저 더하고
#     for i in range(10):
#         tdp -= toSubtract[i]
#         res += tdp  # 하나씩 뺀 값도 결과값에 더한다
#         toSubtract[i] = tdp
# n은 자릿수, 한 자리에 올 수 있는 수는 0~9 로 10가지
# 1번 숫자부터 n번 숫자까지 있다고 한다면,
# 1번 숫자가 무엇인지에 따라 2번, 3번, ... n번에 올 수 있는 수의 가짓수가 달라지니까
# DP를 써서 풀어야하는 문제임.

