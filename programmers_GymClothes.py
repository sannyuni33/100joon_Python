def solution(n, lost, reserve):
    attend = [1 for _ in range(n)]  # 0번부터 n-1번까지 ^^

    for r in reserve:
        attend[r-1] += 1
    for l in lost:
        attend[l-1] -= 1

    for a in range(len(attend)-1):
        if not attend[a]:
            if attend[a+1] == 2:
                attend[a] += 1
                attend[a+1] -= 1
    return n - attend.count(0)


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])

# 첫 번째 접근
# 모든 애들의 체육복은 1벌
# reserve 에 있는 애들껀 2로 증가.
# lost 에 있는 애들껀 -1 한다.
# 그 다음 그리디로

# 두 번째 접근
# for i in range(1, n+1) 을 돌면서
# reserve 에 있을때와 lost 에 있을때의 프로세스를 정의한다.
