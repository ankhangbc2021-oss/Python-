# (1) Phân tích & Thiết kế Giải Pháp
# Input
# Số lượng chi nhánh: số nguyên (int).

# Số học viên đi học của từng lớp: số nguyên (int).

# Output
# Trạng thái lớp học sau khi nhập:

# Nếu số học viên > 0 → đánh giá trạng thái:

# Ví dụ: ≥ 20 → “Lớp học ổn định”

# < 20 → “Lớp cần được nhắc nhở theo dõi”

# Nếu số học viên = 0 → “Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.”

# Nếu số học viên < 0 → “Số học viên không hợp lệ. Vui lòng nhập lại.”

# Edge Cases
# Số học viên âm → báo lỗi, yêu cầu nhập lại cho đến khi hợp lệ.

# Số học viên bằng 0 → báo “Lớp vắng toàn bộ”, bỏ qua đánh giá.

# Giải pháp
# Dùng vòng lặp for để duyệt qua từng chi nhánh.

# Mỗi chi nhánh có 2 lớp → vòng lặp lồng nhau.

# Với mỗi lớp:

# Kiểm tra dữ liệu nhập.

# Nếu âm → yêu cầu nhập lại (dùng while).

# Nếu bằng 0 → in thông báo, bỏ qua đánh giá.

# Nếu > 0 → đánh giá trạng thái lớp học.

# Pseudocode

# nhập số lượng chi nhánh
# for mỗi chi nhánh:
#     for mỗi lớp (2 lớp):
#         nhập số học viên
#         while số học viên < 0:
#             in "Số học viên không hợp lệ. Vui lòng nhập lại."
#             nhập lại số học viên
#         nếu số học viên == 0:
#             in "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
#         ngược lại:
#             nếu số học viên >= 20:
#                 in "Lớp học ổn định"
#             ngược lại:
#                 in "Lớp cần được nhắc nhở theo dõi"
# (2) Triển khai Code Python

# Điểm danh học viên theo chi nhánh - Rikkei Education

# Nhập số lượng chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")
    for classroom in range(1, 3):  # mỗi chi nhánh có 2 lớp
        # Nhập số học viên, kiểm tra dữ liệu hợp lệ
        student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))
        while student_count < 0:
            print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))

        # Edge case: lớp vắng toàn bộ
        if student_count == 0:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue

        # Đánh giá trạng thái lớp học
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")
