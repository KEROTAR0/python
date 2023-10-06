def insertion_sort_recursive(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left_half = insertion_sort_recursive(arr[:mid])

	right_half = insertion_sort_recursive(arr[mid:])

	i, j = 0, 0
	sorted_arr = []
	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			sorted_arr.append(left_half[i])
			i += 1
		else:
			sorted_arr.append(right_half[j])
			j += 1
	sorted_arr += left_half[i:]
	sorted_arr += right_half[j:]

	return sorted_arr
arr = [5, 2, 4, 6, 1, 3]
sorted_arr = insertion_sort_recursive(arr)
print(sorted_arr)
