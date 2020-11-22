heightOfStair = int(input())
stairs = []
res = 0

for _ in range(heightOfStair):
    stairs.append(int(input()))

temp = len(stairs)-1  # 몇 번째 계단?
n = stairs[temp]  # 그 계단의 점수는?
isTriple = 1
while temp > 0:
    res += n
    print(n, '더함요')
    if stairs[temp-1] > stairs[temp-2] and isTriple != 2:
        temp -= 1
        isTriple += 1
    else:
        temp -= 2
        isTriple = 1
    n = stairs[temp]

if isTriple != 2:
    res += stairs[0]
    print(stairs[0], '더함요')
print(res)


# 우리가 궁금한건 최고점수. 이걸 알려면 뭘로 접근하는게 좋을깝슈
# 계단을 오르는 방법의 모든 경우의 수는 당연히 구할 수 없고...
# 맨 마지막 계단부터 다 밟았다고 생각하고
# 계단 오르기 법칙에 맞게 한 계단씩 빼주는데,
# 가장 낮은 애를 빼주면 되지 않나 싶네

# temp = temp-1 if stairs[temp-1] > stairs[temp-2] else temp-2 로 더해가는데,
# 연속된 세 계단이 더해지지 않게끔 조치를 먼저 취한다음에

# temp 가 2일때부터 고려를 해주어야 할 것 같다
# temp 가 2가 됐으면, 정상적으로 1이랑 0중에 고르면 됨
# temp 가 1이 됐으면, 3계단 연속이 아닌 경우에만 0을 데려올 수 있음

# 바로 풀리지는 않넴

# 계단을 오를 수 있는 패턴이 그러게 많지 않음
# 그 패턴중 가장 높은 점수를 갖는 것을 택해서 더한다... .라는 방식으로 접근해서 다시 시도 ㄱㄱ