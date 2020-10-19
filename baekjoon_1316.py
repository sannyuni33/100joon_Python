numOfWord = int(input())
numOfGW = numOfWord


def func1():
    used = []  # 나온적 있는 알파벳의 리스트
    wd = str(input())
    for i in range(1, len(wd)):
        if wd[i] != wd[i - 1]:
            used.append(wd[i - 1])
            for x in used:
                if x == wd[i]:
                    return True
        else:
            continue


for _ in range(numOfWord):
    if func1():
        numOfGW -= 1
print(numOfGW)

# 그룹 단어냐 아니냐를 나누는 기준은 한 번 나온 알파벳이 또 나오냐 안나오냐.
# '한 번 나왔다' 라는 것은 연속되게 나온 것도 포함.
# 첫 번째로 필요한 건 연속되게 나온것을 한 번 나온것으로 간주하는 알고리즘.
# 두 번째가 나왔던게 또 나오는지 체크하는 알고리즘.
# 이거 두 개 있으면 그룹단어인지의 여부 판단 가능.
# 맞긴 했는데... 2중 for 문에다가 조건문도 두 개나 들어가버려서...
# 좀 더 효율적인 코드가 있지 않을지 고민할 필요가 있음
