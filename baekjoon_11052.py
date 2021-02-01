N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
        print(dp)
    print(i, '번째 카드팩까지 진행완료')
print(dp[i])

# 도움받은 코드 https://infinitt.tistory.com/250
# 1장당 가격이 최대인 카드팩 같은걸 찾을 필요가 없었음
# 1장, 2장, ... n-1장 n 장까지 구매할때 어떻게 사는 경우가 최댓값인지를
# 쭉 저장해서 가져오면 됐다


# n = int(input())
# cardPack = list(map(int, input().split()))
# priceOfCards = []
# c, res = n, 0
# for i in range(len(cardPack)):
#     priceOfCards.append([i+1, cardPack[i]/(i+1)])
# priceOfCards = sorted(priceOfCards, key=lambda price: price[1], reverse=True)
#
# print(*priceOfCards)
#
# while True:
#     tmp = priceOfCards[0]  # 1장당 가격이 제일 비싼 카드팩
#     print('Most expensive card pack:', tmp)
#     while c >= tmp[0]:  # 그 카드팩으로 구매할 수 있는만큼 구매
#         c -= tmp[0]
#         res += cardPack[tmp[0] - 1]
#         print('Bought card pack')
#     if not c:  # n장의 카드를 모두 사면 종료
#         break
#     # 카드를 더 사야하면
#     while priceOfCards[0][0] > c and len(priceOfCards) > 0:
#         print(priceOfCards.pop(0))
# print(res)

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
# 역시 DP 써야하나. DP 써서 푼다해도 이 코드의 반례가 궁금하긴 함

# 10장 구매하려고 할 때 1 100 160 1 1 1 1 1 1 1 로 가격이 주어지면
# 정답은 520, 출력은 481
# 장당 가격이 높은걸로 살 수 있는만큼 사는 것 자체가 틀린거였음. 역시 DP 해야함
# 카드팩 하나를 구매하고, 그 상황에서의 최적해를 계속 구해야함요
# 정답이 520인건, 3장, 3장, 2장, 2장 이렇게 구매해서임
# 3 3 3 1 이 아니라 3 3 2 2 였던 것. 어떤 근거로 이렇게 구매했을지를 설계
