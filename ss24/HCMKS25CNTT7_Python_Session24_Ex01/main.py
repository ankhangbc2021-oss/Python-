"""
(1) Phân tích lỗi – Code Review
Vi phạm tính chất cốt lõi nào?
→ Việc gán trực tiếp order_table1.total_amount = 0 từ bên ngoài vi phạm Encapsulation (Đóng gói).

Đổi tên thuộc tính để kích hoạt Name Mangling:
→ Đổi thành __total_amount (dùng 2 dấu gạch dưới đầu tên).

Decorator để cho phép đọc giá trị an toàn:
→ Dùng @property để tạo getter chỉ đọc.

Hành động thực chất của self.vat_rate = new_rate:
→ Python tạo một biến instance mới tên vat_rate cho riêng đối tượng đó, che khuất biến class vat_rate. Vì vậy chỉ bàn 1 thay đổi, bàn 2 vẫn giữ giá trị cũ.

Decorator để cập nhật thuế cho toàn bộ hệ thống:
→ Dùng @classmethod, thay tham số self bằng cls.

(2) Sửa lỗi – Refactoring
"""


# Hệ thống quản lý hóa đơn Rikkei Coffee
class CoffeeOrder:
    # Thuộc tính của lớp (Class Attribute)
    vat_rate = 0.10  # Mặc định thuế VAT là 10%

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0  # Bảo vệ bằng Name Mangling

    # Phương thức thêm tiền món ăn vào hóa đơn
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    # Cho phép đọc tổng tiền một cách an toàn
    @property
    def total_amount(self):
        return self.__total_amount

    # Tính tổng tiền khách phải trả (đã cộng VAT)
    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder.vat_rate)

    # Cập nhật thuế VAT cho toàn bộ hệ thống
    @classmethod
    def update_vat_rate(cls, new_rate):
        cls.vat_rate = new_rate


# --- KỊCH BẢN KIỂM CHỨNG ---
order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

# Khách gọi món
order_table1.add_item(50000)  # Bàn 1 gọi Cà phê sữa
order_table2.add_item(30000)  # Bàn 2 gọi Trà đào

# 1. Nhân viên gian lận cố gán đè tổng tiền (KHÔNG THỂ vì __total_amount bị ẩn)
# order_table1.__total_amount = 0  # Không tác động được
# order_table1.total_amount = 0    # Lỗi: property không cho gán

# 2. Quản lý chi nhánh cập nhật thuế VAT xuống 8% cho toàn hệ thống
CoffeeOrder.update_vat_rate(0.08)

print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Tổng tiền Bàn 2 (sau VAT): {order_table2.calculate_final_bill()} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {CoffeeOrder.vat_rate}")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {CoffeeOrder.vat_rate}")
