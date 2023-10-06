def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n = int(input("Nhập một số nguyên dương n: "))
    if n < 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        result = factorial_iterative(n)
        print(f"{n}! = {result}")
except ValueError:
    print("Vui lòng nhập một số nguyên dương.")
