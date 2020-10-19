n = int(input())
tmp1, tmp2 = [], []
arr1 = list(input().split(' '))
arr2 = list(input().split(' '))
arr1.sort()
tempList = [float('-inf')]

for i in range(n):
    arr1[i] = int(arr1[i])
    arr2[i] = int(arr2[i])

for i in range(n):
    tmp1.append([arr1[i], i+1])
    tmp2.append([arr2[i], 0])
    tempList.append(arr2[i])
tempList.sort()

rank = 1
while len(tempList) > 1:  # 크기 순위 부여하기
    for i in range(n):
        if tmp2[i][0] == max(tempList):
            tempList.pop()
            tmp2[i][1] = rank
            rank += 1

# 이 부분에서 런타임 오류가 떴던게, B 의 마지막 수가 0, 1 아니고 다른 수면
# 오류가 떴었는데 왜 그런고...
# 마지막이 2 이상이면 비어있는 리스트에 대해 max()를 수행할 수 없다는 오류가 뜨는데 ..
# 그건 1도 마찬가지 아니냐? -> -inf 집어넣어서 어거지로 해결

for i in range(n):
    for j in range(n):
        if tmp1[i][1] == tmp2[j][1]:
            tmp1[i], tmp1[j] = tmp1[j], tmp1[i]

# 위와 같이 코드를 짜니까 예제 입력 1이 들어오면,
# 0은 자기랑 맞는 애는 찾아보지도 못하고 for 문이 끝나버림.
# 이걸 해결하면 '1' 들이 동일하게 4순위를 갖는 것은 문제가 안될 듯 함.
# A 에게 순위 부여를 1~n 까지 똑바로 해주면 답이 나옴.
# 둘 중에 하나만 해결해도 답 나오는데 ...........
# 어 잠깐만. A는 재정렬 쥰내 해도 되는거 아니냐?
# 근데 B도 순위 제대로 넣어줘야 해결되는건 마찬가지 .... 결국 해결해야 함.

result = 0
for i in range(n):
    result += int(tmp1[i][0]) * int(tmp2[i][0])
print(result)
# 리스트 안의 요소들이 문자이긴 하지만 정렬하는데에는 문제가 없음.
# 마지막에 int 로만 바꿔서 처리하면 끝나는 문제고,
# 문제는 arr2 를 안건드리고 arr1을 정렬해야 하는 것.
# 정렬의 기준도 s 값을 작게 만드는게 목적이니까 ..
# arr2에서 가장 큰 값에다가 arr1의 가장 작은 값을 매칭시키는 것이 s 를 작게 만드는 방법.
# arr2를 그냥 재배열 해버려도 정답 출력에는 영향을 미치지 않지만
# 알고리즘을 생각해보는게 취지니까 ... 재배열 하지말고 해보자
# arr2의 원소들을 '순서' 라고 생각해도 되지 않을까
# arr1이랑 arr2를 딕셔너리로 만들어버리고 value 값에다가 순서를 저장해서
# arr1은 작은 순서대로, arr2는 큰 순서대로 value 값을 지정.
# 그러면 문제는 얘네들한테 순서를 부여해주는 방식인데.
# peek 와 비교하는 식으로 해서 달아주는게 좋을까?
# 이 원소가 리스트에서 몇 번째로 큰 수인지 정해주는 알고리즘만 짜면 완성인데.
# <= >= 식으로 비교하면 같은 수의 순위가 모두 같은 수가 되버리는 문제가 생기는데 우짜지
#