import heapq

# A function to perform the uniform cost search
def uc_search(start, goal, grid):
    
    # Create a priority queue to store the states we need to visit
    pq = []
    
    # Add the start state to the queue
    heapq.heappush(pq, (0, start))

    # Create a set to store the states we have already visited
    visited = set()

    # Keep searching until the queue is empty
    while pq:
        # Get the state with the lowest cost
        cost, state = heapq.heappop(pq)
        # Check if we have reached the goal state
        if state == goal:
            return cost
        
        # Mark the state as visited
        visited.add(state)
        
        # Get a list of all the possible next states
        next_states = get_next_states(state, grid)
        
        # Add the next states to the queue, if they have not been visited yet
        for next_state in next_states:
            if next_state not in visited:
                # Calculate the cost to reach this state
                next_cost = cost + get_cost(state, next_state)
                # Add the state to the queue
                heapq.heappush(pq, (next_cost, next_state))

    # If we reach here, it means we were unable to find a path to the goal
    return -1

if __name__ == "__main__":
    
    uc_search()