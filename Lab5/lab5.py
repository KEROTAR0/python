#1. Kết nối tới cơ sở dữ liệu và lấy thông tin phiên bản

# cách đơn giản nhất kết nối CSDL và lấy phiên bản hệ quản trị CSDL SQL server
'''
import pyodbc 

conn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P7KU7A4I\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes')
cursor = conn.cursor()
cursor.execute("Select @@version")
db_version = cursor.fetchone()
conn.close()
print("Bạn đang dùng hệ quản trị CSDL SQL Server phiên bản ", db_version)'''


# cách lấy phiên bản hệ quàn trị CSDL SQLite, đã tổ chức thành các 
# hàm kết nối và đóng kết nối riêng biệt, có sử dụng try… exception … 
# để xử lý nếu có lỗi xảy ra khi kết nối và thực thi truy vấn
'''
import sqlite3
def get_connection():
        connection = sqlite3.connect('QLSinhVien.db') 
        return connection
def close_connection(connection):
    if connection:
        connection.close()
def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("Bạn đang sử dụng SQLite phiên bản: ", db_version) 
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)
read_database_version()'''

#2. Lấy danh sách của lớp học, sinh viên:
#a danh sách lớp
'''from unittest import result
import pyodbc
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P7KU7A4I\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes")
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách các lớp là: ") 
        for row in records:
            print("*"*108)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error: 
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
get_all_class()'''

#b danh sách lớp và sinh viên
'''from unittest import result
import pyodbc
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P7KU7A4I\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes")
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
        select SinhVien.ID as "Mã số",HoTen,MaLop,TenLop
        from QLSinhVien.dbo.SinhVien,QLSinhVien.dbo.Lop
        where SinhVien.MaLop=Lop.ID
        """
        cursor.execute(select_query)
        result = cursor.fetchall()
        print(f"Danh sách tất cả các sinh viên là: ")
        print(f"Mã số        Họ tên        Mã lớp          Tên lớp")
        
        for i, row in enumerate(result, start=1):
            ID = row[0]
            HoTen = row[1]
            MaLop = row[2]
            TenLop = row[3]
            # Định dạng thông tin để căn chỉnh
            print(f"{ID:<5}  {HoTen:<20}  {MaLop:<13}  {TenLop}")
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error: 
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
get_all_class()'''

#3. Lấy thông tin lớp học, sinh viên theo mã:
#a Lấy thông tin lớp học
'''import pyodbc
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P7KU7A4I\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes")
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()
def get_class_by_id(class_id):
    try:
        connection = get_connection() 
        cursor = connection.cursor()
        # dấu "?" chính là placeholder, điểm đánh dấu vị trí tham số được truyền vào 
        select_query = "select * from Lop where id= ?"
        # danh sách tham số sẽ truyền vào câu truy vấn
        params = (class_id,) 
        cursor.execute(select_query, params)
        record = cursor.fetchone()
        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", record[0])
        print("Tên lớp: ", record[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
get_class_by_id(1)'''

#b Sinh viên theo mã lớp:
'''import pyodbc
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P7KU7A4I\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes")
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()
def get_student_by_id_class(class_id):
    try:
        connection = get_connection() 
        cursor = connection.cursor()
        # dấu "?" chính là placeholder, điểm đánh dấu vị trí tham số được truyền vào 
        # Truy vấn SQL để lấy danh sách sinh viên theo mã lớp
        select_query = "select * from SinhVien where MaLop= ?" # tìm sv theo mã sv|| select_query = "select * from SinhVien where ID= ?"
        # danh sách tham số sẽ truyền vào mã lớp
        params = (class_id,) 
        cursor.execute(select_query, params)
        records = cursor.fetchall()
        if records:
            print(f"Danh sách sinh viên có mã = {class_id} là: ")
            for record in records:
                print("Mã sinh viên: ", record[0])
                print("Họ và tên: ", record[1])
        else:
            print(f"Không tìm thấy mã {class_id} tồn tại")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
# Tìm sv bằng mã lớp
get_student_by_id_class(2)'''

