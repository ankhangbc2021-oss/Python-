# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Bảng thiết kế dữ liệu (5 trường thông tin):

# Tên biến	Câu hỏi input	Kiểu dữ liệu
# patient_name	Nhập tên bệnh nhân (Ví dụ: Nguyễn Văn A):	str
# birth_year	Nhập năm sinh (Ví dụ: 1999):	int
# sick_days	Nhập số ngày bị bệnh (Ví dụ: 2):	int
# body_temperature	Nhập nhiệt độ cơ thể (°C, Ví dụ: 39):	float
# medical_cost	Nhập chi phí khám (VNĐ, Ví dụ: 300000):	float


# Luồng chương trình (Pseudocode):

# Bắt đầu
#   Nhập dữ liệu bệnh nhân
#   Kiểm tra dữ liệu hợp lệ:
#     - Tên không rỗng
#     - Năm sinh trong khoảng 1900 → năm hiện tại
#     - Số ngày bệnh ≥ 0
#     - Nhiệt độ trong khoảng 30 → 45
#     - Chi phí > 0
#   Nếu dữ liệu không hợp lệ → báo lỗi và kết thúc
#   Tính toán:
#     - Tuổi = năm hiện tại - birth_year
#     - Phụ phí = 10% chi phí
#     - Tổng chi phí = chi phí + phụ phí
#   Phân loại tình trạng sức khỏe:
#     - Nếu nhiệt độ > 38 và sick_days > 3 → "Nguy hiểm"
#     - Elif nhiệt độ > 38 → "Sốt cao"
#     - Elif nhiệt độ > 37.5 → "Sốt nhẹ"
#     - Else → "Bình thường"
#   Đánh giá mức độ ưu tiên (nested if):
#     - Nếu tình trạng = "Nguy hiểm":
#         - Nếu tuổi > 60 → "Cấp cứu"
#         - Else → "Ưu tiên cao"
#     - Else → "Bình thường"
#   Đánh giá mức chi phí (toán tử 3 ngôi):
#     - Nếu tổng chi phí > 500000 → "Cao"
#     - Else → "Thấp"
#   In phiếu kết quả
# Kết thúc
# (2) Triển khai code Python

import datetime

# --- Khối Khởi tạo ---
print("=== MEDICAL TRIAGE SYSTEM ===")
current_year = datetime.datetime.now().year

# --- Khối Thu thập dữ liệu ---
patient_name = input("Nhập tên bệnh nhân (Ví dụ: Nguyễn Văn A): ").strip()

try:
    birth_year = int(input(f"Nhập năm sinh (1900 → {current_year}, Ví dụ: 1999): "))
    sick_days = int(input("Nhập số ngày bị bệnh (Ví dụ: 2): "))
    body_temperature = float(input("Nhập nhiệt độ cơ thể (°C, Ví dụ: 39): "))
    medical_cost = float(input("Nhập chi phí khám (VNĐ, Ví dụ: 300000): "))
except ValueError:
    print("LỖI: Dữ liệu nhập vào phải là số hợp lệ!")
    exit()

# --- Khối Kiểm tra dữ liệu hợp lệ ---
if (not patient_name or 
    birth_year < 1900 or birth_year > current_year or 
    sick_days < 0 or 
    body_temperature < 30 or body_temperature > 45 or 
    medical_cost <= 0):
    print("LỖI: Dữ liệu nhập vào không hợp lệ!")
    exit()

# --- Khối Tính toán ---
age = current_year - birth_year
extra_fee = medical_cost * 0.1
total_cost = medical_cost + extra_fee

# --- Khối Phân loại tình trạng sức khỏe ---
if body_temperature > 38 and sick_days > 3:
    health_status = "Nguy hiểm"
elif body_temperature > 38:
    health_status = "Sốt cao"
elif body_temperature > 37.5:
    health_status = "Sốt nhẹ"
else:
    health_status = "Bình thường"

# --- Khối Đánh giá mức độ ưu tiên (nested if) ---
if health_status == "Nguy hiểm":
    if age > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
else:
    priority = "Bình thường"

# --- Khối Đánh giá mức chi phí (toán tử 3 ngôi) ---
cost_level = "Cao" if total_cost > 500000 else "Thấp"

# --- Khối Hiển thị kết quả ---
print("\n=== KẾT QUẢ KHÁM BỆNH ===")
print(f"Tên bệnh nhân : {patient_name}")
print(f"Tuổi          : {age}")
print(f"Nhiệt độ      : {body_temperature} °C")
print(f"Số ngày bệnh  : {sick_days}")
print(f"Tình trạng    : {health_status}")
print(f"Mức độ ưu tiên: {priority}")
print(f"Tổng chi phí  : {total_cost:.1f} VNĐ")
print(f"Mức chi phí   : {cost_level}")
