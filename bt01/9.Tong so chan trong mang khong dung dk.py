def sum_even_numbers(arr):
    total_sum = 0

    for num in arr:
        total_sum += num & 1  # Kiểm tra tính chẵn bằng phép AND với 1

    return total_sum

# Khởi tạo một mảng
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tổng số chẵn trong mảng
even_sum = sum_even_numbers(numbers)

print("Mảng:", numbers)
print("Tổng số chẵn trong mảng:", even_sum)
