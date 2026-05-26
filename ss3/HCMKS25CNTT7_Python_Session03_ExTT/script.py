# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Các trường thông tin cần thu thập:

# employee_name – Tên nhân viên (str, không rỗng)

# working_days – Số ngày đi làm (int, ≥ 0)

# Bảng thiết kế dữ liệu:

# Tên biến	Câu hỏi input	Kiểu dữ liệu	Điều kiện validation
# employee_name	Nhập tên nhân viên (Ví dụ: Nguyễn Văn A):	str	Không rỗng, không toàn space
# working_days	Nhập số ngày đi làm (Ví dụ: 22):	int	≥ 0


# Luồng chương trình (Pseudocode):

# Bắt đầu
#   While True (vòng lặp tổng):
#     Nhập số lượng nhân viên
#     For i in range(1, số lượng):
#       Nhập tên nhân viên
#       Nếu tên rỗng → báo lỗi, nhập lại
#       Nhập số ngày đi làm
#       Nếu working_days < 0 → báo lỗi, nhập lại
#       In thông tin nhân viên
#       Đánh giá chuyên cần:
#         Nếu <20 → "Cần cải thiện chuyên cần"
#         Else → "Nhân viên chuyên cần tốt"
#     Hỏi tiếp tục chương trình? (y/n)
#     Nếu n → break
# Kết thúc
# (2) Triển khai code Python

print("=== HỆ THỐNG QUẢN LÝ NHÂN VIÊN ===")

while True:
    try:
        num_employees = int(input("Nhập số lượng nhân viên: "))
        if num_employees <= 0:
            print("[LỖI] Số lượng nhân viên phải lớn hơn 0!\n")
            continue
    except ValueError:
        print("[LỖI] Vui lòng nhập số nguyên hợp lệ!\n")
        continue

    for i in range(1, num_employees + 1):
        print(f"\n--- Nhân viên {i} ---")

        # Nhập tên nhân viên
        employee_name = input("Tên nhân viên: ").strip()
        if not employee_name:
            print("[LỖI] Tên nhân viên không hợp lệ! Bỏ qua nhân viên này.\n")
            continue

        # Nhập số ngày đi làm
        try:
            working_days = int(input("Số ngày đi làm: "))
            if working_days < 0:
                print("[LỖI] Số ngày đi làm không hợp lệ! Bỏ qua nhân viên này.\n")
                continue
        except ValueError:
            print("[LỖI] Vui lòng nhập số nguyên hợp lệ! Bỏ qua nhân viên này.\n")
            continue

        # Hiển thị thông tin nhân viên
        print("\nThông tin nhân viên:")
        print(f"Tên: {employee_name}")
        print(f"Số ngày đi làm: {working_days}")

        # Đánh giá chuyên cần
        if working_days < 20:
            print("Đánh giá: Cần cải thiện chuyên cần")
        else:
            print("Đánh giá: Nhân viên chuyên cần tốt")

    # Hỏi tiếp tục hay kết thúc
    cont = input("\nTiếp tục chương trình? (y/n): ").strip().lower()
    if cont != "y":
        print("Chương trình kết thúc")
        break
