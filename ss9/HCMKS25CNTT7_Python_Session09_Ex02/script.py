"""
(1) Phân tích lỗi
Sau khi chạy express_orders.insert(0, "GE100-FAST")  
→ "GE100-FAST" được chèn vào đầu danh sách, các phần tử cũ dịch sang phải.
Kết quả: ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"].

Vì sao dòng express_orders[1] = "GE102-UPDATED" sửa nhầm đơn hàng "GE101"?  
→ Sau khi chèn "GE100-FAST" vào đầu, phần tử ở index 1 là "GE101", không phải "GE102-WRONG". Do đó lệnh này sửa nhầm "GE101".

Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" đang nằm ở index nào?  
→ "GE102-WRONG" nằm ở index 2.

Vì sao dòng express_orders.pop(3) không xóa đúng đơn hàng bị hủy?  
→ pop(3) xóa phần tử ở vị trí index 3, nhưng sau khi chèn "GE100-FAST", vị trí index 3 lại là "GE103-CANCEL" chỉ khi chưa thêm "GE104". Sau khi thêm "GE104", "GE103-CANCEL" nằm ở index 3, nhưng việc dùng pop() để xóa theo vị trí dễ gây nhầm lẫn. Đúng nghiệp vụ là phải xóa theo giá trị "GE103-CANCEL".

Nếu muốn xóa đúng đơn hàng "GE103-CANCEL", nên dùng remove() như thế nào?  
→ express_orders.remove("GE103-CANCEL").

Phương thức pop() không truyền index sẽ lấy phần tử ở đâu trong danh sách?  
→ Mặc định lấy phần tử cuối cùng.

Vì sao dòng current_order = express_orders.pop() lấy sai đơn hàng đang giao?  
→ Vì pop() mặc định lấy phần tử cuối cùng ("GE104"), trong khi yêu cầu là lấy phần tử đầu tiên ("GE100-FAST").

Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết lệnh như thế nào?  
→ current_order = express_orders.pop(0).

Muốn chương trình cho ra kết quả đúng, cần sửa lại những dòng nào?

Sửa "GE102-WRONG" đúng vị trí: express_orders[2] = "GE102-UPDATED".

Xóa "GE103-CANCEL" bằng remove("GE103-CANCEL").

Lấy đơn hàng đầu tiên bằng pop(0) thay vì pop().

"""
# (2) Source Code đã sửa

# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai (GE102-WRONG thành GE102-UPDATED)
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)
