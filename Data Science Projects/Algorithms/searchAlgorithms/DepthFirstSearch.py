def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

if __name__ == "__main__":
    
    depth_first_search()