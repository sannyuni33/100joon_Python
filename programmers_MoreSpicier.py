def solution(scoville, K):
    answer = 0
    scoville.append(K)
    scoville.sort()
    scoville = scoville[:scoville.index(K)]

    for i in range(len(scoville)-1):
        scoville.sort()
        newScov = scoville.pop(0) + 2*scoville.pop(0)
        scoville.append(newScov)
        answer += 1
        if newScov >= K:
            break

    if scoville[0] < K:
        return -1
    return answer



# solution([1, 2, 3, 9, 10, 12], 7)
print(solution([1, 2, 3, 7, 9, 10, 12, 3, 67, 124, 34, 21, 215, 123, 232, 57], 100000000))
# 가장 먼저 K 이상인 원소를 싹 다 뺀다.
# 그 리스트에서 가장 작은 두 개를 뽑고, 새로운 스코빌 지수를 구해 맨 앞에 넣는다.

# 1차 시도 실패. sort 가 많으니까 시간 초과도 많이 날듯함.
