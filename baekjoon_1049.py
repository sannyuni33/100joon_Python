packList, pieceList = [], []
n, m = map(int, input().split())

for _ in range(m):
    package, piece = map(int, input().split())
    packList.append(package)
    pieceList.append(piece)
packMin = min(packList)
pieceMin = min(pieceList)
x, y = n // 6, n % 6  # x 는 패키지 구매 개수, y 는 낱개 구매 개수

if packMin > pieceMin:
    if packMin > pieceMin*6:
        res = n*pieceMin
    elif pieceMin*y >= packMin:
        res = (x+1)*packMin
    else:
        res = x*packMin + y*pieceMin
else:
    res = (x+1)*packMin
print(res)

# 각 행은 각 브랜드의 패키지 가격(6개), 낱개 가격(1개)
# 끊어진 기타줄 갯수를 채우기 위해 6의 배수 + 6으로 나눈 나머지로 채워야하고
# 그만큼 해당하는 가격을 곱해주면 되겠다
# 예제 입력 1의 경우는 어떻게 나온거냐면...
# 4개가 끊어졌는데 낱개로 사면 3*4 = 12 이고, 12*1 = 12 임.
# 예제 입력 2의 경우는
# 10개가 끊어짐, 6개는 패키지 가격 중 가장 낮은 20, 4개는 낱개 가격 중 가장 낮은 4
# 20*1 + 4*4 = 36이 나왔음

# 첫 번째로.. 패키지, 낱개 가격 각각 가장 낮은 값을 알고 있어야하고,
# 두 번째로 그 낱개 가격으로 몇 개를 사면 차라리 패키지로 사는게 나은지 알아야 함

# 예제 입력 1 2 3 은 다 맞게 나오는데... 이렇게 간단히 풀릴리가 없음
# 채점 중 5%까진가 갔다가 틀림. 이제부턴 반례 찾기다

# 어떤 반례가 있을까 packMin 이 pieceMin 보다 작은 경우?
# 그런 입력이 들어오지 않는다는 말은 없음
# 그리고 0도 입력으로 들어올 수 있음.

# 6개를 싹 다 낱개로 사도 packMin 보다 저렴한 경우는? -> res = n*pieceMin 이 맞음
# 살짝 손봤더니 예제 입력 3 이 320이 떠버리는데 ...
# if elif 문으로 했더니 30%까지 가고 틀림.
