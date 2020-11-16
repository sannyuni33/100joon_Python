def getGCD(a, b):
    while b:  # 유클리드 호제법
        a, b = b, a % b
    return a


n = int(input())
trees = []
intervals = []

trees.append(int(input()))
for i in range(1, n):
    t = int(input())
    trees.append(t)
    intervals.append(t-trees[i-1])

print('trees: ', trees)
print('intervals: ', intervals)

gcd = intervals[0]
for i in range(len(intervals)):  # 간격들의 리스트에서 gcd 구해버리기~!
    gcd = getGCD(gcd, intervals[i])

res = 0
curr = trees[0]
while curr < trees[-1]:
    if curr not in trees:
        res += 1
    curr += gcd

print(res)
# (1, 3, 7, 13) 일 때는 (5, 9, 11) 에 심어야 함...
# 이렇게 심어야하는 이유는 1 ~ 3 의 간격이 2로 가장 좁기 때문에 여기에 맞춰서 심은 것
# (2, 6, 12, 18) 일 때는 (4, 8, 10, 14, 16) 에 심어야 함
# 이럴때는 2 ~ 6의 간격이 4로 가장 좁긴 한데 나머지 간격이 6이라서 2 간격으로 심은 것
# 결국 "간격들"의 최대공약수를 구하는 문제임
# 최대공약수를 구한 다음, 첫 번째 요소에 더하면서 카운팅해주고
# trees 리스트에 존재하는 수라면 카운팅하지말고 넘어가면 될 듯

# ...로 하니까 시간초과가 떠부리네요잉
# 가로수의 수는 최대 100,000이고, 가로수의 위치는 최대 100,000,000
# 어디서 오버헤드가 생겼을까. 유클리드 호제법이 의심된다.
