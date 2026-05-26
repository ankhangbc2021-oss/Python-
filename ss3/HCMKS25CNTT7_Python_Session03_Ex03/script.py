# (1) Phân tích & Thiết kế giải pháp
# Input/Output:

# Input (dữ liệu đầu vào):
# employee_code (str) – Mã nhân viên
# employee_name (str) – Họ và tên nhân viên
# department (str) – Phòng ban công tác
# Output (dữ liệu đầu ra):
# Phiếu Hồ sơ Điện tử hiển thị rõ ràng thông tin nhân viên.
# Nếu dữ liệu không hợp lệ (mã hoặc tên rỗng/toàn khoảng trắng) → cảnh báo đỏ, không in phiếu.
# Giải pháp:
# Dùng vòng lặp for chạy đúng 3 lần để nhập thông tin cho 3 nhân viên.
# Sau mỗi lượt nhập:
# Kiểm tra hợp lệ bằng strip() để loại bỏ khoảng trắng.
# Nếu employee_code hoặc employee_name rỗng → in cảnh báo, bỏ qua in phiếu.
# Ngược lại → in Phiếu Hồ sơ Điện tử.
# Sau khi hoàn tất 3 lượt → in thông báo kết thúc.
# Pseudocode:


# Bắt đầu
#   For i in range(1,4):
#     Nhập employee_code, employee_name, department
#     Nếu employee_code rỗng hoặc employee_name rỗng:
#         In cảnh báo đỏ
#         Tiếp tục vòng lặp
#     Ngược lại:
#         In Phiếu Hồ sơ Điện tử
#   In thông báo hoàn thành
# Kết thúc
# (2) Triển khai code Python

print("=== HỆ THỐNG TẠO HỒ SƠ NHÂN VIÊN ===")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(f"\n--- Đang nhập dữ liệu cho nhân viên số {employee_number} ---")

    # Thu thập dữ liệu
    employee_code = input("Nhập mã nhân viên (Ví dụ: NV001, DEV099...): ").strip()
    employee_name = input("Nhập họ và tên nhân viên (Ví dụ: Nguyễn Văn A): ").strip()
    department = input("Nhập phòng ban công tác (Ví dụ: IT, Marketing, Kế toán...): ").strip()

    # Kiểm tra dữ liệu hợp lệ
    if not employee_code or not employee_name:
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue  # bỏ qua in phiếu, chuyển sang nhân viên tiếp theo

    # In Phiếu Hồ sơ Điện tử
    print("\n=== PHIẾU HỒ SƠ ĐIỆN TỬ ===")
    print(f"Mã nhân viên : {employee_code}")
    print(f"Họ và tên    : {employee_name}")
    print(f"Phòng ban    : {department}")
    print("============================")

print("\n>>> Hoàn tất quá trình nhập hồ sơ cho 3 nhân viên! <<<")
