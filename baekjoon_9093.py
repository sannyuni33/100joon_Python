t = int(input())
result = []

for _ in range(t):
    tempList = input().split(' ')  # 공백 구분해서 입력받기
    reversedList = []

    for x in tempList:
        reversedList.append(x[::-1]+' ')  # 단어 하나씩 뒤집어서 리스트에 저장, 공백 추가
    reversedList[-1] = reversedList[-1][:-1]  # 맨 마지막 단어만 공백 제거

    res = ""
    for y in reversedList:
        res += y  # 한 줄에 출력하기
    result.append(res)  # 결과 리스트에 출력

for z in result:
    print(z)

# 맨 처음에는 reversedList 를 따로 만들지 않고 tempList 에 대해 for 문을 직접돌리면서
# x = x[::-1]로 리스트의 원소 자체를 변경을 시도했는데 왜 이게 안바뀌는지 의문임.
# 파이썬에 대한 공부가 더 필요해보임..