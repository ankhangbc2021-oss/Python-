# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Các trường thông tin cần thu thập (tối thiểu 5):
# patient_name – Họ và tên bệnh nhân – kiểu str
# patiet_code – Mã bệnh nhân (ví dụ: BN999) – kiểu str
# body_temperature – Nhiệt độ cơ thể – kiểu float
# heart_rate – Nhịp tim – kiểu int
# weight – Cân nặng – kiểu float
# Bảng thiết kế dữ liệu:

# Tên biến	Nội dung input	Kiểu dữ liệu mong muốn
# patient_name	Họ và tên bệnh nhân	str
# patient_code	Mã bệnh nhân (BNxxx)	str
# body_temperature	Nhiệt độ cơ thể (ví dụ: 37.5 °C)	float
# heart_rate	Nhịp tim (ví dụ: 85 nhịp/phút)	int
# weight	Cân nặng (ví dụ: 65.5 kg)	float
# Luồng chương trình (pseudocode):

# Bắt đầu
#   In lời chào hệ thống
#   Thu thập dữ liệu cá nhân (họ tên, mã bệnh nhân)
#   Thu thập dữ liệu sinh hiệu (nhiệt độ, nhịp tim, cân nặng)
#   Ép kiểu dữ liệu: nhiệt độ -> float, nhịp tim -> int, cân nặng -> float
#   In Phiếu Khám Bệnh Điện Tử (thông tin rõ ràng, dễ đọc)
#   In Log hệ thống (tên biến + kiểu dữ liệu)
# Kết thúc
# Thiết kế câu hỏi input() thân thiện:

# Ví dụ:

# python
# input("Nhập nhiệt độ cơ thể (°C, ví dụ: 37.5): ")
# input("Nhập nhịp tim (nhịp/phút, ví dụ: 85): ")
# input("Nhập cân nặng (kg, ví dụ:

# (2) Triển khai code Python

# --- Khối Khởi tạo ---
print("=== HỆ THỐNG KIOSK TIẾP NHẬN BỆNH NHÂN ===")

# --- Khối Thu thập dữ liệu ---
patient_name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyễn Văn A): ")
patient_code = input("Nhập mã bệnh nhân (Ví dụ: BN999): ")

temp_str = input("Nhập nhiệt độ cơ thể (°C, ví dụ: 37.5): ")
heart_str = input("Nhập nhịp tim (nhịp/phút, ví dụ: 85): ")
weight_str = input("Nhập cân nặng (kg, ví dụ: 65.5): ")

# --- Khối Xử lý ép kiểu ---
body_temperature = float(temp_str)
heart_rate = int(heart_str)
weight = float(weight_str)

# --- Khối Hiển thị ---
print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")
print(f"Bệnh nhân: {patient_name} - Mã BN: {patient_code}")
print(f"Nhiệt độ cơ thể: {body_temperature} °C")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f"Cân nặng: {weight} kg")
print("=> Thông tin đã được tiếp nhận thành công!\n")

# --- Log hệ thống (dành cho IT) ---
print("=== SYSTEM LOG ===")
print("patient_name:", type(patient_name))
print("patient_code:", type(patient_code))
print("body_temperature:", type(body_temperature))
print("heart_rate:", type(heart_rate))
print("weight:", type(weight))
print("=== END LOG ===")
