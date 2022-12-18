
def radix_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Set the number of digits in the maximum element
    max_digits = len(str(max_element))

    # Initialize the base
    base = 1

    # Iterate through the digits
    for i in range(max_digits):
        # Initialize an empty list to store the digits
        digit_list = [[] for _ in range(10)]

        # Iterate through the elements in the array
        for element in arr:
            # Extract the digit at the current base
            digit = (element // base) % 10

            # Append the element to the appropriate list
            digit_list[digit].append(element)

        # Initialize an empty list to store the sorted elements
        sorted_list = []

        # Iterate through the lists of digits
        for digit in digit_list:
            # Append the elements in each list to the sorted list
            sorted_list.extend(digit)

        # Update the array with the sorted list
        arr = sorted_list

        # Update the base
        base *= 10

    # Return the sorted array
    return arr

if __name__ == "__main__":
    
    radix_sort()