fiboList = [0, 1]
n = int(input())

for _ in range(n-1):
    fiboList.append(fiboList[-2]+fiboList[-1])

print(fiboList[-1])
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ... 이 피보나치 수열인데.
# 피보나치 수를 보통 fibo 라는 함수를 정의해서 재귀로 풀던데...
# 파이썬에서 시간초과가 안뜰까?
# 리스트에 append 만 하고 반목문 끝난 다음에 -1번째 꺼내면 가능할 것 같은디.
# 제 생각은요. 재귀 안해도 될 것 같아요.

# 아~ 넘 쉽다! 파이썬 개꿀

# DP 써서 풀어보삼요
