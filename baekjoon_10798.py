wordList = []
result = []
for _ in range(5):
    wordList.append(list(input()))

sortedList = sorted(wordList, key=len)

for i in range(len(sortedList[-1])):
    for j in range(5):
        if len(wordList[j]) > 0:
            result.append(wordList[j].pop(0))

result = ''.join(result)
print(result)
# 다섯개의 단어를 큐에 집어넣는다 생각하고 돌리면 될려나.
# 행렬에 집어넣으면 어떨...까가 아니라 이미 행렬형태라고 봐도됨.
# if wordList[j][i] 로 요소가 존재하는지 확인이 안됨. out of range 오류 뜸.
# pop 연산써서 앞 글자 뽑아내는 방식으로 해결