while True:
    user_input = input("Nhập một số nguyên (nhập 'exit' để kết thúc): ")

    if user_input.lower() == 'exit':
        break

    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} là số chẵn.")
        else:
           print(f"{number} là số lẻ.")
    else:
        print("Vui lòng nhập một số nguyên.")
