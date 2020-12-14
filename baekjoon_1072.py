# 몇 판을 해야 승률이 오를런지는 프로그램이 끝나야지만 알 수 있다...
# 즉 이분탐색에서는 경기 수 x 를 넣어서 연산한 승률을 가지고 비교를 해야하는 것
def binarySearch(lst, n):  # n 은 찾아야하는 승률값. 변할 수 없음.
    start, end = 0, len(lst)-1
    mid = (start+end)//2
    while start < end:
        newZ = int((y + lst[mid] - x) / lst[mid] * 100)
        print(newZ)
        if newZ == n:  # newZ 는 확률
            return lst[mid]  # 그 확률을 나오게 한 경기수를 리턴
        elif newZ < n:
            start = mid + 1
        else:
            end = mid
        mid = (start+end)//2
        print('next list: ', lst[start:end+1])
    return -1


x, y = map(int, input().split())
if x == y:
    print(-1)
else:
    defeatedGame = x-y
    z = int((y/x)*100)  # 승률값
    BSrange = [i for i in range(x+1, 2*x+1)]
    # 이 리스트에 대해서 이분탐색을 할거임.
    # 이렇게해도 틀렸다고하면 나올때까지 리스트 다시 만들어주는 식으로 할거임.
    print(binarySearch(BSrange, z+1) - x)


# if x == y:
#     print(-1)
# else:
#     init = int((y/x)*100)
#     z = init
#     term = 10**len(str(x))-1
#     while z <= init:
#         x += term
#         y += term
#         z = int((y/x)*100)
#         if z > init:  # 승률의 변화가 감지되었다...!
#             x -= term
#             y -= term
#             for i in range(term):  # 정확히 어디서 변했는지...!
#                 x += 1
#                 y += 1
#                 z = int((y/x)*100)
#                 if z > init:  # 정확히 여기서 변했다...!
#                     break
#     print(x-tmp)

# 1 씩 더해가면서 찾지말구 주기를 두고 더하면서 찾자(시간초과 예방)
# 이것도 시간초과가 걸리는게 ..
# x = 1,000,000,000 이고 y = 0 이면 term 이 100,000,000 이니까 여기서도 겁나 반복.
# term = 10**len(str(x))-1 일땐 시간초과, term = 10000 일땐 틀렸다?

# 아... 근데 이거 이분탐색 문제랬는데...
# 이분탐색의 아이디어는 절반씩 줄여나가는 것.
# 찾고자하는 값은 뭐냐.. init 보다 1 큰거. 또는 init 이 1 커지게 하는 게임 수
# 게임 수의 값을 찾고자하는데, 범위가 명확하지 않은 상태에서 이분탐색을 할 수 있나?
# 범위가 명확하지 않다고 한 이유는 x 와 y 가 같이 1씩 늘어나기 때문임
# 그러면 x 값의 절반만큼을 범위로 정해주고 거기서 안나오면 또 그만큼 더해서 ...?
# 출제의도가 이게 아닐 것 같은디 ...
# 이분탐색을 수행할 범위를 딱 찝을 수 있는지 없는지가 관건

# 진 게임을 가지고 해볼수는 없나... 이긴 게임은 계속 늘어나지만 진 게임 수는 고정
# 근데 소수점을 버리는게 영향을 끼칠 우려가 존재
# 생각해보니까 안됨. 절대 안됨. 소수점 아래 때문에
# 아 아닌가 1에서 빼주면 상관없나...

# 메모리 초과가 뜨는 이유가 멀까.
# 재귀함수를 쓰니까 이렇게 되는거같은디 ,,,
# 재귀쓰지말고 함수내에서 while 문으로 끝낼 수 있을걸?!