import heapq

def dijkstra(graph, start, end):
    # create a heap to store the distances of the vertices
    heap = []
    # initialize the distances to infinity
    distances = {vertex: float('inf') for vertex in graph}
    # set the distance of the start vertex to 0
    distances[start] = 0
    # add the start vertex to the heap
    heapq.heappush(heap, (0, start))
    # create a set to store the visited vertices
    visited = set()

    # while there are vertices in the heap
    while heap:
        # pop the vertex with the smallest distance from the heap
        distance, vertex = heapq.heappop(heap)
        # if the vertex has not been visited
        if vertex not in visited:
            # add it to the visited set
            visited.add(vertex)
            # for each neighbor of the vertex
            for neighbor in graph[vertex]:
                # if the distance to the neighbor is smaller than the current distance
                if distance + graph[vertex][neighbor] < distances[neighbor]:
                    # update the distance to the neighbor
                    distances[neighbor] = distance + graph[vertex][neighbor]
                    # add the neighbor to the heap
                    heapq.heappush(heap, (distances[neighbor], neighbor))

    # return the distance to the end vertex
    return distances[end]

if __name__ == "__main__":
    
    dijkstra()