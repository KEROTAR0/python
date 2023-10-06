def check_number(num):
    if num > 0:
        return 1 
    elif num < 0:
        return -1
    else:
        return 0

try:
    user_input = float(input("Nhập một số: "))
    result = check_number(user_input)
    print("Kết quả:", result)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
