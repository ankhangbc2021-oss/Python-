# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Các trường thông tin cần thu thập (5 trường):

# employee_name – Họ và tên nhân viên (str, không rỗng)

# employee_id – Mã nhân viên (str, không rỗng)

# department – Phòng ban (str, không rỗng)

# salary – Lương cơ bản (float, > 0)

# kpi_score – Điểm KPI (float, từ 1.0 đến 5.0)

# Bảng thiết kế dữ liệu:

# Tên biến	Câu hỏi input	Kiểu dữ liệu	Điều kiện validation
# employee_name	Nhập họ và tên nhân viên (Ví dụ: Nguyễn Văn A):	str	Không rỗng, không toàn khoảng trắng
# employee_id	Nhập mã nhân viên (Ví dụ: NV001):	str	Không rỗng, không toàn khoảng trắng
# department	Nhập phòng ban công tác (Ví dụ: IT, HR, Marketing):	str	Không rỗng
# salary	Nhập lương cơ bản (VNĐ, Ví dụ: 15000000):	float	> 0
# kpi_score	Nhập điểm KPI (Thang 1.0 → 5.0, Ví dụ: 4.5):	float	1.0 ≤ kpi_score ≤ 5.0


# Luồng chương trình (Pseudocode):

# Bắt đầu
#   In lời chào hệ thống
#   While True (vòng lặp tổng):
#     Nhập employee_name, employee_id, department
#     Nếu dữ liệu rỗng → báo lỗi, nhập lại
#     Nhập salary (while salary <= 0 → báo lỗi, nhập lại)
#     Nhập kpi_score (while kpi_score ngoài 1.0–5.0 → báo lỗi, nhập lại)
#     In Hồ sơ Nhân sự Điện tử
#     In Log hệ thống (tên biến + kiểu dữ liệu)
#     Hỏi: Tiếp tục nhập nhân viên khác? (y/n)
#     Nếu n → break
# Kết thúc
# (2) Triển khai code Python

print("=== KIOSK HR TỰ PHỤC VỤ - TECHCORP ===")

while True:
    # --- Khối Thu thập dữ liệu chuỗi ---
    employee_name = input("Nhập họ và tên nhân viên (Ví dụ: Nguyễn Văn A): ").strip()
    if not employee_name:
        print("[LỖI] Tên nhân viên không hợp lệ! Vui lòng nhập lại.\n")
        continue

    employee_id = input("Nhập mã nhân viên (Ví dụ: NV001): ").strip()
    if not employee_id:
        print("[LỖI] Mã nhân viên không hợp lệ! Vui lòng nhập lại.\n")
        continue

    department = input("Nhập phòng ban công tác (Ví dụ: IT, HR, Marketing): ").strip()
    if not department:
        print("[LỖI] Phòng ban không hợp lệ! Vui lòng nhập lại.\n")
        continue

    # --- Khối Thu thập dữ liệu số ---
    # Lương
    while True:
        try:
            salary = float(input("Nhập lương cơ bản (VNĐ, Ví dụ: 15000000): "))
            if salary <= 0:
                print("[LỖI] Lương phải lớn hơn 0! Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("[LỖI] Dữ liệu không hợp lệ! Vui lòng nhập số.")

    # Điểm KPI
    while True:
        try:
            kpi_score = float(input("Nhập điểm KPI (Thang 1.0 → 5.0, Ví dụ: 4.5): "))
            if kpi_score < 1.0 or kpi_score > 5.0:
                print("[LỖI] Điểm KPI phải nằm trong khoảng 1.0 → 5.0! Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("[LỖI] Dữ liệu không hợp lệ! Vui lòng nhập số.")

    # --- Khối Hiển thị Hồ sơ ---
    print("\n=== HỒ SƠ NHÂN SỰ ĐIỆN TỬ ===")
    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {employee_name}")
    print(f"Phòng ban    : {department}")
    print(f"Lương cơ bản : {salary:,.0f} VNĐ")
    print(f"Điểm KPI     : {kpi_score}")
    print("================================")

    # --- Khối Log hệ thống ---
    print("\n=== SYSTEM LOG ===")
    print("employee_name:", type(employee_name))
    print("employee_id:", type(employee_id))
    print("department:", type(department))
    print("salary:", type(salary))
    print("kpi_score:", type(kpi_score))
    print("=== END LOG ===\n")

    # --- Khối hỏi tiếp tục ---
    cont = input("Tiếp tục nhập nhân viên khác? (y/n): ").strip().lower()
    if cont != "y":
        print("\n>>> Hoàn tất quá trình nhập hồ sơ nhân sự! <<<")
        break
