total_sum = 0
count = 0
while True:
    user_input = input("Nhập một số nguyên dương (nhập số âm để kết thúc): ")
    if not user_input.isdigit() or int(user_input) < 0:
        break
    number = int(user_input)
    total_sum += number
    count += 1
    if count == 0:
       print("Không có số nguyên dương nào được nhập.")
    else:
       average = total_sum / count
       print(f"Trung bình cộng của {count} số nguyên dương là: {average}")
