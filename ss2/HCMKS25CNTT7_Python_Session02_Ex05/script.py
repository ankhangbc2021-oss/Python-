# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Bảng thiết kế dữ liệu (5 trường thông tin):

# Tên biến	Câu hỏi input	Kiểu dữ liệu
# patient_name	Nhập họ và tên bệnh nhân (Ví dụ: Nguyễn Văn A):	str
# patient_age	Nhập tuổi bệnh nhân (Ví dụ: 30):	int
# spo2_level	Nhập nồng độ oxy trong máu SpO2 (%) (Ví dụ: 95):	int
# heart_rate	Nhập nhịp tim (nhịp/phút, Ví dụ: 85):	int
# has_insurance	Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'):	str

# Luồng chương trình (Pseudocode):

# Bắt đầu
#   Thu thập dữ liệu bệnh nhân (5 trường)
#   Kiểm tra dữ liệu âm hoặc nhập sai định dạng → báo lỗi và kết thúc
#   Phân luồng y khoa:
#     Nếu spo2_level < 90 hoặc heart_rate > 120 → RED
#     Elif spo2_level từ 90–95 hoặc heart_rate từ 100–120 → YELLOW
#     Else → GREEN
#   Tính viện phí:
#     Nếu age < 6 hoặc age >= 80 → phí = 0
#     Elif has_insurance == "yes" → phí = 250000
#     Else → phí = 500000
#   In Phiếu Khám Bệnh Điện Tử (thông tin, phân luồng, viện phí)
#   In Log hệ thống (tên biến + kiểu dữ liệu)
# Kết thúc
# (2) Triển khai code Python

# --- Khối Khởi tạo ---
print("=== HỆ THỐNG KIOSK TIẾP NHẬN BỆNH NHÂN ===")

# --- Khối Thu thập dữ liệu ---
patient_name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyễn Văn A): ").strip()

try:
    patient_age = int(input("Nhập tuổi bệnh nhân (Ví dụ: 30): "))
    spo2_level = int(input("Nhập nồng độ oxy trong máu SpO2 (%) (Ví dụ: 95): "))
    heart_rate = int(input("Nhập nhịp tim (nhịp/phút, Ví dụ: 85): "))
except ValueError:
    print("LỖI: Dữ liệu nhập vào phải là số nguyên hợp lệ!")
    exit()

has_insurance = input("Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

# --- Khối Kiểm tra lỗi ---
if not patient_name or patient_age < 0 or spo2_level < 0 or heart_rate < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ (không được âm hoặc bỏ trống)!")
    exit()

if has_insurance not in ["yes", "no"]:
    print("LỖI: Câu trả lời BHYT không hợp lệ (chỉ được nhập 'yes' hoặc 'no')!")
    exit()

# --- Khối Phân luồng y khoa ---
if spo2_level < 90 or heart_rate > 120:
    triage_result = "BÁO ĐỘNG ĐỎ (Cấp cứu khẩn)"
elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage_result = "BÁO ĐỘNG VÀNG (Theo dõi sát)"
else:
    triage_result = "XANH (Khám thường)"

# --- Khối Tính viện phí ---
base_fee = 500000
if patient_age < 6 or patient_age >= 80:
    fee = 0
elif has_insurance == "yes":
    fee = base_fee * 0.5
else:
    fee = base_fee

# --- Khối Hiển thị Phiếu Khám ---
print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")
print(f"Tên bệnh nhân : {patient_name}")
print(f"Tuổi          : {patient_age}")
print(f"SpO2          : {spo2_level}%")
print(f"Nhịp tim      : {heart_rate} nhịp/phút")
print(f"Phân luồng    : {triage_result}")
print(f"Viện phí      : {fee:.0f} VNĐ")

# --- Khối Log hệ thống ---
print("\n=== SYSTEM LOG ===")
print("patient_name:", type(patient_name))
print("patient_age:", type(patient_age))
print("spo2_level:", type(spo2_level))
print("heart_rate:", type(heart_rate))
print("has_insurance:", type(has_insurance))
print("=== END LOG ===")
