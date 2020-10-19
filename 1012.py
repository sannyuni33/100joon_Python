"""
20.07.08
먼저 입력받은거 저장부터 잘 해보자

일단은 하나의 테스트 케이스를
케이스 = [가로길이, 세로길이, 배추수, [배추위치리스트]]
요렇게 저장했고, 배추위치리스트를 가지고 0, 1 행렬을 만들어야할 필요가 있나 없나?
이걸 만들지 말지는 문제풀이 접근방법에 따라 다를듯싶음.

"""

testCases = int(input())
caseLists = []
for i in range(testCases):
    row, col, cabbage = map(int, input().split(' '))
    caseLists.append([row, col, cabbage])
    cabbageMap = []
    for _ in range(caseLists[i][2]):
        x, y = map(int, input().split(' '))
        cabbageMap.append([x, y])
    caseLists[i].append(cabbageMap)


print(caseLists)

