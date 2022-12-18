def bubble_sort(arr):
    # Set a flag to track whether any swaps were made
    swaps_made = True
    
    # Keep looping until no swaps are made
    while swaps_made:
        # Set the flag to False
        swaps_made = False
        
        # Loop through the array, comparing each pair of adjacent elements
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # If the elements are out of order, swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Set the flag to True to indicate that a swap was made
                swaps_made = True

if __name__ == "__main__":
    bubble_sort()
