def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities)*5
    for n in range(len(cities)):
        cities[n] = cities[n].lower()
    answer = 0
    cache = ['']*cacheSize
    indexQ = [i for i in range(cacheSize)]

    for i in range(len(cities)):
        if cities[i] not in cache:
            c = indexQ.pop(0)  # indexQ의 0번째가 가장 오래된 놈
            cache[c] = cities[i]
            indexQ.append(c)
            answer += 5
        else:
            c = cache.index(cities[i])
            indexQ.append(indexQ.pop(indexQ.index(c)))
            answer += 1
    return answer


solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])

# 캐시사이즈만큼의 캐시를 만들고, 거기에 cities 의 첫번째 요소부터 넣어준다.
# 캐시 교체 알고리즘은 LRU 니까, 교체된지 가장 오래된놈이 누군지를 알아야한다.
# 캐시에는 중복되는 요소가 없으니까 인덱스를 저장하는 큐를 사용하는게 어떨까
# c 라는 변수로 캐시 어느 자리에 넣어줄껀지 정하는데 이걸 잘 만져야함