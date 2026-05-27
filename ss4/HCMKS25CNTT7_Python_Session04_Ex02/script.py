"""Weekly Revenue Report - Rikkei Store"""

# Chức năng 1: Nhập doanh thu từng ngày (7 ngày)
revenues = []
for day in range(1, 8):
    revenue = int(input(f"Nhập doanh thu Ngày {day}: "))
    revenues.append(revenue)

# Chức năng 2: Tính toán tổng và trung bình
total_revenue = sum(revenues)
average_revenue = total_revenue // len(revenues)

# Chức năng 3: Đếm số ngày đạt mục tiêu >= 5,000,000 VND
target_days = sum(1 for r in revenues if r >= 5000000)

print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print("Tổng doanh thu cả tuần:", total_revenue, "VND")
print("Doanh thu trung bình mỗi ngày:", average_revenue, "VND")
print("Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND):", target_days, "ngày")
