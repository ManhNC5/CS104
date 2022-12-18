def search(start, goal, graph):
    # Set the initial depth limit to 0
    depth_limit = 0
    while True:
        # Perform a depth-limited search with the current depth limit
        result = depth_limited_search(start, goal, graph, depth_limit)
        # If the search was successful, return the result
        if result != "cutoff":
            return result
        # If the search was not successful, increase the depth limit and try again
        depth_limit += 1

def depth_limited_search(start, goal, graph, depth_limit):
    # If the depth limit has been reached, return "cutoff"
    if depth_limit == 0:
        return "cutoff"
    # If the start state is the goal state, return "success"
    if start == goal:
        return "success"
    # Set the result to "cutoff"
    result = "cutoff"
    # Iterate over the children of the start state
    for child in graph[start]:
        # Recursively search the child, with the depth limit decreased by 1
        result = depth_limited_search(child, goal, graph, depth_limit - 1)
        # If the search was successful, return the result
        if result == "success":
            return "success"
    # Return the result
    return result

if __name__ == "__main__":
    
    depth_limited_search()