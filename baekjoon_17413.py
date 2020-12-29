sentence = list(input())
res = ""
stack = []
n = 0

while n < len(sentence):
    if sentence[n] == '<':
        while sentence[n] != '>':
            res += sentence[n]
            n += 1
        res += sentence[n]  # '>'도 결과에 넣어줘야 함
        n += 1
    elif sentence[n] == ' ':
        res += sentence[n]  # ' '도 결과에 넣어줘야 함
        n += 1
    else:
        while sentence[n] != '<' and sentence[n] != ' ':
            stack.append(sentence[n])
            n += 1
            if n == len(sentence):
                break
        while len(stack) > 0:
            res += stack.pop(-1)
print(res)
# 태그(< >)는 그대로 두고, 나머지는 단어별로 뒤집어야 함
# split(' ') 을 쓰기에는, 태그와 단어가 붙어있는 경우가 있음
# 이런 애들을 어떻게 태그와 단어로 구분할거냐 하는게 중요한 문제인듯
# 단어와 태그의 차이는 시작과 끝이 <>냐 아니냐로 나뉘는데,

# 문자열 앞에서부터 차근차근 진행,
# 1. <이 나오면 >이 나올때까지 그대로 결과에 더한다.
# 2. 문자가 나오면 스택에 집어넣다가~
# 3. 공백이나 < 가 나오면 스택을 전부 pop 한다!

# 문자열이 태그로 끝나면 제대로 나오고, 단어로 끝나면 index out of range 오류 뜸
#