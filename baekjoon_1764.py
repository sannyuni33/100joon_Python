from sys import stdin

n, m = map(int, stdin.readline().split(' '))
neverHeared = []
neverSeen = []
result = []

for _ in range(n):
    neverHeared.append(stdin.readline().split())
for _ in range(m):
    neverSeen.append(stdin.readline().split())

for x in neverHeared:
    for y in neverSeen:
        if x == y:
            result.append(x)

print(len(result))
for x in sorted(result):
    print(x[0])

# n, m 이 최대 50만까지 가능하니까 ... 2중으로 체크를 한다면
# 250,000,000,000 까지 가는데 이건 100퍼 시간초과 나올텐데
# 일단 해보고 고민
# 1차시도. 역시나 시간 초과
# input() 을 stdin.readline() 으로 바꿔서 시도. 역시나 시간 초과
# 입력 시간도 뭐 영향이 있겠지만, 제일 크리티컬한 부분은 50만 x 50만임.
# 이걸 피하려면 어떻게 접근해야할까... 이진 탐색트리?
#