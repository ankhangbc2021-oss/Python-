"""
(Phân tích):

(1) Tài liệu Thiết kế Lớp – Class Design Document
Class: MenuItem

Class Attributes (Thuộc tính Lớp):

service_charge: Phụ phí dịch vụ chung cho toàn hệ thống (float, mặc định 0.0).

Instance Attributes (Thuộc tính Đối tượng):

item_id: Mã món (public).

item_name: Tên món (public).

__base_price: Giá gốc (private, bảo mật bằng Name Mangling).

__is_available: Trạng thái bán (private, bảo mật bằng Name Mangling, mặc định True).

Methods (Các Phương thức):

__init__(self, item_id, item_name, base_price): Khởi tạo mã, tên, giá gốc, trạng thái mặc định là “Đang bán”.

Getters/Setters:

@property base_price: Trả về giá gốc.

@base_price.setter: Kiểm tra giá mới > 0, nếu không hợp lệ thì báo lỗi và giữ nguyên giá cũ.

@property is_available: Trả về trạng thái bán.

Instance Methods:

toggle_availability(self): Đảo trạng thái bán (True ↔ False).

calculate_selling_price(self): Tính giá niêm yết = base_price + (base_price * service_charge).

Class Methods:

update_service_charge(cls, new_rate): Cập nhật phụ phí dịch vụ cho toàn hệ thống.

Static Methods:

is_valid_item_id(item_code): Kiểm tra mã món hợp lệ (2 chữ cái in hoa + 2 chữ số).

(2) Triển khai Code – Source Code Python
"""


class MenuItem:
    # Class Attribute
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    # Getter & Setter cho base_price
    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if isinstance(new_price, (int, float)) and new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0! Giá cũ được giữ nguyên.")

    # Getter cho trạng thái bán
    @property
    def is_available(self):
        return self.__is_available

    # Instance Method: Đảo trạng thái bán
    def toggle_availability(self):
        self.__is_available = not self.__is_available
        status = "ĐANG BÁN" if self.__is_available else "HẾT HÀNG"
        print(f">> Đã cập nhật {self.item_name} thành {status}!")

    # Instance Method: Tính giá niêm yết
    def calculate_selling_price(self):
        return self.__base_price + (self.__base_price * MenuItem.service_charge)

    # Class Method: Cập nhật phụ phí dịch vụ
    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate
        print("Cập nhật phụ phí dịch vụ thành công!")

    # Static Method: Kiểm tra mã món hợp lệ
    @staticmethod
    def is_valid_item_id(item_code):
        return (
            len(item_code) == 4
            and item_code[:2].isalpha()
            and item_code[:2].isupper()
            and item_code[2:].isdigit()
        )


# ================= MAIN FLOW =================
menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000),
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")
    print("======================================================")
    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
        for i, item in enumerate(menu_db, 1):
            status = "Đang bán" if item.is_available else "Hết hàng"
            print(
                f"{i}. Mã: {item.item_id} | Tên: {item.item_name} | Trạng thái: {status} | Giá niêm yết: {item.calculate_selling_price():,} VNĐ"
            )

    elif choice == "2":
        print("\n--- THÊM MÓN MỚI VÀO MENU ---")
        item_id = input("Nhập mã món: ").strip()
        if not MenuItem.is_valid_item_id(item_id):
            print(
                "Mã món không hợp lệ! Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01."
            )
            continue
        if find_item(item_id):
            print("Mã món đã tồn tại trong hệ thống!")
            continue
        item_name = input("Nhập tên món: ").strip()
        base_price = int(input("Nhập giá gốc: "))
        new_item = MenuItem(item_id, item_name, base_price)
        menu_db.append(new_item)
        print("Thêm món mới thành công!")

    elif choice == "3":
        print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
        item_id = input("Nhập mã món cần cập nhật: ").strip()
        item = find_item(item_id)
        if not item:
            print("Không tìm thấy món trong hệ thống!")
            continue
        item.toggle_availability()

    elif choice == "4":
        print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
        item_id = input("Nhập mã món cần đổi giá: ").strip()
        item = find_item(item_id)
        if not item:
            print("Không tìm thấy món trong hệ thống!")
            continue
        new_price = int(input("Nhập giá tiền mới: "))
        item.base_price = new_price

    elif choice == "5":
        print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
        print(f"Phụ phí hiện tại: {MenuItem.service_charge*100}%")
        new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
        MenuItem.update_service_charge(new_rate)

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-6.")