#c Hiển thị danh sách sinh viên theo lớp (khi biết mã lớp/tên lớp)
'''import pyodbc

connectionString = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-P7KU7A4I\\SQLEXPRESS;"
    "DATABASE=QLSinhVien;"
    "Trusted_Connection=yes"
)

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_student_in_class(class_id, class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
        select SinhVien.ID as "Mã số", HoTen, MaLop, TenLop
        from SinhVien, Lop
        where SinhVien.MaLop=Lop.ID 
        and SinhVien.MaLop = ? AND Lop.TenLop = ?
        """

        params = (class_id, class_name)
        cursor.execute(select_query, params)
        records = cursor.fetchall()
        if records:
            print(f"Danh sách sinh viên theo lớp {class_id} - {class_name}:")
            print(f"Mã số    Họ tên             Mã lớp       Tên lớp")
            for row in records:
                ID = row[0]
                HoTen = row[1]
                MaLop = row[2]
                TenLop = row[3]
                # Định dạng thông tin để căn chỉnh
                print(f"{ID:<8}  {HoTen:<20}  {MaLop:<7}  {TenLop}")
        else:
            print(f"Không tìm thấy mã lớp {class_id} - {class_name}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

# all the function with a class ID (e.g., "2") and class name (e.g., "CTK44A")
get_student_in_class('1','CTK43')'''

#d Tìm kiếm thông tin sinh viên theo tên và mã lớp:
'''import pyodbc

connectionString = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-P7KU7A4I\\SQLEXPRESS;"
    "DATABASE=QLSinhVien;"
    "Trusted_Connection=yes"
)

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_student_info_in_class(student_name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
        select SinhVien.ID as "Mã số", HoTen, MaLop, TenLop
        from SinhVien, Lop
        where SinhVien.MaLop=Lop.ID 
        and SinhVien.HoTen LIKE ?   AND SinhVien.MaLop = ?
        """

        params = (f'%{student_name}', class_id)
        cursor.execute(select_query, params)
        records = cursor.fetchall()
        if records:
            print(f'Danh sách sinh viên có tên {student_name.split()[-1]} - mã lớp {class_id}:')
            print('Mã số    Họ tên             Mã lớp       Tên lớp')
            for row in records:
                ID = row[0]
                HoTen = row[1]
                MaLop = row[2]
                TenLop = row[3]
                # Định dạng thông tin để căn chỉnh
                print(f'{ID:<5}  {HoTen:<20}  {MaLop:<7}  {TenLop}')
        else:
            print(f'Không tìm thấy sinh viên {student_name} - {class_id}')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:', error)

get_student_info_in_class('yeah', '1')'''

#4. Insert/Update/Delete:
import pyodbc

connectionString = '''DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=.;DATABASE=QLSinhVien,Encrypt=no'''
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
# insert
def insert_class(class_name):
    try:
        connection = get_connection() 
        cursor = connection.cursor()
        # Cách 1 - truyền trực tiếp tham số vào câu truy vấn 
        # select_query = f"Insert into Lop(TenLop) values ('{class_name}')"
        # cursor.excute(select_query,)
        
        # Cách 2 - Dùng tham số
        select_query = "INSERT INTO Lop (TenLop) VALUES (?) "
        cursor.execute(select_query, (class_name,))
        
        connection.commit()
        print("Đã thêm lớp mới thành công")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

# Update
# Function to update both ID and class name and display the updated class
def update_class(old_class_id, new_class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Update the class name
        update_query = "UPDATE Lop SET TenLop = ? WHERE ID = ?"
        cursor.execute(update_query, (new_class_name, old_class_id))

        connection.commit()

        # Retrieve the updated class information
        select_query = "SELECT * FROM Lop WHERE ID = ?"
        cursor.execute(select_query, (old_class_id,))
        updated_class = cursor.fetchone()

        if updated_class:
            print(f"Đã cập nhật lớp có ID={old_class_id} và Tên lớp thành công")
            print("Thông tin lớp sau khi cập nhật:")
            print("ID lớp:", updated_class.ID)
            print("Tên lớp:", updated_class.TenLop)
        else:
            print(f"Không tìm thấy lớp có ID={old_class_id} sau khi cập nhật")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

# Call the function to update class name and display the updated class information

# Delete
def delete_class(class_id):
    try:
        connection = get_connection() 
        cursor = connection.cursor()
        delete_query = "DELETE FROM Lop WHERE ID = ?"
        cursor.execute(delete_query, (class_id,))
        connection.commit()
        print(f"Đã xóa lớp {class_id} thành công")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách các lớp là: ") 
        for row in records:
            print("*" * 108)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error: 
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

# Gọi hàm insert_class để chèn lớp mới
insert_class('CTK47')

# delete_class(9)

update_class(10,'CTK48')

# Gọi hàm get_all_class để xuất tất cả các lớp ra màn hình
get_all_class()

