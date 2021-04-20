res = []
while True:
    l, p, v = map(int, input().split())
    if not l:
        break
    a, b, tmp = v//p, v % p, 0
    if b < l:
        tmp += b
    else:
        tmp += l
    tmp += a*l
    res.append(tmp)
for r in range(len(res)):
    print('Case %d: %d' % (r + 1, res[r]))

# 그리디 알고리즘... 인데
# 전체 일수 v를 p로 나눈 몫과 나머지로 구분(a, b) 후 
# a 만큼 l 을 곱하고 나머지는 따로 연산했음. .. 이게 그리디 맞냐
# 순위권 코드 참고해도 알고리즘은 동일