t = int(input())
for _ in range(t):
    n = int(input())


# 1 + 3 과 3 +1 은 다른 방법으로 간주
# 3 이 입력으로 들어오면, (1 + 1 + 1) (1 + 2) (2 + 1) (3) => 4가 나오는게 맞고
# 6 이 입력으로 들어오면...
# 각 튜플 요소 사이에 다른 튜플 요소를 넣을 수 있는 경우를 세는 건 너무 어려운 접근방법
# 발상의 전환을 바꿔야 한다
# 정답률이 61퍼라는건 쉬운편에 속하는 문제라는거니까 내가 너무 어렵게 생각하는 듯.

# 사이사이에 들어온다고 생각하지말고, 3씩 나눠서 곱하는 방식으로 하면 되나.
# 3 을 표현할 수 있는 방법은 총 4가지.
# 4 를 표현할 수 있는 방법은 총 7가지...

# 2를 표현하는 방법은 두 가지 뿐 (1 + 1) (2)
# 5를 표현할땐 3과 2로 나누고 곱한다고 생각하면 8가지가 나와야하는데 그럴리가 없음
# 다른 변수를 생각해야 함
#