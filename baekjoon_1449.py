n, l = map(int, input().split())
leakPoint = list(map(int, input().split()))
leakPoint.sort()
res = 0

for y in leakPoint:
    for i in range(1, l):
        if y+i in leakPoint:
            leakPoint.remove(y+i)
            print(y+i, '있어서 빼뻐린다!')
    res += 1
    print(leakPoint)
print(res)
# 새는 곳이 1 2 100 101 이라면
# 커버해야하는 곳은 0.5 ~ 1.5 / 1.5 ~ 2.5 / 99.5 ~ 100.5 / 100.5 ~ 101.5
# 이렇게 나오고 테이프 길이가 4라면 0.5 ~ 2.5 / 99.5 ~ 101.5 를 카바가능. 2개필요
# 너무 복잡하게 생각하지 말고 길이가 n이면 연속한 n개의 새는 곳을 막는다고 생각하자

# 아놔. 리스트 입력받고 소팅해주니까 맞다네 이런...............