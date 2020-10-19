n = int(input())
sangCard = []
for _ in range(n):
    sangCard.append(int(input()))

m = int(input())
targetCard = []
for _ in range(n):
    targetCard.append(int(input()))

print(sangCard, targetCard)

# 이것두 듣보잡 문제랑 비슷
# 50만 X 50만 이니까 시간초과 안되게 하려면 우째야 될까 ..
# C++이랑 자바는 시간초과 안뜨나요 ?!?
