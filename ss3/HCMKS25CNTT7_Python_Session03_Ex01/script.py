# (1) Phân tích lỗi
# Dò luồng thực thi (trace code):

# Chương trình khởi tạo vòng lặp for employee_number in range(1, 4): → chạy 3 lần cho 3 nhân viên.
# Bên trong vòng lặp, thực tập sinh lại viết:

# total_budget = 0
# → tức là mỗi lần lặp lại khởi tạo lại biến tổng quỹ lương về 0.

# Sau đó nhập lương và cộng vào total_budget.
# Kết thúc vòng lặp, giá trị total_budget chỉ giữ lại lần cộng cuối cùng (vì các lần trước đã bị reset về 0).

# Nguyên nhân:
# Đây là lỗi logic kinh điển: khởi tạo biến cộng dồn bên trong vòng lặp.
# Biến cộng dồn (total_budget) phải được khởi tạo trước vòng lặp, để mỗi lần lặp chỉ cộng thêm vào giá trị hiện có, thay vì reset.
# (2) Sửa lỗi

print("=== PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ===")

# Khởi tạo biến cộng dồn tổng quỹ lương (đặt ngoài vòng lặp)
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    
    # Nhập mức lương
    salary = int(input(" Nhập mức lương (VND): "))
    
    # Cộng dồn lương vào tổng quỹ
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print("⇒ KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")
