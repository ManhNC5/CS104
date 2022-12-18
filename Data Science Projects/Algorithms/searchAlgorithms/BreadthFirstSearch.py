from collections import deque

def breadth_first_search(graph, start, end):
        
    
    
    # create a queue for storing nodes to visit
    queue = deque([start])
    # create a set for storing visited nodes
    visited = set()

    while queue:
        # remove the first node from the queue
        node = queue.popleft()
        # mark the node as visited
        visited.add(node)

        # check if the node is the end node
        if node == end:
        return True

        # add the neighbors of the node to the queue
        for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)

    return False

if __name__ == "__main__":
    
    breadth_first_search()