# (1) Phân tích & Đề xuất giải pháp
# Input/Output:

# Input: HR nhập số lượng nhân sự mới trong tháng → kiểu int.

# Output:

# Nếu nhập số ≤ 0 → báo lỗi và yêu cầu nhập lại.

# Nếu nhập số > 0 → in thông báo thành công và kết thúc chương trình.

# Giải pháp tạo vòng lặp bắt nhập lại (validation loop):

# Giải pháp A – While True + break:

# while True:
#     number = int(input("Nhập số lượng: "))
#     if number > 0:
#         print("Thành công")
#         break
#     else:
#         print("Lỗi, nhập lại")
# Ngắn gọn, dễ viết.

# Dùng break để thoát khi hợp lệ.

# Giải pháp B – While với điều kiện:

# number = 0
# while number <= 0:
#     number = int(input("Nhập số lượng: "))
#     if number <= 0:
#         print("Lỗi, nhập lại")
# print("Thành công")
# Rõ ràng về mặt logic (vòng lặp chỉ chạy khi dữ liệu chưa hợp lệ).
# Nhưng hơi dài dòng, khó đọc hơn.

# Chốt lựa chọn:  
# → Giải pháp A (While True + break) được chọn vì ngắn gọn, dễ đọc, dễ bảo trì. Trong môi trường HR, sự đơn giản và trực quan là ưu tiên hàng đầu.

# (2) Triển khai code Python
print("=== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ===")

while True:
    try:
        # Nhập dữ liệu từ HR
        new_employees = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này (Ví dụ: 5): "))
    except ValueError:
        print("[LỖI] Dữ liệu không hợp lệ! Vui lòng nhập một số nguyên.")
        continue

    # Kiểm tra điều kiện hợp lệ
    if new_employees <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {new_employees} nhân sự mới!")
        print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
        break
