n = int(input())
p = int(input())
rlist = list(input().split())
rlist = [int(i) for i in rlist]
photoFrames, countCache, lruQ = [0 for _ in range(n)], [0 for _ in range(n)], [i for i in range(n)]
for r in rlist:
    print('r:', r)
    if r not in photoFrames:
        print('cache miss. find min.')
        if countCache.count(min(countCache)) > 1:  # 최소값이 여러개(여기서 시작)
            print('countCache;', countCache)
            m, mlist = min(countCache), []
            for n in range(len(countCache)):
                if countCache[n] == m:
                    mlist.append(n)
            for c in lruQ:
                if c in mlist:
                    i = c
                    break
        else:  # 최소값이 한개
            i = countCache.index(min(countCache))
        photoFrames[i] = r
        countCache[i] = 1
    else:
        print('cache success')
        countCache[photoFrames.index(r)] += 1
    lruQ.append(lruQ.pop(lruQ.index(photoFrames.index(r))))  # 캐시성공은 여기서 끝
    print('photoFrames:', photoFrames)
    print('lruQ:', lruQ)

while True:
    try:
        photoFrames.remove(0)
    except:
        break

print(*sorted(photoFrames))


# LRU 캐시교체 알고리즘에다가 참조횟수를 추가해줘서 풀어야함.
# 캐시 실패가 발생하면
# 1. 참조횟수가 적은놈을 먼저 교체
# 2. 그게 여럿이면 제일 오래된놈을 교체
# in, not in photoFrames 을 먼저 판단하고,
# not in 이라서 교체를 할 때는 참조횟수가 우선 순위임.

# 최소값이 여러개면 최소값 갖는 애들의 인덱스를 mlist 에 저장하고,
# lruQ 의 원소를 0번부터 살피다가 mlist 에 있는애면 i로 지정하고 반복문 종료
