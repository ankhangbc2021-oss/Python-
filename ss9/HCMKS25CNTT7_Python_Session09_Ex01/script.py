"""
Lession 9
"""
# (1) Phân tích lỗi
# Sau khi chạy delivery_orders.insert(0, "GE000")  
# → "GE000" được chèn vào đầu danh sách, các phần tử cũ dịch sang phải.
# Kết quả: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"].

# Vì sao dòng delivery_orders[1] = "GE002-UPDATED" sửa sai đơn hàng cần cập nhật?  
# → Sau khi chèn "GE000" vào đầu, phần tử ở index 1 là "GE001", không phải "GE002". Do đó lệnh này sửa nhầm "GE001".

# Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index nào?  
# → "GE002" nằm ở index 2.

# Vì sao dòng delivery_orders.remove(3) gây lỗi?  
# → remove() nhận giá trị cần xóa, không phải chỉ số. Ở đây truyền số 3 (kiểu int), nhưng trong danh sách không có phần tử nào bằng 3, nên báo lỗi ValueError.

# Phương thức remove() xóa phần tử theo giá trị hay theo vị trí?  
# → Xóa theo giá trị.

# Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh như thế nào?  
# → delivery_orders.remove("GE003-CANCEL").

# Phương thức pop() có tác dụng gì?  
# → Xóa phần tử khỏi danh sách và trả về chính phần tử vừa bị xóa.

# Vì sao chương trình báo lỗi khi in biến transferred_order?  
# → Vì chưa gán kết quả trả về của pop() vào biến transferred_order.

# Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh như thế nào?  
# → transferred_order = delivery_orders.pop().

# (2). Sửa lỗi
# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
delivery_orders[1] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)
