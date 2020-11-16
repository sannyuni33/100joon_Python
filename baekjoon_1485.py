def isSquare():
    testCase = []
    for _ in range(4):
        x, y = map(int, input().split())
        testCase.append([x, y])

    disList = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(((testCase[i][0]-testCase[j][0])**2)+((testCase[i][1]-testCase[j][1])**2))
        temp.sort()
        if not (temp[0] < temp[1] == temp[2] < temp[3]):  # 정사각형 모양이어야 함
            return False
        else:
            disList.append(temp)

    std = disList[0]
    for k in range(1, 3):  # 모든 점이 다른 점까지 가는 거리의 리스트가 같아야 함
        if disList[k] != std:
            return False
    return True


t = int(input())
res = []
for _ in range(t):
    res.append(1) if isSquare() else res.append(0)
for r in res:
    print(r)

# 이미 찍힌 네 개의 점 갖고 정사각형 여부를 판단하기보다
# 점이 들어올때마다 체크를 해주는게 어떤가 싶은디

# 두 번째 점까지는 어떤식으로 들어오든 정사각형을 만들 수 있음
# 세 번째 점부터 삐끗하면 정사각형 만들기 불가.
# 세 번째까지 이쁘게 들어왔어도 네 번째 삐끗하면 NG
# 이걸 생각하면서 코드를 짜면 되려나
# 그럼 세 번째 점이 어떻게 찍히면 삐끗인가... 생각을 해보니

# 잠깐잠깐 근데 이거 마름모나 회전된 형태도 인식을 해야하는건가?
# 위에 생각했던 알고리즘으로 판별하면 ㅁ 모양 정사각형만 인식 가능
# (0, 1), (2, 0), (1, 3), (3, 2) 같은 정사각형이 들어오면 인식 불가능

# 진짜 수학계산을 구현해야 될 것 같은데
# 벡터 사용? 아니면 x, y의 델타값 사용?
# 델타 값을 사용하자니, 또 점의 순서가 정해져 있지 않기 때문에 빡셈.
# 벡터를 써서 한 점과 나머지 세 점까지의 거리를 각각 비교.
# 정사각형이라고 한다면 이웃한 두 점과의 거리는 같고, 대각에 위치한 점의 거리는 좀 더 길거임.
# 이 세 거리를 가지고 있는 리스트를 정렬하고, 나머지 점에 대해서도 같은 과정을 반복.
# 이 세 개의 리스트가 모두 똑같아야지 정사각형임.

# 기울여진것까지 계산 좋게 되는데,
# 뭐가 틀렸을까...
# 의심되는 부분은 점끼리 계산을 하면서 제곱근 처리 안한거.
# 어차피 제곱근 안해도 값은 똑같으니까 안한건데,,, 문제가 될 수 있을래나
# 음수 들어간거 해도 제대로 나오고,,

# 정사각형이 아닌데도 길이리스트가 다들 같을 수 있나..
# 같은 점만 네 번 들어오면 그러겠네 가 아니라 같은 점은 두 번 이상 안나온다네
# 아니 잠만 직사각형이 그러나?
# 그러네...............................................................
# 그러면 정렬했을때 두 세 번째가 같아야한다는 조건을 넣어주면 될 듯
# 첫 번째 < 두 번째 == 세 번째 < 네 번째 이러면 되겠다

# 시간은 244 ms 걸렸고 ..