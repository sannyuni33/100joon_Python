#You may use import as below.
#import math

def solution(n):
    # Write code here.
    answer = 0
    tmp = 1
    answer += tmp
    cnt = 1  # 1까지 더해준 상태

    dp = 2*(n - 1)
    while cnt < n:
        tmp += dp  # 여까지 이상 없음
        answer += tmp
        print(tmp, '를 더했삼')
        cnt += 1
        if cnt == n:
            break
        if not cnt % 2:
            tmp += dp
            answer += tmp  # 두 번씩 더해줘야 해서
            print(tmp, '를 더했삼')
            cnt += 1
            dp -= 4

    return answer


#The following is code to output testcase.
# n1 = 7
# ret1 = solution(n1)
#
# #Press Run button to receive output.
# print("Solution: return value of the function is", ret1, ".")
#
# n2 = 2
# ret2 = solution(n2)
#
# #Press Run button to receive output.
# print("Solution: return value of the function is", ret2, ".")

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))


# 소용돌이 수... 대각선 성분의 합을 구한다고 하면
# 2 => 1 + 3        ( +2 ) = 4
# 3 => 1 + 5 + 9    ( +4 +4 ) = 15
# 4 => 1 + 7 + 13 + 15      ( +6 +6 +2 ) = 36
# 5 => 1 + 9 + 17 + 21 + 25 ( +8 +8 +4 +4 ) = 73
# 6 => 1 + 11 + 21 + 27 + 33 + 35   ( +10 +10 +6 +6 +2) = 128
# 7 => 1 + 13 + 25 + 33 + 41 + 45 + 49( +12 +12 +8 +8 +4 +4) = 207
# 이런식으로 반복이 되고... 뭔가 규칙성이 보인다.
