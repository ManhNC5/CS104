
def greedy_search(graph, start, end):
    
    queue = [(start, [start])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node not in visited:
            visited.add(node)
        if node == end:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            queue.append((neighbor, path + [neighbor]))
            return None
            
