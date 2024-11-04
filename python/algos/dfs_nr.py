def dfs(graph):
    stack = []
    visited = set()
    
    for node in graph:
        if node not in visited:
            stack.append(node)
            visited.add(node)
            while stack:
                cur_node = stack.pop()
                print(cur_node)
                for _node in graph[cur_node]:
                    if _node not in visited:
                        stack.append(_node)
                        visited.add(_node)
                             
graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

dfs(graph)

