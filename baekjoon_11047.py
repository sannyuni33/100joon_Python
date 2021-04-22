n, k = map(int, input().split())
w, res = [], 0
for _ in range(n):
    w.append(int(input()))

# k보다 비싼 동전 날려버리기
w.append(k)
w.sort(reverse=True)
idx = w.index(k)
w = w[idx+1:]

curr = 0
while k:  # 첫 번째 동전은 무조건 1원이니까 마지막엔 무조건 0이 됨.
    res += k//w[curr]
    k %= w[curr]
    curr += 1

print(res)


# 1. k 원보다 비싼 동전은 당연히 필요 없으니까 날려버리고
# 2. k 원보다 값싼 동전 중 제일 비싼거부터 사용
# 3. k // 비싼거 계산결과를 res 에 더해주고,
# 4. 몫 // 그 다음 비싼거 계산결과를 res 에 더해주는 과정을 반복하면 될 듯.

# 해결완료!