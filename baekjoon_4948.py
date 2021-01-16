def prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


while 1:
    n = int(input())
    if not n:
        break
    res = prime_list(2*n+1)
    print(len([i for i in res if i > n]))

# def isPrime(x):
#     eraSieve = [True] * x
#     for i in range(2, int(x ** 0.5) + 1):
#         if eraSieve[i]:
#             for j in range(2 * i, x, i):
#                 eraSieve[j] = False
#     return [i for i in range(2, n) if eraSieve[i]]
#
#
# while True:
#     n = int(input())
#     if not n:
#         break
#     res = isPrime(2*n+1)
#     print(len([i for i in res if i > n]))
