"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p149, 음료수 얼려 먹기]
난이도 1.5/3, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB
1 <= N <= 1000
1 <= M <= 1000
"""

n, m = map(int, input().split())

frame = []
for i in range(n):
    frame.append(list(map(int, input())))

graph = dict()
for y in range(n):
    for x in range(m):
        graph[(y, x)] = []

# construct a graph for each node
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]  # Up Right Down Left
for y in range(n):
    for x in range(m):
        # For each node, find adjacent nodes
        if frame[y][x] == 0:
            for direction in range(4):
                if y + dy[direction] >= n or x + dx[direction] >= m \
                        or y + dy[direction] < 0 or x + dx[direction] < 0:
                    continue

                if frame[y + dy[direction]][x + dx[direction]] == 0:
                    graph[(y, x)].append((y + dy[direction], x + dx[direction]))


# Depth-first search nodes
def dfs(graph, node, visited):
    visited[node] = True

    for adjacent_node in graph[node]:
        if not visited[adjacent_node]:
            dfs(graph, adjacent_node, visited)


counter = 0
visited = dict()
for y in range(n):
    for x in range(m):
        visited[(y, x)] = False

for node in graph:
    if not visited[node] and frame[node[0]][node[1]] == 0:
        counter += 1
        dfs(graph, node, visited)

print(counter)
