n = list(input())
resList = [0 for _ in range(9)]
for _ in range(len(n)):
    x = int(n.pop())
    if x == 9:
        resList[6] += 1
    else:
        resList[x] += 1

if resList[6] % 2 == 0:  # 6과 9를 같이 카운팅했기 때문에 처리
    resList[6] //= 2
elif resList[6] > 1:
    resList[6] = (resList[6]+1) // 2
print(max(resList))

# n 의 범위는 0부터 100만까지.
# 최대 세트 갯수는 100만일때 6개, 여섯자리 일땐 6개 다섯자리 일땐 5개...(같은 수로)
# 0일때는 당연히 한 개고
# 고려해야 할 부분은 9와 6을 뒤집어서 쓸 수 있다는 것.
# 이걸 어떤식으로 구현할거냐.
# 숫자로 받지말고 문자열로 받아서 나눌까. -> len 하면 몇자리 수인지 나옴.
# 한 번 나왔던 숫자가 나올때마다 세트의 수를 1씩 더해주고 싶은데,
# 9와 6은 합해서 1번, 3번, 5번 나올때마다 카운트가 올라감.
# 살짝 다른 접근 방식으로 해본다면.
# 모든 요소를 다 카운팅해주고. 카운팅 수가 가장 높은 놈이 세트의 수가 되겠지.
# 이때 9와 6을 같이 세주고, 그 수에 대해 2로 나눈다는지 하는 식으로 처리한 뒤에
# 카운팅 된 수 중 max 값을 찾는 것이 순서가 맞고.
# 굳이 딕셔너리 안쓰고 리스트에서 해결 가능. (딕셔너리가 가독성은 좋을지도)
# 9와 6에 대한 처리는 짝수면 2로 나누고, 홀수면 +1 한걸 2로 나누고. 1이면 그대로
# 1차 시도가 틀렸다. 머가 틀렸을까.
# 아놔 리스트 출력하는거 안지워서 틀림요 ;;;;;;;;;;;;;;;;;;;;;;;;;;