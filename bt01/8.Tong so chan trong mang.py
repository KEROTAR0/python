def sum(arr):
    total_sum = 0

    for num in arr:
        if num % 2 == 0:
            total_sum += num

    return total_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = sum(numbers)

print("Mảng:", numbers)
print("Tổng các số chẵn trong mảng:", even_sum)
