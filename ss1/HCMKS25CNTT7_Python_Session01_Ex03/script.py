# 1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output:
# Input (dữ liệu đầu vào):
# Họ và tên bệnh nhân → kiểu str
# Mã bệnh án (ví dụ: BN1024, BA9901) → kiểu str
# Khoa/Phòng khám chỉ định (ví dụ: Khoa Nội, Phòng Khám Mắt) → kiểu str
# Output (dữ liệu đầu ra):
# Phiếu khám bệnh điện tử hiển thị theo định dạng chuẩn:
# Mã
# --- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---
# Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]
# => Thông tin đã được tiếp nhận thành công!
# Đề xuất giải pháp:
# Sử dụng hàm input() để lấy dữ liệu từ người dùng.
# Lưu trữ dữ liệu vào các biến tương ứng.
# Dùng print() để hiển thị phiếu khám bệnh theo định dạng chuẩn.
# Có thể bổ sung kiểm tra dữ liệu (ví dụ: mã bệnh án phải bắt đầu bằng BN/BA và theo sau là số).
# Thiết kế thuật toán (Pseudocode):
# Mã
# Bắt đầu
#   In tiêu đề hệ thống
#   Nhập họ tên bệnh nhân -> name_patient
#   Nhập mã bệnh án -> medical_code
#   Nhập khoa/phòng khám -> department
#   In phiếu khám bệnh điện tử:
#     "Bệnh nhân: [name_patient] - Mã BA: [medical_code] - Chuyển tới: [department]"
#     "=> Thông tin đã được tiếp nhận thành công!"
# Kết thúc
# (2) Triển khai code Python

print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")

# Nhập dữ liệu từ nhân viên lễ tân
name_patient = input("Nhập họ và tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án (ví dụ: BN1024, BA9901): ")
department = input("Nhập khoa/phòng khám chỉ định: ")

# Hiển thị phiếu khám bệnh điện tử
print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Bệnh nhân: {name_patient} - Mã BA: {medical_code} - Chuyển tới: {department}")
print("=> Thông tin đã được tiếp nhận thành công!")
