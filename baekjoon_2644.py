def DFS(s, e, g):
    visited = [False]*n  # 방문여부
    stack = [[s, 0]]  # 시작점, 스택에는 각 노드들까지 가는데 걸린 단계를 [1]에 저장
    while len(stack) > 0:
        tmp = stack.pop()  # 스택에 있는거 꺼내면,
        visited[tmp[0]-1] = True  # 방문 처리하고
        print(tmp[0], 'has popped')

        if e in g[tmp[0]-1]:
            print('bingo!')
            print(tmp[1]+1)
            exit()

        for t in g[tmp[0]-1]:  # 연결된 정점중 방문안한 애들을 스택에 넣음
            if not visited[t-1]:
                stack.append([t, tmp[1]+1])
    print(-1)


n = int(input())
graph = [[] for _ in range(n)]
start, end = map(int, input().split())
edgeNum = int(input())

for _ in range(edgeNum):
    x, y = map(int, input().split())
    graph[x-1].append(y)
    graph[y-1].append(x)

DFS(start, end, graph)


# 인접행렬은 정점에비해 간선이 적으면 개손해(행렬 전체를 탐색하니깐)
# 인접리스트는 연결여부를 확인할때 비효율(x 정점이랑 연결된 애들중에 y가 있는지 봐야함)
# 이 문제에서는 어떤 자료구조가 더 적절할까~요

# 인접리스트로 해결 시도 고고
# 마자따. 68ms