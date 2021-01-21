n = int(input())
columns = []
for _ in range(n):
    left, height = map(int, input().split())
    columns.append([left, height])

# 5번 조건인 '오목하게 들어간 부분이 없어야한다' 때문에 까다로움.
# 어떤 모양이 되어야 가장 작은 창고다각형이 나오는지 파악해야함 빨리
#