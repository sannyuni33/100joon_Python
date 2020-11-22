n = int(input())
res = []

for _ in range(n):
    stack = []
    ps = input()
    for x in ps:
        stack.append(x)

    check = 0
    while check > -1 and len(stack) > 0:
        if stack.pop() == ')':
            check += 1
        else:
            check -= 1

    if check != 0:
        res.append('NO')
    else:
        res.append('YES')

for r in res:
    print(r)


# 괄호 검사 -> 스택
# 스택이 비었는지 검사하는 방법은 len 을 사용해도 되고..
# vps 가 되지 못하는 경우는 무엇무엇이 있을까
# 맨 처음부터 ( 가 나오면 무조건 나가리.
# ) 로 먼저 시작하는데, ) 가 나온 수 만큼 ( 가 나와줘야 vps 로 인정.

# 예제 입력 테스트 결과 ))가 YES 로 나옴. 심각한 오류
# 지금 while 문의 조건은 check > -1 이고 len(stack) 이 0보다 클 때.
# 즉 ) 의 갯수가 ( 갯수보다 적지만 않으면 YES 가 되는 알고리즘임 지금.

# 그럼 vps 가 되지 못하는 경우를 다시 정의해야 함.
# 첫 번째, ) 가 나온 횟수만큼 ( 가 나와야 함. 스택 비었을 때 정확히 같아야 함.
# 두 번째, 중간에 ( 갯수가 많아진다면 루프문 끝내야 함.
# 스택 끝나고나서 조건문만 바꿔줘서 해결!
