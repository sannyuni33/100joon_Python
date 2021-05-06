import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    print(scoville)

    for i in range(len(scoville)-1):
        if scoville[0] >= K:
            break
        hq.heappush(scoville, hq.heappop(scoville) + 2*hq.heappop(scoville))
        answer += 1
        print(scoville, answer)

    if scoville[0] < K:
        return -1
    return answer



print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1, 2, 3, 7, 9, 10, 12, 3, 67, 124, 34, 21, 215, 123, 232, 57], 100000000))
# print(solution([2, 2, 2, 2, 2, 2], 42))
# print(solution([4, 1, 7, 3, 8, 5], 5))

# 가장 먼저 K 이상인 원소를 싹 다 뺀다.
# 그 리스트에서 가장 작은 두 개를 뽑고, 새로운 스코빌 지수를 구해 맨 앞에 넣는다.

# 1차 시도 실패. sort 가 많으니까 시간 초과도 많이 날듯함.
# 이 문제가 힙 문제인만큼, 새로운 숫자를 리스트에 넣고 정렬하기보다
# 힙을 구현하고 거기에 넣어서 자동으로 정렬되게끔 하는 부분이 낫겠다.

# 일단 2차 시도에서는 sort는 놔두고 반복문 끝내주는 부분만 수정.
# 테스트케이스는 모두 맞았지만 효율성 테스트는 모두 시간초과. 최소힙 구현 고고

# heapq 모듈 사용해서 성공!