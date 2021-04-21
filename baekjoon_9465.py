t = int(input())
res = []
for _ in range(t):
    n = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    if n < 2:
        print(max(row1[0], row2[0]))
        exit()
    DP = [[row1[0], row2[0]+row1[1]], [row2[0], row1[0]+row2[1]]]

    for i in range(2, n):
        DP[0].append(row1[i] + max(DP[1][i-1], DP[1][i-2]))
        DP[1].append(row2[i] + max(DP[0][i-1], DP[0][i-2]))
    res.append(max(DP[0][-1], DP[1][-1]))

for r in res:
    print(r)

# n-1 열에서 1행 스티커를 뜯은 경우, 2행 스티커를 뜯은 경우로 나누고
# n 열과 n+1 열이 어떻게 뜯길 수 있는지 경우를 나눠보자

# ...라고 하기엔 두 칸씩 계산하다보면 인덱스 오류 발생가능성이 있음.
# 한 칸씩 진출하다가 특수한 경우에 이전스티커를 다시 붙이는(점수를 빼는)식으로 접근

# 할려고 하다가 그냥 두 칸씩 진행하고 한 칸 남았을때를 따로 처리해주는 식으로 1차시도 ㄱ
# 로 했더니 실패.
# if row1[0] >= row2[0]:
#     ans = row1[0]
#     flag = 'U'
# else:
#     ans = row2[0]
#     flag = 'D'
# curr = 0
# while curr + 2 < n:
#     if flag == 'U':
#         if row2[curr+1]+row1[curr+2] >= row2[curr+2]:
#             ans += row2[curr+1]+row1[curr+2]
#         else:
#             ans += row2[curr+2]
#             flag = 'D'
#     else:
#         if row1[curr+1]+row2[curr+2] >= row1[curr+2]:
#             ans += row1[curr+1]+row2[curr+2]
#         else:
#             ans += row1[curr+2]
#             flag = 'D'
#     curr += 2
# if curr < n-1:  # 아직 한 열 남았다(n이 짝수라서)
#     if flag == 'U':
#         ans += row2[-1]
#     else:
#         ans += row1[-1]
# res.append(ans)