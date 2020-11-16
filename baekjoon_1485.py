t = int(input())
res = []
for _ in range(t):
    testCase = []
    for _ in range(4):
        x, y = map(int, input().split())
        testCase.append([x, y])
    print(testCase)
    # 여기서부터 바로 정사각형인지 아닌지의 여부를 판단해버리자~!

    # for t in testCase:




    isSquare = 1
    res.append(1) if isSquare == 1 else res.append(0)

for x in res:
    print(x)

# 이미 찍힌 네 개의 점 갖고 정사각형 여부를 판단하기보다
# 점이 들어올때마다 체크를 해주는게 어떤가 싶은디

# 두 번째 점까지는 어떤식으로 들어오든 정사각형을 만들 수 있음
# 세 번째 점부터 삐끗하면 정사각형 만들기 불가.
# 세 번째까지 이쁘게 들어왔어도 네 번째 삐끗하면 NG
# 이걸 생각하면서 코드를 짜면 되려나
# 그럼 세 번째 점이 어떻게 찍히면 삐끗인가... 생각을 해보니
#