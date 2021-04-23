def solution(brown, yellow):
    answer = []
    xList, yList = [], []
    i = 1
    while True:  # for 문의 범위를 줄여줄 필요가 있삼
        if not yellow % i:  # i 로 나누어 떨어지면
            xList.append(yellow // i)  # 노랑의의 가로 길이 목록에 추가
            yList.append(i)  # 노랑이의 세로 길이 목록 추가
        i += 1
        if yellow // i < i:  # 가로 세로 길이가 같아질때까지만 추가하고, 그 다음부터는 세로가 길어지니까 중단
            break

    print(xList)
    print(yList)

    for i in range(len(xList)):
        if ((xList[i] + 2) * 2) + (yList[i] * 2) == brown:
            answer = [xList[i] + 2, yList[i] + 2]
            break

    return answer

solution(24, 24)

# 가운데의 노란 격자 수가 같아도 여러 형태를 가질 수 있다.
# 가령 yellow 로 60이 입력되면, 1*60, 2*30, 3*20, 4*15, 5*12, 6*10 의 형태가 가능한데
# 이때 brown 으로 가능한 입력은 정해져있다.
# (62*2)+(1*2)
# (32*2)+(2*2)
# (22*2)+(3*2)
# (17*2)+(4*2)
# (14*2)+(5*2)
# (12*2)+(6*2)
# 이렇게 계산해서 나온 수들 중, brown 입력값과 같은 식을 찾는다.
# ((가로+2)*2)+((세로)*2) 꼴로 나오니까, 이때의 가로 세로를 정답으로 리턴하면 되겠따