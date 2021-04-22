n = int(input())
lst = list(map(int, input().split()))
DP = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i] and DP[j] > DP[i]:
            DP[i] = DP[j]
    DP[i] += lst[i]
print(max(DP))

# 가장 긴 증가 부분 수열 문제에서, DP에 길이가 아니라 수열 요소 값을 
# 그대로 가져오는 것만 다르다. 알고리즘은 동일하다. 알고리즘 응용 스킬 활용