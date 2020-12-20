n = int(input())
wines = []
dp = []
for _ in range(n):
    wines.append(int(input()))

if n > 3:
    dp.append(wines[0])
    dp.append(wines[0]+wines[1])
    dp.append(max([wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2]]))
    # 여기에 끝날때까지 점화식
    for i in range(3, n):
        dp.append(max([dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i]]))
    print(dp[-1])
elif n == 3:
    print(max([wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2]]))
elif n == 2:
    print(wines[0]+wines[1])
else:
    print(wines[0])

# result = wines[0] if wines[0] > wines[1] else wines[1]
# 1번 2번 중 더 큰넘을 시작값으로 놓고 시시시시작
# 1번 2번 둘 다 안 마시는 일은 없음. 3번부터 마시면 1번도 마시는게 최대니깐요
# 아니다 그렇게하고 점화식 설계해서 풀면 2번이 더 클 때 1번은 아예 포함안됨.
# 근데 예제입력만 봐도 1번 2번을 둘 다 더했음.
# 그러면 아예 처음부터 2~3개 포도주를 더한 값을 시작값으로 해야할듯.
# 어떤 알고리즘으로 1번 2번 포도주를 선택했을까요
# 세 포도주 중 두 개를 고르지말고 네 포도주 중 세 개를 고르는 방식을 택하면
# 1, 2, 3, 4 번 포도주를 놓고 적용시켰을때 1+2+4 혹은 1+3+4 두 가지 선택지만 나옴.
# 두 선택지 중 하나를 고른다치면, 다음에는 몇 번 포도주가 1번의 역할을 해야할지 결정.
# 근데 그렇게 해도 예제로 치면 1 3 4 를 골라야하는데 답은 1 2 4 를 고르는 경우임
# 계단 오르기는 마지막 계단을 밟아야한다는 조건이 있었는데
# 이건 없으니까 더 어렵넹
# 세 개 중에서는 무조건 두 개(1+2, 1+3, 2+3)를 고르는데,,
# 이 기준을 찾아보는게 맞을듯 싶음
# 이 세 개만 보고서 찾는 건 무조건 아니고 네 번째꺼, 다섯 번째꺼까지 봐야하나

# 그게 아니라 DP 쓰는 법을 제대로 이해못하고 있었던거네
#