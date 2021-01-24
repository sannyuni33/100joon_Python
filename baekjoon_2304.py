n = int(input())
columns, left, right = [], [], []
highest = [0, 0]  # 가장 높은 기둥(최초 기준)
for _ in range(n):
    locate, height = map(int, input().split())
    if height > highest[1]:
        highest = [locate, height]
    columns.append([locate, height])
res = highest[1]  # highest 의 면적만큼 결과값에 더함

for x in columns:
    if x[0] < highest[0]:
        left.append(x)
    elif x[0] > highest[0]:
        right.append(x)
# highest 와의 거리를 기준으로 정렬. 가까운 기둥부터 0번
# max 를 해도 highest 랑 가까운애가 먼저 걸림
left.sort(reverse=True)
right.sort()

print(*right)

print('start left')
std = highest
while len(left) > 0:
    lh = max([x[1] for x in left])
    print('new column:', lh)

    while left[0][1] != lh:  # 기준 기둥과 새로 선택된 기둥사이의 기둥 제거
        left.pop(0)
        if len(left) == 0:  # out of index 방지
            break

    print(left[0][1]*(std[0]-left[0][0]), 'has added')
    res += left[0][1]*(std[0]-left[0][0])
    print('res:', res)
    print('left: ', *left)
    std = left[0]
    left.pop(0)
    print('new highest:', std)

print('start right')
std = highest
while len(right) > 0:
    rh = max([x[1] for x in right])

    while right[0][1] != rh:  # 기준 기둥과 새로 선택된 기둥사이의 기둥 제거
        right.pop(0)
        if len(right) == 0:  # out of index 방지
            break

    print(right[0][1] * (right[0][0] - std[0]), 'has added')
    print(right[0][1], right[0][0] - std[0])
    res += right[0][1] * (right[0][0] - std[0])
    print('res:', res)
    std = right[0]
    right.pop(0)

print(res)

# 5번 조건인 '오목하게 들어간 부분이 없어야한다' 때문에 까다로움.
# 어떤 모양이 되어야 가장 작은 창고다각형이 나오는지 파악해야함 빨리
# 가장 높은 기둥에서부터 시작... 가장자리로 가면서 지붕은 낮아질순 있지만 높아질순 없다
# 가장 높은 기둥을 시작으로 왼쪽으로 진행, 오른쪽으로 진행
# 왼쪽에 기둥 중 제일 높은 것 선택. 선택된 애를 기준으로 왼쪽으로 계속진행, 오른쪽도 마찬가지
# 다각형 넓이는 지붕 높이가 바뀔때마다 그려지는 직사각형 넓이를 더하자
# 예제처럼 주어지면 2*4 + 4*6 + 10*1 + 7*8 = 98 나옴
# 기준 기둥과 선택된 기둥의 거리차이와 선택된 기둥의 높이를 곱하면 직사각형 넓이 나옴

# '제일 높은 기둥' 선택할때 max()를 쓰게 될 것 같은데
# 만약 기둥이 1 2 3 ... 498 499 500 499 498 ... 3 2 1
# 이런식으로 생겨 먹었으면 max() 를 1000 번 호출할 것으로 예상되니 주의.
# 혹은 1000개 기둥의 높이가 모두 같을경우도 고려해야 함.
# 가장 높은 기둥이 여러개일 경우는 리스트 컴프리헨션 사용해서 해결가능할듯

# 132ms 로 해결완료