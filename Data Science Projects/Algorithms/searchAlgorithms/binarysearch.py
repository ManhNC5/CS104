
def binary_search(arr, target):

    # Set the initial low and high indices
    low = 0
    high = len(arr) - 1
    
    # Loop until the low index is greater than the high index
    while low <= high:
        # Calculate the midpoint index
        mid = (low + high) // 2
        
        # If the target is less than the value at the midpoint index,
        # set the high index to the midpoint - 1
        if target < arr[mid]:
            high = mid - 1
        # If the target is greater than the value at the midpoint index,
        # set the low index to the midpoint + 1
        elif target > arr[mid]:
            low = mid + 1
        # If the target is equal to the value at the midpoint index,
        # return the midpoint index
        else:
            return mid
    
    # If the target was not found, return -1
    return -1

if __name__ == "__main__":
    
    binary_search()