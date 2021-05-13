def solution(n, lost, reserve):
    attend = [1 for _ in range(n)]  # 0번부터 n-1번까지 ^^

    for r in reserve:
        attend[r-1] += 1
    for l in lost:
        attend[l-1] -= 1
    print('before:', attend)

    # 지금 알고리즘은 무조건 뒷번호 친구의 체육복을 빌려오는 알고리즘이다.
    # 앞번호 친구의 체육복을 빌려오는 경우도 생각해줘야한다.
    # 그러면, 앞번호껄 빌리는걸로 시작했다가 중간에 1이 많이 나와서 다시 뒷번호껄 빌리는걸로 바뀔수도 있다.
    # 요걸 잘 고려한 알고리즘을 내일 짜보장.

    # 그럴거 없이 그냥 2번부터 n-1 번만 돌고, 앞 뒤를 다 살피는게 어떻겠누
    # 알고리즘 그렇게 안 복잡할걸?

    for i in range(1, n-1):
        if not attend[i]:
            if attend[i-1] == 2:
                attend[i-1] -= 1
                attend[i] += 1
                continue
            elif attend[i+1] == 2:
                attend[i+1] -= 1
                attend[i] += 1
                continue
    # for a in range(len(attend)-1):
    #     if not attend[a] and attend[a+1] == 2:
    #         attend[a] += 1
    #         attend[a+1] -= 1
    if not attend[0] and attend[1] == 2:
        attend[1] -= 1
        attend[0] += 1
    if not attend[-1] and attend[-2] == 2:
        attend[-2] -= 1
        attend[-1] += 1
    print('after:', attend)

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
