# (1) Phân tích lỗi
# Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?  
# Vì chuỗi trong Python là immutable (bất biến). Khi gọi .strip(), Python trả về một chuỗi mới đã loại bỏ khoảng trắng, nhưng không thay đổi chuỗi gốc. Nếu không gán lại cho student_name, giá trị ban đầu vẫn giữ nguyên.

# Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?  
# Tương tự, .title() trả về chuỗi mới với chữ cái đầu mỗi từ viết hoa. Nhưng trong code hiện tại, kết quả không được gán lại cho biến student_name, nên giá trị vẫn là " nguYEn vAn a ".

# Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?  
# .upper() cũng trả về chuỗi mới, nhưng không gán lại cho student_code. Do đó, biến vẫn giữ nguyên " rk-001-python ".

# Vì sao email.lower() không làm email chuyển thành chữ thường?  
# .lower() trả về chuỗi mới viết thường, nhưng không gán lại cho email. Vì vậy, biến vẫn giữ nguyên " Student01@GMAIL.COM ".

# Muốn các phương thức xử lý chuỗi có hiệu lực, cần phải gán lại kết quả cho biến.  

# # Ví dụ:
# student_name = student_name.strip().title()

# (2) Sửa lỗi – Source Code Chuẩn Hóa

student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
