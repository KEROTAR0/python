'''
def bubbleSort(arr):
	n = len(arr)
	swapped = False

	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
'''

def bubblesort(elements):
	swapped = False

	for n in range(len(elements)-1, 0, -1):
		for i in range(n):
			if elements[i] > elements[i + 1]:
				swapped = True

				elements[i], elements[i + 1] = elements[i + 1], elements[i]	 
		if not swapped:
			return

elements = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)
