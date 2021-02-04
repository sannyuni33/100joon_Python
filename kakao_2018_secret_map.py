n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
bitmap1, bitmap2 = [], []
bitmap3 = [[0 for _ in range(n)] for _ in range(n)]
answer = ["" for _ in range(n)]

for i in range(n):
    tmp1 = list(bin(arr1[i])[2:].zfill(n))
    tmp2 = list(bin(arr2[i])[2:].zfill(n))
    bitmap1.append(tmp1)
    bitmap2.append(tmp2)
print(*bitmap1)
print(*bitmap2)
for i in range(n):
    for j in range(n):
        bitmap3[i][j] = int(bitmap1[i][j]) or int(bitmap2[i][j])
        if bitmap3[i][j]:
            answer[i] += '#'
        else:
            answer[i] += ' '
print(*bitmap3)
print(answer)