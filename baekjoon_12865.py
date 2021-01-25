n, k = map(int, input().split())
items = []
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if items[i-1][0] <= j:
            dp[i][j] = max(items[i-1][1]+dp[i-1][j-items[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
# 알고리즘 수업시간에 배낭 알고리즘 배웠었는디 ...
# k 라는 무게 내에서 가치합의 최댓값을 구한다는점에서 이전 DP 문제랑은 살짝 다름
# 이 물건을 선택하는 경우와 선택안하는 경우로 나눌까
# n == 100이면 2**100의 경우의 수 ... 노답

# 그게 아님. 0/1 배낭 문제에 대해 공부하고 다시 생각할 것
# 0/1 배낭 문제 알고리즘 적용한 코드는... 7632 ms