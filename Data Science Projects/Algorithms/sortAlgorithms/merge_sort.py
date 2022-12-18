
def merge_sort(arr):
    # base case: if the array has fewer than 2 elements, it is already sorted
    if len(arr) < 2:
        return arr
    
    # split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # merge the sorted halves and return the result
    return merge(left, right)

def merge(left, right):
    # create an empty result array
    result = []
    
    # while there are elements in both arrays, append the smaller element
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    # if one of the arrays is not empty, append the remaining elements
    result.extend(left)
    result.extend(right)
    
    return result


if __name__ == "__main__":
    
    merge_sort()