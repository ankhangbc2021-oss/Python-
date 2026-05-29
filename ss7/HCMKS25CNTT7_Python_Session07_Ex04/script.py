# (1) Phân tích và thiết kế giải pháp
# Input/Output:

# Input:

# Số lượng phiếu đăng ký (kiểu int).

# Với mỗi phiếu: một chuỗi chứa 4 phần dữ liệu, phân tách bằng dấu |.
# Ví dụ: "nguyEN vAn a | python basic | rk-001 | student01@GMAIL.COM".

# Output:

# Nếu hợp lệ: In thông tin đã chuẩn hóa theo định dạng yêu cầu.

# Nếu không hợp lệ: In thông báo lỗi tương ứng và bỏ qua phiếu.

# Giải pháp:

# Dùng .strip() để loại bỏ khoảng trắng thừa.
# Dùng .split("|") để tách dữ liệu.
# Kiểm tra số lượng phần tử sau khi tách.
# Chuẩn hóa từng phần:
# Họ tên: .title().
# Khóa học: .title().
# Mã học viên: .upper().
# Email: .lower().
# Kiểm tra tính hợp lệ:
# Email phải chứa @.
# Mã học viên phải có độ dài ≥ 5 ký tự.
# Tạo mã xác nhận: "{student_code}_{course_name.replace(' ', '-')}".

# Thuật toán (Pseudocode):

# nhập n
# nếu n <= 0:
#     in "Số lượng phiếu đăng ký không hợp lệ"
#     kết thúc

# lặp i từ 1 đến n:
#     nhập transaction
#     transaction = transaction.strip()
#     parts = transaction.split("|")

#     nếu len(parts) != 4:
#         in "Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này"
#         tiếp tục

#     student_name = parts[0].strip().title()
#     course_name = parts[1].strip().title()
#     student_code = parts[2].strip().upper()
#     email = parts[3].strip().lower()

#     nếu "@" không có trong email:
#         in "Email không hợp lệ. Bỏ qua phiếu này"
#         tiếp tục

#     nếu len(student_code) < 5:
#         in "Mã học viên không hợp lệ. Bỏ qua phiếu này"
#         tiếp tục
#     confirm_code = student_code + "_" + course_name.replace(" ", "-").upper()
#     in thông tin chuẩn hóa
# (2) Triển khai Code Python

# Chương trình chuẩn hóa phiếu đăng ký học viên tại Rikkei Education

# Nhập số lượng phiếu đăng ký
num_forms = int(input("Nhập số lượng phiếu đăng ký: "))

# Kiểm tra số lượng hợp lệ
if num_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    for i in range(num_forms):
        transaction = input(f"Nhập phiếu đăng ký {i+1}: ").strip()
        parts = transaction.split("|")

        # Kiểm tra đủ 4 phần dữ liệu
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        # Chuẩn hóa dữ liệu
        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        # Kiểm tra email hợp lệ
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Kiểm tra mã học viên hợp lệ
        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Tạo mã xác nhận
        confirm_code = f"{student_code}_{course_name.replace(' ', '-').upper()}"

        # In kết quả
        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirm_code)
