n = int(input())
p = int(input())
photoFrames, countCache, lruQ = [0]*n, [0]*n, []
for _ in range(p):
    r = int(input())
    if r not in photoFrames:
        print('cache miss. find min.')
        if countCache.count(min(countCache)) > 1:
            print('multiple min. use LRU.')
        else:
            print('')

    else:
        print('cache success')
        countCache[photoFrames.index(r)] += 1


# LRU 캐시교체 알고리즘에다가 참조횟수를 추가해줘서 풀어야함.
# 캐시 실패가 발생하면
# 1. 참조횟수가 적은놈을 먼저 교체
# 2. 그게 여럿이면 제일 오래된놈을 교체
# in, not in photoFrames 을 먼저 판단하고,
# not in 이라서 교체를 할 때는 참조횟수가 우선 순위임.