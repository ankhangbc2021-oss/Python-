# (1) Phân tích & Đề xuất giải pháp
# Input/Output:
# Input (dữ liệu đầu vào):
# age (int) – tuổi bệnh nhân
# systolic_bp (int) – huyết áp tâm thu (mmHg)
# blood_sugar (int) – đường huyết (mg/dL)
# Output (dữ liệu đầu ra):
# Nếu dữ liệu âm hoặc không hợp lệ → "Dữ liệu nhập vào không hợp lệ"
# Nếu hợp lệ:
# Nếu thỏa mãn tất cả điều kiện (age < 75, 90 ≤ systolic_bp ≤ 140, blood_sugar < 150) → "ĐỦ ĐIỀU KIỆN PHẪU THUẬT"
# Ngược lại → "TỪ CHỐI PHẪU THUẬT"
# Giải pháp 1 – Flat Logic (gộp điều kiện):

# if age < 75 and 90 <= systolic_bp <= 140 and blood_sugar < 150:
#     print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
# else:
#     print("TỪ CHỐI PHẪU THUẬT")
# Ngắn gọn, dễ viết.
# Nhưng khi từ chối, không chỉ rõ lý do từng tiêu chí.
# Giải pháp 2 – Nested If (điều kiện lồng nhau):
# if age < 75:
#     if 90 <= systolic_bp <= 140:
#         if blood_sugar < 150:
#             print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
#         else:
#             print("TỪ CHỐI PHẪU THUẬT - Đường huyết quá cao")
#     else:
#         print("TỪ CHỐI PHẪU THUẬT - Huyết áp ngoài giới hạn an toàn")
# else:
#     print("TỪ CHỐI PHẪU THUẬT - Tuổi quá cao")
# Dài hơn, nhiều thụt lề.
# Nhưng thông báo chi tiết, giúp bác sĩ/điều dưỡng biết rõ lý do từ chối.

# Bảng so sánh:

# Tiêu chí	Flat Logic	Nested If
# Độ ngắn gọn code	Ngắn gọn	Dài hơn
# Độ phức tạp khi đọc (thụt lề)	Ít	Nhiều
# Trải nghiệm người dùng & y khoa	Thông báo chung chung	Thông báo chi tiết, hữu ích


# Chốt lựa chọn:  
# → Nested If phù hợp hơn trong môi trường y khoa, vì thông báo chi tiết giúp nhân viên y tế hiểu rõ nguyên nhân từ chối. Trade-off: code dài hơn nhưng giá trị y khoa cao hơn.

# (2) Triển khai code Python

print("=== SURGERY ELIGIBILITY SYSTEM ===")

try:
    age = int(input("Nhập tuổi bệnh nhân (ví dụ: 45): "))
    systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg, ví dụ: 120): "))
    blood_sugar = int(input("Nhập đường huyết (mg/dL, ví dụ: 110): "))
except ValueError:
    print("LỖI: Dữ liệu nhập vào phải là số nguyên!")
    exit()

# Edge Case: dữ liệu âm
if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ (không được âm)!")
    exit()

# Kiểm tra điều kiện Nested If
if age < 75:
    if 90 <= systolic_bp <= 140:
        if blood_sugar < 150:
            print("KẾT QUẢ: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("KẾT QUẢ: TỪ CHỐI PHẪU THUẬT - Đường huyết quá cao (≥150 mg/dL)")
    else:
        print("KẾT QUẢ: TỪ CHỐI PHẪU THUẬT - Huyết áp ngoài giới hạn an toàn (90–140 mmHg)")
else:
    print("KẾT QUẢ: TỪ CHỐI PHẪU THUẬT - Tuổi quá cao (≥75)")
