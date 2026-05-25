# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output:
# Input:
# patient_name → chuỗi (str)
# patient_age → số nguyên (int)

# Output:
# Phiếu khám bệnh điện tử gồm: Tên, Tuổi, Kết quả phân luồng.
# Nếu dữ liệu không hợp lệ → In cảnh báo lỗi, không in phiếu.
# Edge Cases cần xử lý:
# Bẫy 1: Tên bỏ trống hoặc chỉ toàn khoảng trắng.
# Bẫy 2: Tuổi âm hoặc tuổi quá lớn (>150).
# Giải pháp:
# Dùng strip() để loại bỏ khoảng trắng, kiểm tra tên rỗng.
# Dùng if-elif-else để phân luồng theo tuổi.
# Trước khi phân luồng, kiểm tra điều kiện lỗi:
# Nếu tên không hợp lệ hoặc tuổi ngoài phạm vi 0–150 → In cảnh báo lỗi và kết thúc.

# Pseudocode:

# Bắt đầu
#   Nhập tên bệnh nhân
#   Nhập tuổi bệnh nhân
#   Nếu tên rỗng hoặc tuổi <0 hoặc tuổi >150:
#       In cảnh báo lỗi
#       Kết thúc
#   Ngược lại:
#       Nếu tuổi <6:
#           Kết quả = "ƯU TIÊN: Bệnh nhi..."
#       Elif tuổi >=80:
#           Kết quả = "ƯU TIÊN: Người cao tuổi..."
#       Else:
#           Kết quả = "KHÁM THƯỜNG..."
#       In phiếu khám bệnh điện tử (Tên, Tuổi, Kết quả)
# Kết thúc
# (2) Triển khai code Python

# --- Khối Khởi tạo ---
print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")

# --- Khối Thu thập dữ liệu ---
patient_name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyễn Văn A): ").strip()
try:
    patient_age = int(input("Nhập tuổi bệnh nhân (Ví dụ: 25): "))
except ValueError:
    print("LỖI: Tuổi phải là số nguyên hợp lệ!")
    exit()

# --- Khối Kiểm tra lỗi (Edge Cases) ---
if not patient_name or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    exit()

# --- Khối Phân luồng ---
if patient_age < 6:
    result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif patient_age >= 80:
    result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

# --- Khối Hiển thị Phiếu Khám ---
print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")
print(f"Tên bệnh nhân : {patient_name}")
print(f"Tuổi          : {patient_age}")
print(f"Kết quả       : {result}")
