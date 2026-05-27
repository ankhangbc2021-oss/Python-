"""
Hệ thống kiểm toán tổng kết doanh thu toàn diện của cửa hàng trước khi đóng cửa.
"""
# Biến ban đầu
client = 1
bills = []
# Bắt đầu code
WL_CHECK = True

while WL_CHECK is True:
    check = True

    bill = int(input(f"Khách hàng {client} - Nhập giá trị hóa đơn: "))
    bills.append(bill)

    while check is True:
        input_check = input("Có muốn nhập tiếp không? (C/K): ").strip()
        if input_check in ("C", "c"):
            client += 1
            check = False
        elif input_check in ("K", "k"):
            WL_CHECK = False
            check = False
        else:
            check = True

total_revenue = sum(bills)
sum_revenue = sum(1 for b in bills if b > 1000000)
percent = (sum_revenue / len(bills)) * 100

print("---Báo cáo doanh thu cuối ngày---")
print(f"Tổng số hóa đơn đã xử lý: {client} hóa đơn.")
print(f"Tổng doanh thu ngày hôm nay: {total_revenue:,} VND.")
print(f"Số hóa đơn lớn (>= 1.000.000 VND): {sum_revenue} hóa đơn.")
print(f"Tỷ lệ hóa đơn lớn đạt: {float(percent)}% trên tổng hóa số đơn hàng.")
