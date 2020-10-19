n = int(input())
first = input()
for _ in range(n-1):
    word = input()
    for i in range(len(first)):
        if first[i] != '?' and word[i] != first[i]:
            first = list(first)
            first[i] = '?'
            first = ''.join(first)
print(first)

# 여러개의 문자열을 받는데... 문자열의 길이가 모두 같다?
# 문자열을 입력 받으면 처음 문자열하고만 비교하면 되지 않을까 싶다.
# 한 번이라도 틀린거 나오면 ? 처리하고
# 1차 시도 실패 ... 머가 틀렸을까
# 파일이름에 ? 가 들어가는게 문제일래나
# 아닌데 ... 설마 대소문자?
# 아니다 아니다 replace 할 때마다 프린트 찍어보니까 문제점을 확인했음.
# config.sys 에서 왜 한 번에 config.?y? 가 되는지 실험해보니까
# 문자열에 존재하는 모든 s를 한 번에 바꿔버리는 놈이었음 replace 가.
# 후 .... 그럼 다른 방법을 써야하는디.
# 리스트를 활용해봐야 할까나 => 맞았음