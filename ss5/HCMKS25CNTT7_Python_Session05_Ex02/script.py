# 1) Phân tích lỗi
# Trong mã nguồn hiện tại, biến total_students được khai báo bên ngoài vòng lặp chi nhánh.
# Điều này dẫn đến:
# Chi nhánh 1:
# Ban đầu total_students = 0.
# Cộng lần lượt 30 + 25 + 28 = 83.
# In ra đúng: 83 học viên.
# Chi nhánh 2:
# total_students không được reset về 0, vẫn giữ giá trị 83 từ chi nhánh 1.
# Cộng thêm 20 + 22 + 18 = 60.
# Kết quả: 83 + 60 = 143 học viên → sai.
# Chi nhánh 3:
# total_students vẫn giữ giá trị 143 từ chi nhánh 2.
# Cộng thêm 35 + 32 + 30 = 97.
# Kết quả: 143 + 97 = 240 học viên → sai.
# Nguyên nhân: biến tổng không được reset về 0 khi chuyển sang chi nhánh mới.

# (2) Sửa lỗi – Source Code chuẩn

# Thống kê số lượng học viên theo chi nhánh - Rikkei Education

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    branch_total = 0  # reset tổng học viên cho chi nhánh này

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        branch_total += student_count

    print(f"Chi nhánh {branch}: {branch_total} học viên")
