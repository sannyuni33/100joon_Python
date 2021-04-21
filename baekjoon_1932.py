n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

if n == 1:
    print(tri[0][0])
elif n == 2:
    print(tri[0][0]+max(tri[1]))
else:
    rTri = [tri[0]]
    for i in range(1, n):  # 여긴 행부분이니까 건들지말고
        tmp = [tri[i][0] + rTri[i - 1][0]]  # 각 행의 0번째 요소 추가
        for j in range(i - 1):  # 각 행의 가운데 요소 추가
            tmp.append(tri[i][j+1] + max(rTri[i-1][j], rTri[i-1][j+1]))
        tmp.append(tri[i][-1] + rTri[i-1][-1])  # 각 행의 마지막 요소 추가
        rTri.append(tmp)  # 그 행을 DP 삼각형에 추가
    print(max(rTri[-1]))
    
# n 행의 0번째 요소 -> tri[n][0] + rTri[n-1][0]
# n 행의 -1번째 요소 -> tri[n][-1] + rTri[n-1][-1]
# 그 외 나머지 -> tri[n][n+1] + max(tRti[n-1][n], tRti[n-1][n+1])