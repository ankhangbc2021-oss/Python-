"""(1) Phân tích lỗi"""
# Nguyên nhân: Trong code ban đầu, vòng lặp ngoài duyệt theo tháng, vòng lặp trong duyệt theo chi nhánh. Điều này khiến dữ liệu được in ra theo thứ tự tháng → chi nhánh, tức gom theo tháng chứ không gom theo chi nhánh.
# Theo yêu cầu nghiệp vụ: Báo cáo cần gom dữ liệu theo từng chi nhánh.
# → Vòng lặp ngoài phải duyệt theo chi nhánh.
# → Vòng lặp trong phải duyệt theo tháng.
# (2) Sửa lỗi – Source Code chuẩn

"""(2) Sửa lỗi"""
# Báo cáo doanh thu theo chi nhánh - Rikkei Store

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

revenues = [[0] * month_count for _ in range(branch_count)]

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        revenues[branch - 1][month - 1] = revenue

print("-------------- Kết quả --------------")
for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        print(f"Chi nhánh {branch}, tháng {month}: {revenues[branch - 1][month - 1]} triệu đồng")
