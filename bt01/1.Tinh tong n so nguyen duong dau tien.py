def sum_first_n_positive_integers(n):
    if n <= 0:
        return 0

    sum = (n * (n + 1)) // 2

    return sum

n = 5

result = sum_first_n_positive_integers(n)
print(f"Tổng của {n} số nguyên dương đầu tiên là: {result}")
