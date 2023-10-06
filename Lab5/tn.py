#d Tìm kiếm thông tin sinh viên theo tên và mã lớp:
#c1
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
                print(f'{ID:<8}  {HoTen:<20}  {MaLop:<7}  {TenLop}')
        else:
            print(f'Không tìm thấy sinh viên {student_name} - {class_id}')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:', error)

get_student_info_in_class('Trung', '3')'''


#c2
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
        and RIGHT(SinhVien.HoTen, CHARINDEX(' ', REVERSE(SinhVien.HoTen)) - 1) = ?  AND SinhVien.MaLop = ?
        """

        params = (student_name, class_id)
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
                print(f'{ID:<8}  {HoTen:<20}  {MaLop:<7}  {TenLop}')
        else:
            print(f'Không tìm thấy sinh viên {student_name} - {class_id}')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:', error)

get_student_info_in_class('Trung', '3')'''

# Insert sv
import pyodbc

# Chuỗi kết nối đến cơ sở dữ liệu
connectionString = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-P7KU7A4I\\SQLEXPRESS;"
    "DATABASE=QLSinhVien;"
    "Trusted_Connection=yes"
)

def student_exists(student_id):
    try:
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()

        # Truy vấn kiểm tra xem sinh viên có tồn tại không
        select_query = "SELECT COUNT(*) FROM SinhVien WHERE ID = ?"
        cursor.execute(select_query, (student_id,))
        count = cursor.fetchone()[0]

        connection.close()

        return count > 0
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
        return False

def insert_student(student_id, student_name, class_id):
    try:
        if student_exists(student_id):
            print("Sinh viên đã tồn tại")
            return

        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        
        # Gọi thủ tục lưu trữ InsertStudent và truyền giá trị cho các tham số
        cursor.execute("EXEC InsertStudent @Id = ?, @HoTen = ?, @MaLop = ?", (student_id, student_name, class_id))
        
        connection.commit()
        print("Đã chèn sinh viên thành công")
        
        connection.close()
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)

def display_students():
    try:
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()

        # Truy vấn danh sách sinh viên
        select_query = "SELECT * FROM SinhVien"
        cursor.execute(select_query)
        records = cursor.fetchall()

        # Xuất danh sách sinh viên ra màn hình
        print("*" * 108)
        print("{:<15} {:<45} {:<15}".format("Mã sinh viên", "Họ và tên", "Mã lớp"))
        print("*" * 108)
        for row in records:
            print("{:<15} {:<45} {:<15}".format(row[0], row[1], row[2]))

        connection.close()
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)


# Gọi hàm insert_student để chèn sinh viên mới
insert_student(17, 'Nguyễn Văn A', 1)

# Gọi hàm display_students để xuất danh sách sinh viên ra màn hình
display_students()



