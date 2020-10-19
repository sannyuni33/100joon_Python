numList = []
for i in range(1, 45):
    for _ in range(i):
        numList.append(i)
for _ in range(10):
    numList.append(45)

a, b = map(int, input().split(' '))

res = 0
for i in numList[a-1:b]:
    res += i
print(res)

# 수열의 범위는 1000, 990번째가 44고 991부터 1000번째까지 45
# 그렇다고 이걸 그대로 길이 1000짜리 리스트를 만들면 맞긴 맞는데 너무 무식한데요.
# 좀 이쁜 코드를 짜고 시픈디... 이게 최선일까요. 만약 수열 범위가 무한이면 어떻게 해야할까.
# 딕셔너리를 이용해보면 어떨까요. 숫자가 key, 범위가 value 로 나오면?
# 딕셔너리보다는 경계값만 요소로 갖고 있는 리스트를 만들면 어때요
# 1, 3, 6, 10, 15 ... 이렇게하고 인덱스 숫자를 더하는 방식으로 하는것이 어떤가 싶어요
#

# borderList = []
# tmp = 0
# for i in range(1, 45):
#     tmp += i
#     borderList[i-1] = [i]
# borderList.append(1000)
#
# a, b = map(int, input().split(' '))
