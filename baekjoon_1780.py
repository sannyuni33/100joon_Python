def paperDQ(nn, pp):
    print(nn, '길이 정사각형')
    print(pp)
    tmp = pp[0][0]
    if nn == 1:
        if tmp == -1:
            res[0] += 1
        elif tmp == 0:
            res[1] += 1
        else:
            res[2] += 1
        return

    flag = False

    for i in range(len(pp)):
        for j in range(i):
            if pp[i][j] != tmp:  # 반동분자 하나라도 나오면 종이를 9조각으로 쪼개야함.
                flag = True

    if flag:
        for y in range(0, nn, nn // 3):
            for x in range(0, nn, nn // 3):
                smallPaper = []
                for z in range(nn // 3):
                    smallPaper.append(pp[y + z][x:x + (nn // 3)])
                paperDQ(nn // 3, smallPaper)

    else:
        # 이중 for 문에서 한번도 안걸리는건 모두 다 같은 숫자라는 의미. 그만 나누자
        if tmp == -1:
            res[0] += 1
        elif tmp == 0:
            res[1] += 1
        else:
            res[2] += 1


res = [0, 0, 0]  # -1종이, 0종이, 1종이 갯수
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

paperDQ(n, paper)

for r in res:
    print(r)

# 분할정복은 보통 재귀함수를 통해 구현한다...
# n 과 paper 를 첫 번째 args 로 넣어주고 반동분자를 색출,
# 반동분자가 없다면 리턴.
# 반동분자가 있다면 n/3 과 n/3 길이로 쪼갠 paper 조각을 for 문으로 접근하면서 재귀호출

# 9 길이의 정사각형에서 [0][3] 만 1이고 나머지가 싹 다 0이더라도
# 재귀는 무조건 9번 돌리는게 맞음. (3길이 정사각형 9개를 살펴야함)
#
