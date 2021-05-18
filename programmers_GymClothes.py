def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)  # 2벌 가진 넘들
    set_lost = set(lost)-set(reserve)  # 땡벌
    for i in set_reserve:  # 2벌 가진 넘 양옆을 왼쪽부터 본다
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

# def solution(n, lost, reserve):
#     attend = [1 for _ in range(n)]  # 0번부터 n-1번까지 ^^
#     for r in reserve:
#         attend[r-1] += 1
#     for l in lost:
#         attend[l-1] -= 1
#     print('before:', attend)
#
#     for i in range(1, n-1):
#         if not attend[i]:
#             if attend[i-1] == 2:
#                 attend[i-1] -= 1
#                 attend[i] += 1
#                 continue
#             elif attend[i+1] == 2:
#                 attend[i+1] -= 1
#                 attend[i] += 1
#                 continue
#
#     if not attend[0] and attend[1] == 2:
#         attend[1] -= 1
#         attend[0] += 1
#     if not attend[-1] and attend[-2] == 2:
#         attend[-2] -= 1
#         attend[-1] += 1
#     print('after:', attend)
#
#     print(n - attend.count(0))
#     return n - attend.count(0)


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
solution(15, [1, 2, 4, 13, 14, 15], [3, 9, 14])

# 첫 번째 접근
# 모든 애들의 체육복은 1벌
# reserve 에 있는 애들껀 2로 증가.
# lost 에 있는 애들껀 -1 한다.
# 그 다음 그리디로

# 두 번째 접근
# for i in range(1, n+1) 을 돌면서
# reserve 에 있을때와 lost 에 있을때의 프로세스를 정의한다.

# 세 번째 접근... 오픈소스
#
