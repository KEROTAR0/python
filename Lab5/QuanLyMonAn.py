import tkinter as tk
import pyodbc
from tkinter import ttk

# Hàm để kết nối CSDL và hiển thị dữ liệu trong Data Grid View
def ket_noi_va_hien_thi():
    try:
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT MaMonAn, TenMonAn, DonViTinh, DonGia, TenNhom 
                       FROM master.dbo.MonAn, master.dbo.NhomMonAn  
                       where MonAn.Nhom = NhomMonAn.MaNhom 
                       """)
        rows = cursor.fetchall()
    
        # Xóa dữ liệu cũ trong Data Grid View
        for item in tree.get_children():
            tree.delete(item)
        
        # Hiển thị dữ liệu trong Data Grid View
        for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))
        
        conn.close()
        message_label.config(text="Kết nối thành công và hiển thị dữ liệu thành công!")
    except Exception as e:
        message_label.config(text="Lỗi khi kết nối hoặc hiển thị dữ liệu: " + str(e))  # Hiển thị lỗi

# Hàm để chọn nhóm món ăn từ Combobox
def chon_nhom_mon_an(event):
    selected_nhom = nhom_mon_an_combobox.get()
    # Tại đây, bạn có thể thực hiện việc hiển thị dữ liệu dựa trên nhóm món ăn đã chọn.
    # Ví dụ: hiển thị món ăn của nhóm món ăn đã chọn trong Data Grid View.
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý món ăn")

# Tạo tiêu đề
label = tk.Label(root, text="Danh sách món ăn", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=2, pady=10)  # Sử dụng grid để đặt tiêu đề ở hàng 0, cột 0 và căn giữa

# Tạo nút để kết nối và hiển thị dữ liệu
ket_noi_button = tk.Button(root, text="Menu", command=ket_noi_va_hien_thi)
ket_noi_button.grid(row=1, column=0, columnspan=2)

# Tạo Data Grid View
tree = ttk.Treeview(root, columns=("Mã Món Ăn", "Tên Món Ăn", "Đơn Vị Tính", "Đơn Giá", "Nhóm"), show="headings")
tree.heading("Mã Món Ăn", text="Mã Món Ăn")
tree.heading("Tên Món Ăn", text="Tên Món Ăn")
tree.heading("Đơn Vị Tính", text="Đơn Vị Tính")
tree.heading("Đơn Giá", text="Đơn Giá")
tree.heading("Nhóm", text="Nhóm")
tree.grid(row=2, column=1, columnspan=10)

# Label để hiển thị thông báo
message_label = tk.Label(root, text="", fg="red")
message_label.grid(row=3, column=1, columnspan=2)

# Chuỗi kết nối
connectionString = '''DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=.;DATABASE=QLMonAn,Encrypt=no'''

# Tạo Frame để đặt Combobox và tiêu đề "Nhóm món ăn" cùng hàng
frame_nhom_mon_an = tk.Frame(root)
frame_nhom_mon_an.grid(row=1, column=2, padx=10)  # Đặt frame ở hàng 1, cột 2 và có padding

# Label cho tiêu đề "Nhóm món ăn"
label_nhom_mon_an = tk.Label(frame_nhom_mon_an, )
label_nhom_mon_an.pack(side=tk.LEFT, padx=300,)  # Hiển thị label bên trái

# Tạo Combobox để chọn nhóm món ăn
nhom_mon_an_combobox = ttk.Combobox(frame_nhom_mon_an, values=["Hải sản", "Khai vị", "Bia- Nước ngọt", "Lẩu"])
nhom_mon_an_combobox.set("Chọn nhóm món ăn")
nhom_mon_an_combobox.pack(side=tk.RIGHT)  # Hiển thị Combobox bên phải

# Gắn sự kiện khi chọn nhóm món ăn
nhom_mon_an_combobox.bind("<<ComboboxSelected>>", chon_nhom_mon_an)

# Chạy ứng dụng
root.mainloop()