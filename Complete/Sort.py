def optimized_quadratic_sort(arr):
    n = len(arr)
    last_chosen = 0
    while n > 1:
        max_idx = last_chosen
        min_idx = last_chosen
        swapped = False
        for i in range(last_chosen, n):
            if arr[i] > arr[max_idx]:
                max_idx = i
            if arr[i] < arr[min_idx]:
                min_idx = i
        if max_idx != n - 1:
            arr[max_idx], arr[n - 1] = arr[n - 1], arr[max_idx]
            swapped = True
        if min_idx == n - 1:
            min_idx = max_idx
        if min_idx != last_chosen:
            arr[min_idx], arr[last_chosen] = arr[last_chosen], arr[min_idx]
            swapped = True
        if not swapped:
            break
        last_chosen += 1
        n -= 1
    return arr


unsorted_array = [19, 5, 20, 2, 9, 12, 1, 14, 5, 6, 6, 18, 17, 3, 8, 3, 11, 2,
                  7, 24, 1, 9, 10, 15, 16, 18, 21, 2, 16, 20, 16, 27, 16, 26,
                  31, 1, 40, 22, 31, 21, 11, 7, 3, 9, 10, 11, 31, 41, 51, 45,
                  33, 38, 29, 18, 36, 31, 11, 9, 6, 3, 12, 16, 21, 24, 14, 33, 4]
sorted_array = optimized_quadratic_sort(unsorted_array)
print("Sorted array:", sorted_array)
