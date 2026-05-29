# (1) Phân tích lỗi
# Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?  
# Vì chuỗi trong Python là immutable (bất biến). Các phương thức như .strip() trả về một chuỗi mới, không thay đổi chuỗi gốc. Nếu không gán lại, biến transaction vẫn giữ nguyên giá trị ban đầu.

# Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?  
# Dữ liệu được phân tách bằng dấu | chứ không phải dấu -.

# Vì sao transaction.split("-") là sai?  
# Vì delimiter không đúng. Khi dùng "-", chương trình sẽ tách sai vị trí, dẫn đến dữ liệu bị lệch.

# Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?  
# Ví dụ: "nguyEN vAn a | PYTHON-01 | 15000000 | paid" khi split bằng "-" sẽ tạo ra các phần tử như "nguyEN vAn a | PYTHON", "01 | 15000000 | paid". Lúc này parts[0], parts[1] không còn khớp với ý nghĩa ban đầu (tên học viên, mã khóa học, số tiền, trạng thái).

# Vì sao cần .strip() lại từng phần sau khi split()?  
# Vì mỗi phần tử sau khi tách vẫn có thể chứa khoảng trắng thừa ở đầu/cuối. Nếu không .strip(), dữ liệu hiển thị sẽ không chuẩn.

# Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?  
# .format() hoặc f-string với dấu phẩy phân cách hàng nghìn chỉ hoạt động với kiểu số (int hoặc float). Nếu giữ nguyên dạng chuỗi, không thể định dạng đúng.

# (2) Sửa lỗi – Source Code Đúng Chuẩn


transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()


amount_formatted = f"{amount:,}"

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount_formatted, "VND")
print("Trạng thái:", status)
