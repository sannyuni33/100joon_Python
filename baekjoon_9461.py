t = int(input())
res = []
for _ in range(t):
    DP = [1, 1, 1, 2, 2]
    n = int(input())
    if n < 6:
        res.append(DP[n-1])
    else:
        for i in range(n-5):
            DP.append(DP[-1]+DP[-5])
        res.append(DP[-1])
for x in res:
    print(x)

# 이것도 그냥 규칙성 찾아서 점화식 세우는 문제. 1, 2, 3 더하기랑 완전 똑같다!