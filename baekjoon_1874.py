n = int(input())
init = [i for i in range(1, n+1)]
stack, answer, res = [0], [], []
for _ in range(n):
    x = int(input())
    if stack[-1] == x:
        res.append(stack.pop())
        answer.append('-')
    else:
        while stack[-1] != x:
            stack.append(init.pop(0))
            answer.append('+')
        res.append(stack.pop())
        answer.append('-')
print(res)
for x in answer:
    print(x)
# 1 부터 n 까지 있는 수열을 스택가지고 입력받은 수열로 바꾸고 싶다
# 어떤 수가 정답 수열에 더해지려면, pop 이 되야하고,
# 그 이전엔 당연히 스택에 push 가 됐을것임 물론 걔보다 작은 수들도 마찬가지
# 원하는 수열이 1 2 3 ... 100,000 이면 push() pop() 을 10만 번 하면 끝이고(20만),
# 100,000 99,999 99,998 ... 1 이면 push() 10만 번, pop() 10만 번 이다.
# 스택에서는 top 이 중요. top 가지고 알고리즘을 짤 수 있는지 고민
# 파이썬에서는 [-1]이 top 이라고 생각해도 무방

# 만들고 싶다는 수열 res 의 각 요소들(x)에 대해 for 문을 돌리고,
# x 와 스택의 top 이 일치하면 pop. 그렇지 않으면 x 가 될때까지 push 한 다음 pop

# 수열을 만들 수 없을때 break 처리 없이 일단 위 알고리즘만 돌리니까
# 예제 출력 1은 맞게 나오고 예제 출력 2(NO인 경우)는 
# 비어있는 init 에서 꺼내올려고 해서 런타임에러.
# 어디서 어떻게 break 걸어주는게 가장 똑똑한걸까