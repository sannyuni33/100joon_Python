def solution(array, commands):
    answer = []
    for x in commands:
        arr = sorted(array[x[0]-1:x[1]])
        answer.append(arr[x[2]-1])
    return answer

# 보자마자 그냥 바로 풀었다.
# 파이썬이라서 슬라이싱이랑 sorted 쓴게 편했던듯
# 근데 다른 풀이 보니까

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 이런것도 있었다...