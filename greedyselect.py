def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get user input for the list of numbers
select = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in select]

# Call the selection_sort function to sort the numbers
sorted_numbers = selection_sort(numbers)

# Print the sorted numbers
print("Sorted numbers:", sorted_numbers)
