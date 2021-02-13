def turn(table):
    table.append(table.pop(0))


k = int(input())
n = int(input())
countDown = 210
firstIsBomb = [i for i in range(1, 9)]
for _ in range(k-1):
    turn(firstIsBomb)
for _ in range(n):
    t, z = map(str, input().split())
    countDown -= int(t)
    if countDown <= 0:
        break
    if z == 'T':
        turn(firstIsBomb)
print(firstIsBomb[0])

# k = int(input())
# n = int(input())
# countDown = 210
#
# for _ in range(n):
#     t, z = map(str, input().split())
#     countDown -= int(t)
#     if countDown <= 0:
#         break
#     if z == 'T':
#         k += 1
#         print('폭탄 받은 사람', k % 8)
# ans = k % 8 if k % 8 != 0 else 8
# print(ans)
# 사람수는 8명으로 고정, 3분30초는 210초
# 원형으로 앉아있고, 질문수는 최대 100개니까 큐로 구현하는게 좋겠고
# 폭탄 든 사람이 정해지면 걔부터 8명을 채운다.
# 정답을 맞추더라도 그 전에 시간이 다되면 터지니까 시간 줄이기를 먼저

# 큐로 구현한 버전은 64ms, 모듈로 연산 쓴 버전은 68ms
# 큐로 구현한거 다시 돌리니까 68ms 걸림. 시간복잡도는 똑같은듯