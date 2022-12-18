def bi_directional_search(graph, start, goal):
    # Create two sets to keep track of the visited nodes in each direction
    start_visited = set()
    goal_visited = set()
    
    # Create two queues to store the nodes that need to be explored in each direction
    start_queue = Queue()
    goal_queue = Queue()
    
    # Enqueue the start and goal nodes in their respective queues
    start_queue.put(start)
    goal_queue.put(goal)
    
    # Create a dictionary to store the parent of each node in each direction
    start_parents = {start: None}
    goal_parents = {goal: None}
    
    # Create a variable to keep track of whether the search has reached the goal
    found = False
    
    # Continue the search until one of the queues is empty
    while not start_queue.empty() and not goal_queue.empty():
        # Explore the next node in the start direction
        current_start = start_queue.get()
        if current_start in goal_visited:
            # If the current node has been visited in the other direction, then a path has been found
            found = True
            break
        for neighbor in graph[current_start]:
            if neighbor not in start_visited:
                # Mark the neighbor as visited and add it to the queue
                start_visited.add(neighbor)
                start_queue.put(neighbor)
                start_parents[neighbor] = current_start
        
        # Explore the next node in the goal direction
        current_goal = goal_queue.get()
        if current_goal in start_visited:
            # If the current node has been visited in the other direction, then a path has been found
            found = True
            break
        for neighbor in graph[current_goal]:
            if neighbor not in goal_visited:
                # Mark the neighbor as visited and add it to the queue
                goal_visited.add(neighbor)
                goal_queue.put(neighbor)
                goal_parents[neighbor] = current_goal
    
    if found:
        # If a path has been found, then trace the path back from the start and goal nodes
        path = trace_path(start_parents, start, goal_parents, goal)
        return path
    else:
        # If no path was found, return None
        return None

def trace_path(start_parents, start, goal_parents, goal):
    # Create an empty list to store the path
    path = []
    
    # Trace the path back from the start node
    current_node = start
    while current_node is not None:
        path.append(current_node)
        current_node = start_parents[current_node]
    
    # Reverse the path
    path = path[::-1]
    
    return path

if __name__ == "__main__":
    
    bi_directional_search()
