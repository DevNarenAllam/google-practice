# DFS algorithm - non-recurive


def dfs(graph, start, visited):

    visited.add(start)

    print(start, end=' ')

    for _next in graph[start]:
        if _next not in visited:
            dfs(graph, _next, visited)



graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0', set())