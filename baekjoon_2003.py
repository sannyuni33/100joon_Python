n, m = map(int, input().split())
lst = list(map(int, input().split()))
start = end = res = 0

while start + end < 2*len(lst):
    if sum(lst[start:end+1]) == m:
        res += 1
        start += 1
        end += 1
    elif sum(lst[start:end+1]) < m:
        end += 1
    else:
        start += 1

print(res)

# 이 문제는 투포인터 알고리즘 문제라는데, 투포인터가 뭐야?
# 1차원배열에서 두 개의 포인터. start, end 를 사용해서 원하는 결과를 얻는 알고리즘이란다.
# 리스트에서 start, end 를 옮겨가면서 sum[start:end] 이런식으로 m이 되는지 비교 ㄱㄱ

# 맞긴했는데 시간이 3112 ms...? 다른 사람들은 60 ms 대니까 개선안을 찾아보자