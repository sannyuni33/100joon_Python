n = int(input())
cardPack = list(map(int, input().split()))
priceOfCards = []
c, res = n, 0
for i in range(len(cardPack)):
    priceOfCards.append([i+1, cardPack[i]/(i+1)])

priceOfCards = sorted(priceOfCards, key=lambda price: price[1], reverse=True)

while True:
    tmp = priceOfCards[0]
    print('장당 가격 최고팩:', tmp)
    while c >= tmp[0]:
        c -= tmp[0]
        res += cardPack[tmp[0] - 1]
        print('팩 하나 샀삼')
    if not c:
        break
    while priceOfCards[0][1] == tmp[1] and len(priceOfCards) > 0:
        priceOfCards.pop(0)
        print('장당 가격 최고팩 하나 뺐삼')
print(*cardPack)
print(*priceOfCards)
print(res)
# 배낭 문제랑 비슷해 보인다. 카드팩이 물건, 카드수가 무게, 가격이 가치
# 살짝 다른 부분은 카드 수(무게)를 무조건 꽉 채워야 한다는 것

# 각 카드팩의 1장 당 가격을 따지고, 내림차순으로 정렬
# 가장 앞에 있는(장당 가격이 비싼) 카드팩으로 구매할 수 있는 만큼 구매
# 하고 남은 나머지 카드 수를 채워야 한다
# 장당 가격 최댓값을 갖는 카드팩이 여러개인 경우엔...?

# 나머지 카드 수보다 적은 카드팩만 남기고 같은 과정을 반복한다
# 라고 하면 직관적으로는 풀릴듯 한데, 그럼 너무 쉽게 풀리는데
# 함정이 있을 것 같다................정답률 60% ...읭?

# 배낭 문제하고는 아예 다르다. 동일한 카드팩(물건)을 여러번 선택 가능하니까
# 반례를 최대한 생각해보자
# n = 19 이고, 5장팩과 6장팩의 가격이 모두 10인 경우.
# 5, 6, 4, 1, 팩 제외하고 모두 0이라치고 1장팩과 4장팩의 가격에 따라 어떻게 달라질지
# 1장팩이 2, 4장팩이 8이면, 그러니까 1장당 가격이 같다면 어느걸로나 해도 상관 x
# 근데 아니다!!! 5장팩과 6장팩의 가격이 같다면 5장팩이 1장당 가격이 높은거고,
# 그럼 5장팩으로 3번 구매하고 4장이 남고.

# 예제입력 여섯개는 다 맞게 나오지만 답은 틀렸삼!