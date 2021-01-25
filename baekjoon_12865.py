n, k = map(int, input().split())
items = []
dp = [[0 for _ in range(k+1)]]
for _ in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

# 알고리즘 수업시간에 배낭 알고리즘 배웠었는디 ...
# k 라는 무게 내에서 가치합의 최댓값을 구한다는점에서 이전 DP 문제랑은 살짝 다름
# 이 물건을 선택하는 경우와 선택안하는 경우로 나눌까
# n == 100이면 2**100의 경우의 수 ... 노답

# 그게 아님. 0/1 배낭 문제에 대해 공부하고 다시 생각할 것
#