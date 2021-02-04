def solution(dartResult):
    nums = [0, 0, 0]
    a = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            print(dartResult[i])
            if dartResult[i] != '0':
                nums[a] += int(dartResult[i])
            else:
                nums[a] *= 10
        elif dartResult[i].isalpha():
            print(dartResult[i])
            if dartResult[i] == 'D':
                nums[a] = nums[a]**2
            elif dartResult[i] == 'T':
                nums[a] = nums[a]**3
            print(nums[a])
            if i+1 < len(dartResult) and dartResult[i+1].isdigit():
                a += 1
        else:  # '*' or '#'
            if dartResult[i] == '*':
                if a > 0:
                    nums[a - 1] *= 2
                nums[a] *= 2
            elif dartResult[i] == '#':
                nums[a] = -nums[a]
            a += 1
    answer = sum(nums)
    print(answer)
    return answer


solution(input())

# 1. 첫번째, 두번째, 세번째 시도로 나눠주고 하는 방법
# 2. 나누지말고 for i in range(len(dartResult))로 하는 방법

# 1은 점수가 10인 경우와 옵션이 있을수도 없을수도 있는 경우를 생각해야하고
# 2는 조건문이 많이 생길것으로 예상됨.

# 2번 방법으로 하고 있는데, 언제 다음기회 점수로 넘어갈꺼냐 하는게 고민거리
# 옵션이 있을수도 없을수도 있기때문

# programmers.co.kr 에서 다른 사람의 풀이를 보면,
# 보너스와 옵션을 딕셔너리로 정의하고, re 패키지의 compile 함수를 사용함.
# 파이썬 공부를 더해야겠삼