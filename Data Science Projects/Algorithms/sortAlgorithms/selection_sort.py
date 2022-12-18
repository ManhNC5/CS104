def selection_sort(arr):
  # Loop through the entire array
  for i in range(len(arr)):
    # Find the minimum element in the unsorted portion of the array
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    # Swap the minimum element with the first element of the unsorted portion
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

if __name__ == "__main__":
    selection_sort()