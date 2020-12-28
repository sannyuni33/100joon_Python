n = int(input())
balloons, res = [], []
nums = list(map(int, input().split()))
for i in range(n):
    balloons.append([nums[i], i+1])

while True:
    mes = balloons.pop(0)
    res.append(mes[1])

    if len(balloons) < 1:
        break

    if mes[0] > 0:  # 나온수가 양수일때
        for i in range(mes[0]-1):
            tmp = balloons.pop(0)
            balloons.append(tmp)
    else:  # 나온수가 음수일때
        for j in range(-mes[0]):
            tmp = balloons.pop(-1)
            balloons.insert(0, tmp)

for i in range(n):
    print(res[i], end=' ')
# n 을 입력받으면, balloons 의 요소들의 값의 범위는 -n ~ n 이다. 0은 제외
# 터쳐서 양수가 나오면 오른쪽으로, 음수가 나오면 왼쪽으로 돈다.
# 이동할 때 이미 터진애는 치지 않는다.
# 터진 풍선의 번호를 알고있어야 하므로, 인덱스를 바로 저장할 수는 없음.
# pop 을 할 때마다 모든 요소들의 인덱스가 바뀌기 때문.
# 입력을 받을적에 풍선번호를 부여해주던가,
# 변수 하나로 왔다리 갔다리 하는 두 가지 방법이 떠오름.
# 두 번째 방법은 꽤... 복잡해보인다.


