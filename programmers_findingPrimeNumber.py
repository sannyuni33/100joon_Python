import math
from itertools import permutations as pm


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        ss = set(list(pm(numbers, i)))  # 해당 길이 숫자에서 중복제거
        for s in ss:
            num = int(''.join(s))
            if isPrime(num):
                answer.append(num)
        return len(set(answer))


solution()