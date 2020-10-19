"""
20.07.22
1차시도 시간 초과
while True:
    height += a
    day += 1
    if v <= height:
        print(day)
        break
    if height < v:
        height -= b

2차시도 input() 대신에 sys.stdin.readline() => 시간 초과

3차시도 pypy3 언어로 시도 => 시간 초과

4차시도 시간 초과
while True:
    height += a
    day += 1
    if v <= height:
        print(day)
        break
    else:
        height -= b

5차시도 시간 초과
while v:
    v -= a
    day += 1
    if v <= 0:
        break
    v += b
print(day)
뭘 더 줄이란 거임? 파이썬으로 풀기가 가능하긴 함? 맞은 사람 있네 . ...... 많네....

...저녁먹고옴

반복문 쓰지 말고 몫이랑 나머지를 써서 어떻게 해볼 수 없나
이게 답인거같은데 짱구좀 굴려보자

v를 a-b 로 나누면 나머지는 a보다 크게 나올수가 없음. 무조건 a보다 작거나 같고..
v말고 v - a 를 a-b로 나눠줘야 하나?

6차시도 틀렸습니다
if v-a < a-b:
    print((v - a) // (a - b) + 2)
else:
    print((v - a) // (a - b) + 1)

7차시도 틀렸습니다
if a == v:
    print(1)
elif v-a < a-b:
    print((v - a) // (a - b) + 2)
else:
    print((v - a) // (a - b) + 1)

아무리 생각해봐도 v-a 를 나누면 안될 것 같아요
v % (a-b)로 다시가보자

20.07.27
v % (a-b) 를 하긴 하는데 1일을 언제 더해주고 언제 빼야하는지 구분을 명확히 해줘야 될 듯.

"""
import sys
a, b, v = map(int, sys.stdin.readline().split(' '))
day = v // (a-b)
if v % (a-b) == 0:
    print(day-1)
else:
    print(day) if ((a-b)*day)+b > v else print(day+1)