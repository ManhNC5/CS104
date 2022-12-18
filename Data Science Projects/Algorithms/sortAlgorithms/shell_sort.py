def shell_sort(arr):
  # Start with a gap value equal to half the length of the array
  gap = len(arr) // 2
  while gap > 0:
    for i in range(gap, len(arr)):
      temp = arr[i]
      j = i
      # Shift elements that are greater than temp down the gap
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    # Reduce the gap value by half
    gap //= 2

# Test the shell sort function
# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# shell_sort(arr)
# print(arr)
