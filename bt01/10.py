def find_triplets(arr):
    n = len(arr)
    triplets = []
    
    for i in range(n):
        # Tính vị trí của 3 số trong mảng
        first = i
        second = (i + 1) % n
        third = (i + 2) % n
        
        # Kiểm tra điều kiện số thứ 3 bằng tổng của 2 số đầu tiên
        if arr[first] + arr[second] == arr[third]:
            triplets.append((arr[first], arr[second], arr[third]))
    
    return triplets

# Mảng số nguyên ví dụ
arr = [5, 9, 2, 3, 5, 1, 1, 4, 7, 11, 15, 2, 4]

# Tìm và xuất các dãy thỏa mãn yêu cầu
triplets = find_triplets(arr)
for triplet in triplets:
    print(f"{triplet[0]} + {triplet[1]} = {triplet[2]}")
