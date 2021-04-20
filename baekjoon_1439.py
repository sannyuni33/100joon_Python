s = input()
ls0 = s.split('1')
ls1 = s.split('0')

count0, count1 = 0, 0
for i in ls0:
    if len(i):
        count0 += 1

for i in ls1:
    if len(i):
        count1 += 1

print(min(count0, count1))
# 101010 이라는 문자열이라면 3이 답이겠음. 1 이든 0 이든 세 개로 찢어져있음.
# 111111111110000 이라는 문자열이라면 1이 답. 1 이든 0이든 다 붙어있으니 둘 중 하나만.
# 연속0이랑 연속1로 찢은다음 더 적은수에 맞춰서 출력했더니 76 ms 로 성공