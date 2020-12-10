n = int(input())
ropes = []
maxW = 0
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)
for i in range(len(ropes)):
    w = ropes[i]
    tmpW = w*(i+1)
    if tmpW > maxW:
        maxW = tmpW
print(maxW)

# ropes = []
# maxW = 0
# for _ in range(n):
#     ropes.append(int(input()))
#     tmpW = min(ropes)*len(ropes)
#     print(ropes)
#     print(tmpW)
#     if tmpW > maxW:
#         maxW = tmpW
# print(maxW)

# ropes.sort(reverse=True)
# avg = sum(ropes, 0.0)/len(ropes)
#
# for i in range(len(ropes)):
#     if ropes[i] < avg:
#         ropes = ropes[:i]  # 평균보다 높은 로프만 살린다
#         break
#
# print(min(ropes)*len(ropes))

# n = 1 ~ 100,000 개의 로프가 있고...
# 중량이 w 인 물체를 들면 로프마다 w/n 만큼의 중량이 걸림
# 각 로프마다 견딜 수 있는 중량이 다르다 하고 n 개 로프 각각의 최대 중량이 주어지면
# w 의 최대값을 구하는 문제.
# 골때리는 부분은 모든 로프를 사용안해도 된다는 말.
# 견딜수있는 중량이 낮은 몇몇 로프는 없는게 더 도움된다는 뜻
# 로프 중량 리스트를 돌면서 max 값을 갈아치우는 식으로 했더니 시간초과.

# 로프가 견디는 중량값들의 평균을 구하고, 평균이하의 로프는 안쳐주는 식으로?
# 로 했더니... 예제 입력1 넣으면 15가 나와버림.

# 그러면 첫 번째 시도랑 두 번째 시도 방식을 합쳐서 ..
# 내림차순한 다음 max 값을 갱신하면...
# 최대 중량값이 계속 높아지다가 낮아지는 고점이 발생할 듯. 아마도 평균 근처
# 거기서 스탑!!!
# 이건 틀렸다고?

# min() 함수가 리스트 전체를 도는건지... min 말고 그냥 맨 뒷자리꺼가지고
# 계산하니까 문제는 맞았는데 시간이 4864ms...
# 맞은 사람들 보니까 1등만 136ms, 그 다음은 3948, 4632, ... 3 ~ 4 천대 나오긴 함