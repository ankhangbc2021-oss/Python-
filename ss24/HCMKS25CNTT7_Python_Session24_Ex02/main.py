"""
(1) Phân tích lỗi – Code Review
Hậu quả nếu để points public:
→ Dữ liệu có thể bị gán thành số âm hoặc chuỗi, gây mất toàn vẹn dữ liệu (Data Integrity) và làm crash các phép toán cộng trừ điểm.

Decorator để tạo “bộ lọc” kiểm tra dữ liệu khi gán:
→ Dùng @points.setter (kết hợp với @property). Setter cho phép kiểm duyệt dữ liệu trước khi thay đổi giá trị.

Vì sao self trong is_eligible_for_voucher là dư thừa:
→ Hàm này không dùng đến bất kỳ dữ liệu nào của đối tượng (self), chỉ dựa vào tham số bill_amount. Việc bắt buộc truyền self khiến thiết kế rườm rà và sai nguyên lý.

Decorator cần dùng để biến hàm thành tiện ích độc lập:
→ Dùng @staticmethod.

Khác biệt với @classmethod:

@staticmethod không nhận tham số hệ thống nào (self hay cls).

@classmethod nhận cls để thao tác với biến cấp lớp.

(2) Sửa lỗi – Refactoring
"""


# Hệ thống Thẻ thành viên Rikkei Coffee
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = points  # Đóng gói bằng Name Mangling

    # Getter: đọc điểm an toàn
    @property
    def points(self):
        return self.__points

    # Setter: kiểm duyệt dữ liệu trước khi gán
    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng thêm không hợp lệ!")

    # Static Method: tiện ích độc lập
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


# --- KỊCH BẢN KIỂM CHỨNG ---
card1 = MemberCard("Le Van C", 100)

# 1. Thu ngân gõ nhầm, gán điểm thành số âm
card1.points = -50  # Hệ thống từ chối
print(f"Điểm hiện tại sau khi gán sai: {card1.points}")

# 2. Kiểm tra voucher trực tiếp từ Class
result = MemberCard.is_eligible_for_voucher(250000)

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")
