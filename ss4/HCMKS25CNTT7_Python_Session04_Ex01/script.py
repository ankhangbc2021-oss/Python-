"""Rikkei Store Billing System"""

# Chức năng 1: Nhập tổng số tiền ban đầu
initial_amount = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

# Chức năng 2: Tính số tiền giảm giá
if initial_amount >= 500000:
    DISCOUNT = int(initial_amount * 0.1)
else:
    DISCOUNT = 0

# Chức năng 3: Tính số tiền thực tế phải trả
final_amount = initial_amount - DISCOUNT

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print("Số tiền được giảm giá:", DISCOUNT, "VND")
print("Tổng tiền khách phải trả:", final_amount, "VND")
