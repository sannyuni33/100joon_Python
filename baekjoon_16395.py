n, k = map(int, input().split())

if n > 2:
    firstRow = [1, 1]
    secondRow = []
    for _ in range(n-2):  # n번째 행을 만들때까지 반복
        for i in range(len(firstRow)-1):  # 위의 행을 가지고 아래 행을 만듦
            secondRow.append(firstRow[i]+firstRow[i+1])
        secondRow.insert(0, 1)  # 맨 앞에 1 추가
        secondRow.append(1)  # 맨 뒤에 1 추가
        firstRow = secondRow
        secondRow = []
    print(firstRow[k-1])
else:
    print(1)

# 가장 먼저 생각해 볼 것은
# 1. 파스칼 삼각형 모양의 리스트를 만들어놓고 거기서 탐색을 할건지
# 2. 법칙을 찾아서 n과 k만 가지고 찾을건지
# 3. DP 써서 두 개의 행만 가지고 돌리면 되지 않을까
# 3번 방법으로 금방 해결요..! 메모리 29088KB, 시간 72ms

