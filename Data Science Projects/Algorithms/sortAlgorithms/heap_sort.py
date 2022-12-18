def heap_sort(arr):
    # build a max heap
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, i, len(arr))

    # extract elements from the heap one by one
    for i in range(len(arr) - 1, 0, -1):
        # swap the root (maximum value) of the heap with the last element of the heap
        arr[0], arr[i] = arr[i], arr[0]
        # rebuild the heap with the remaining elements
        heapify(arr, 0, i)

def heapify(arr, root, heap_size):
    # find the largest element between the root and its children
    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child
    # if the largest element is not the root, swap it with the root and heapify the subtree
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, largest, heap_size)

if __name__ == "__name__":
    
    heap_sort()
