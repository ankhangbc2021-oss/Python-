# (1) Thiết kế kiến trúc & Luồng dữ liệu
# Các trường thông tin cần thu thập:
# patient_name – Họ và tên bệnh nhân – str
# gender – Giới tính – str
# year_of_birth – Năm sinh – int
# phone_number – Số điện thoại – str
# email – Địa chỉ email – str
# symptoms – Triệu chứng ban đầu – str
# medical_cost – Chi phí khám – float
# Bảng thiết kế dữ liệu:

# Tên biến	Nội dung input	Kiểu dữ liệu mong muốn
# patient_name	Họ và tên bệnh nhân	str
# gender	Giới tính	str
# year_of_birth	Năm sinh (ví dụ: 1998)	int
# phone_number	Số điện thoại (ví dụ: 0394556888)	str
# email	Email (ví dụ: abc@gmail.com)	str
# symptoms	Triệu chứng ban đầu	str
# medical_cost	Chi phí khám (ví dụ: 250000)	float

# Luồng chương trình (pseudocode):


# Bắt đầu
#   In lời chào hệ thống
#   Thu thập dữ liệu cá nhân (tên, giới tính, năm sinh, điện thoại, email)
#   Thu thập dữ liệu sinh hiệu (triệu chứng, chi phí khám)
#   Ép kiểu dữ liệu: năm sinh -> int, chi phí -> float
#   Sinh mã bệnh nhân: "BN" + year_of_birth + 3 số ngẫu nhiên
#   In thẻ bệnh nhân (thông tin + kiểu dữ liệu)
# Kết thúc
# Thiết kế câu hỏi input() thân thiện:

# Ví dụ:
# input("Nhập năm sinh (YYYY, ví dụ: 1998): ")
# input("Nhập chi phí khám (VND, ví dụ: 250000): ")
# (2) Triển khai code Python

import random

# --- Khối Khởi tạo ---
print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")

# --- Khối Thu thập dữ liệu ---
patient_name = input("Nhập tên bệnh nhân (Ví dụ: Nguyễn Văn A): ")
gender = input("Nhập giới tính (Ví dụ: Nam/Nữ): ")
year_of_birth_str = input("Nhập năm sinh (YYYY, ví dụ: 1998): ")
phone_number = input("Nhập số điện thoại (Ví dụ: 0394556888): ")
email = input("Nhập email (Ví dụ: abc@gmail.com): ")
symptoms = input("Nhập triệu chứng ban đầu (Ví dụ: Đau đầu, ho, sốt...): ")
medical_cost_str = input("Nhập chi phí khám (VND, ví dụ: 250000): ")

# --- Khối Xử lý ép kiểu ---
year_of_birth = int(year_of_birth_str)
medical_cost = float(medical_cost_str)

# Sinh mã bệnh nhân tự động
random_suffix = random.randint(100, 999)
patient_code = f"BN{year_of_birth}{random_suffix}"

# --- Khối Hiển thị ---
print("\n=== THẺ BỆNH NHÂN ===")
print(f"Mã BN        : {patient_code}")
print(f"Tên          : {patient_name} ({type(patient_name).__name__})")
print(f"Giới tính    : {gender} ({type(gender).__name__})")
print(f"Năm sinh     : {year_of_birth} ({type(year_of_birth).__name__})")
print(f"Điện thoại   : {phone_number} ({type(phone_number).__name__})")
print(f"Email        : {email} ({type(email).__name__})")
print(f"Triệu chứng  : {symptoms} ({type(symptoms).__name__})")
print(f"Chi phí      : {medical_cost} VND ({type(medical_cost).__name__})")

# --- Log hệ thống ---
print("\n=== SYSTEM LOG ===")
print("patient_name:", type(patient_name))
print("gender:", type(gender))
print("year_of_birth:", type(year_of_birth))
print("phone_number:", type(phone_number))
print("email:", type(email))
print("symptoms:", type(symptoms))
print("medical_cost:", type(medical_cost))
print("=== END LOG ===")
