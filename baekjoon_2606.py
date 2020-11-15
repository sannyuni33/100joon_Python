numOfCom = int(input())
numOfEdge = int(input())
graph = [[] for _ in range(numOfCom)]

for _ in range(numOfEdge):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

visited = []
stack = [1]

while stack:
    n = stack.pop()
    if n not in visited:
        visited.append(n)
        if len(graph[n-1]) > 0:
            temp = list(set(graph[n-1]) - set(visited))  # 얘가 핵심코드
            temp.sort(reverse=True)
            stack += temp
print(len(visited)-1)
# 그래프 나타내는 리스트 만들고 DFS 쓰면 끝?
# 그러네요 끝나네요