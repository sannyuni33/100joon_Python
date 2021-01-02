n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]  # 숫자 리스트
check_number = [False] * n  # 중복숫자 체크
array = []  # 출력할 수열


def DFS(x):
    if x == m:  # 수열 m개를 충족할경우 출력
        print(*array)
        return

    for i in range(n):
        if check_number[i]:  # 중복될 경우 패스
            continue

        array.append(number_list[i])  # 수열 추가
        check_number[i] = True  # 사용한 수 체크

        DFS(x + 1)  # + 1번째 수열을 위해 재귀함수 호출

        array.pop()  # 수열 마지막 자리 삭제
        check_number[i] = False  # 사용한 수 초기화


DFS(0)

# 백트래킹을 찾아보니까는 DFS 이야기가 먼저 나옴.
# DFS 는 가능한 모든 경로를 탐색하는 애고,
# 백트래킹은 모든 경로를 찾다가 지금 경로가 안 될것 같으면 중지하고 돌아감.
# 그래서 백트래킹 코드를 참고해보면
# DFS 함수를 돌리는데, 중간에 이 경로가 갠춘할지 아닐지 판단하는 함수가 또 있음.

# 그렇다면 이 문제에 적용을 하면 어떻게 해야겠냐,
# 우선은 1 부터 N 까지 for 문을 돌면서 얘들을 다 시작점으로 DFS 수행.
# 1부터 N 까지의 수가 있다면 얘네들을 어떻게 연결해줘야
# 의도에 맞게 DFS 를 활용할 수 있냐
# 2에서 1, 3, 4 다 갈 수 있음.. 그럼 모든 노드가 서로 연결된 형태.

# https://leejunggae.tistory.com/19
# 참고한 코드에서 핵심적인 부분은 for 문, 재귀호출 후 끝을 삭제 처리해주는 부분임.
# 백트래킹 알고리즘에서 요런 코드가 어떻게 나오는 것인지 연구필요.
# 시간은 224ms