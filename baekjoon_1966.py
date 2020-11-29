testCase = int(input())
result = []

for _ in range(testCase):
    n, m = map(int, input().split())
    priority = input().split()
    priority = list(priority)
    pntCount = 0

    while len(priority) > 0:
        if m == 0:  # 알고싶은 문서가 큐의 헤드에 왔음
            if max(priority) == priority[0]:  # 중요도 높은 다른 문서 없음
                break
            else:  # 중요도 높은 다른 문서 있어서 제일 뒤로 빠꾸
                tmp = priority.pop(0)
                priority.append(tmp)
                m = len(priority)-1

        tmax = max(priority)
        tmp = priority.pop(0)
        if tmax != tmp:
            priority.append(tmp)
        else:
            pntCount += 1
        m -= 1

    result.append(pntCount+1)
for r in result:
    print(r)
# 첫 번째로 구현해야 할 것은 나머지 문서들 중 중요도가 더 높은애가 있는지 확인하는 것.
# 두 번째로 구현할 것은 뒤로 보내는 애의 위치를 기억해주는 것.
# 생각해야 할 것은, 언제까지 이걸 반복하냐 이거임.
# m 자리의 문서가 출력이 되면 끝내야 하고,
# while 문으로 돌리면 될 것 같은데 0 자리에 왔다고 무조건 출력이 되는게 아니고
# 뒤에 더 큰 애가 있으면 뒤로 보내야 함.
# 한 번에 맞아버리네... 시간은 84ms