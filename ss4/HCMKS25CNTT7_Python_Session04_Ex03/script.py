"""Chương trình kiểm toán"""
# Số lượng trong ca
bills = []
N = int(input("Nhập số lượng hóa đơn trong ca: "))

for i in range (0, N):
    bill = int(input(f"Nhập giá trị hóa đơn thứ {i + 1}: "))
    bills.append(bill)

max_bill = max(bills)
min_bill = min(bills)

#In ra màn
print("----Kết quả kiểm toán ca RIKKEI STORE----")
print(f"Hóa đơn giá trị cao nhất: {max_bill} VND")
print(f"Hóa đơn có giá trị thấp nhất: {min_bill} VND")