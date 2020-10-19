from sys import stdin
n = int(stdin.readline())
logDict = {}
stillCompany = []

for _ in range(n):
    name, log = map(str, stdin.readline().split(' '))
    logDict[name] = log[:-1]

for x in logDict:
    if logDict[x] == 'enter':
        stillCompany.append(x)

stillCompany.sort(reverse=True)
for x in stillCompany:
    print(x)

# n 의 범위는 2 ~ 1,000,000
# 딕셔너리에 key 값과 value 값을 넣어주는 명령어를 수행하면(line 6)
# key 값이 딕셔너리에 없으면 삽입하고, 있으면 수정해버림. 이거 사기 아니냐
