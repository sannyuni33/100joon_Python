n = int(input())
init = [i for i in range(1, n+1)]
stack, answer, res = [0], [], []
for _ in range(n):
    res.append(int(input()))
for x in res:
    if stack[-1] != x:
        while stack[-1] != x and len(init) > 0:
            stack.append(init.pop(0))
            answer.append('+')
    if stack.pop() != x:
        print("NO")
        exit()
    answer.append('-')
for a in answer:
    print(a)
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

# 이미 5가 pop 되었다는 것은 init 이 텅텅 비었다는 것.
# 그러면 3은 이미 스택에 있다는 것.

# 맞긴 했는데 시간이 5636ms
# 132ms 걸린 코드를 참조해본 결과, init 이라는 리스트는 필요가 없음.
# 만들고자 하는 수열의 각 요소 p에 대해 반복문을 돌리는 것 까지는 일치하는데
# p와 같은 수가 스택에 들어올때까지 1부터 스택에 넣음
# 그 다음부터는 top 이 p 와 같은지와 비교해서 처리하는 부분은 내 코드랑 같은데
# init 을 괜히 사용해서 init 의 길이를 살피고 비교문이 하나 더 추가되버림.
# 갈 길이 멀다