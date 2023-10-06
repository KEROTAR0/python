def xet(num):
    parity = [0, 1]  # Danh sách các giá trị tương ứng với số chẵn và số lẻ
    return parity[num % 2]  # Trả về 0 nếu số chẵn, 1 nếu số lẻ

# Nhập số từ người dùng
try:
    user_input = int(input("Nhập một số: "))
    result = xet(user_input)
    if result == 0:
        print("Số chẵn.")
    else:
        print("Số lẻ.")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
