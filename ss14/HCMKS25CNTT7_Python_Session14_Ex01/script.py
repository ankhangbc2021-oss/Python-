"""
(1) Phân tích lỗi
Thứ tự tham số bị sai  
Hàm được định nghĩa là calculate_final_price(price, discount, shipping_fee).
Nhưng khi gọi hàm: calculate_final_price(100000, 15000, 0.1) thì:

price = 100000 (đúng).

discount = 15000 (sai, lẽ ra phải là 0.1).

shipping_fee = 0.1 (sai, lẽ ra phải là 15000).

Công thức bị sai lệch  
Khi tính:

total = 100000 - (100000 * 15000) + 0.1
tức là 100000 - 1,500,000,000 + 0.1 = -1,499,999,899.9.
Đây chính là lý do ra số âm khổng lồ.

Lỗi TypeError ở dòng final_payment = order_total + 5000  
Vì hàm chỉ print() mà không return, nên order_total nhận giá trị mặc định là None.
Khi cộng None + 5000 thì Python báo lỗi TypeError.

Giá trị của order_total  
order_total = None vì hàm không có return.

Khác biệt giữa print() và return

print() chỉ hiển thị ra màn hình, không lưu giá trị cho biến.

return trả về kết quả để gán cho biến và dùng tiếp trong chương trình.

Cách sửa hàm  
Thay vì print(total), cần dùng return total. Đồng thời truyền đúng thứ tự tham số khi gọi hàm.

"""
# (2) Sửa lỗi – Source Code chuẩn
# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total  # Trả về kết quả thay vì chỉ in ra

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)
