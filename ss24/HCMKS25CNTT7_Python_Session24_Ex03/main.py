"""
1) Phân tích Thiết kế (Code Review & Architecture)
Tại sao point_value_vnd là Class Attribute?
Vì đây là quy định chung cho toàn hệ thống (1 điểm = 1000 VNĐ). Nếu khai báo trong __init__ (Instance Attribute), mỗi thẻ sẽ có giá trị riêng biệt. Khi cập nhật tỷ giá ở Chức năng 5, chỉ một đối tượng thay đổi, các thẻ khác vẫn giữ giá trị cũ → gây sai lệch và mất đồng bộ.

Tại sao is_valid_card_id dùng @staticmethod?
Vì hàm này chỉ kiểm tra định dạng chuỗi card_id, không liên quan đến dữ liệu của bất kỳ đối tượng nào. Không cần tạo object mới để kiểm tra. Static Method cho phép gọi trực tiếp từ Class: MemberCard.is_valid_card_id("RC01").

Encapsulation với __points và __tier:
Giúp ngăn chặn việc gán đè hoặc sửa dữ liệu từ bên ngoài. Ví dụ: thu ngân không thể tự ý card.points = 1000. Điểm và hạng chỉ thay đổi thông qua các phương thức nghiệp vụ (earn_points, redeem_points). Điều này đảm bảo bảo mật dữ liệu và tính toàn vẹn.

(2) Triển khai Code – Refactoring
"""


class MemberCard:
    # Class Attribute
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    # Getter cho points
    @property
    def points(self):
        return self.__points

    # Getter cho tier
    @property
    def tier(self):
        return self.__tier

    # Instance Method: Tích điểm
    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {self.__points}")
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Instance Method: Đổi điểm
    def redeem_points(self, points_to_use):
        if (
            isinstance(points_to_use, int)
            and points_to_use > 0
            and points_to_use <= self.__points
        ):
            self.__points -= points_to_use
            discount = points_to_use * MemberCard.point_value_vnd
            print(f"Đã trừ {points_to_use} điểm.")
            print(f"Khách hàng được giảm giá {discount} VNĐ vào hóa đơn!")
        else:
            print("Không thể đổi điểm!")
            print(f"Số điểm muốn sử dụng vượt quá số điểm hiện có hoặc không hợp lệ.")
        print(f"Số điểm sau giao dịch: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Static Method: Kiểm tra mã thẻ
    @staticmethod
    def is_valid_card_id(card_id):
        return len(card_id) == 4 and card_id.startswith("RC") and card_id[2:].isdigit()

    # Class Method: Cập nhật tỷ giá
    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value
        print(
            f"Cập nhật tỷ giá thành công! Tỷ giá mới: 1 điểm = {cls.point_value_vnd} VNĐ"
        )


# ================= MAIN FLOW =================
cards_database = []


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
    print("6. Thoát chương trình")
    print("======================================================")
    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
        for i, card in enumerate(cards_database, 1):
            print(
                f"{i}. Mã: {card.card_id} | Tên: {card.name} | Điểm: {card.points} | Hạng: {card.tier}"
            )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
        card_id = input("Nhập mã thẻ: ").strip()
        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không hợp lệ! Phải có dạng RCxx (xx là 2 chữ số).")
            continue
        if find_card(card_id):
            print("Mã thẻ đã tồn tại trong hệ thống! Vui lòng kiểm tra lại.")
            continue
        name = input("Nhập tên khách hàng: ").strip()
        new_card = MemberCard(card_id, name)
        cards_database.append(new_card)
        print("\nĐăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {new_card.card_id}")
        print(f"Tên khách hàng: {new_card.name}")
        print(f"Điểm ban đầu: {new_card.points}")
        print(f"Hạng thẻ: {new_card.tier}")

    elif choice == "3":
        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
        card_id = input("Nhập mã thẻ: ").strip()
        card = find_card(card_id)
        if not card:
            print("Không tìm thấy thẻ trong hệ thống!")
            continue
        bill = int(input("Nhập tổng tiền hóa đơn: "))
        print(f"\nKhách hàng: {card.name}")
        print(f"Hóa đơn: {bill:,} VNĐ")
        card.earn_points(bill)

    elif choice == "4":
        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
        card_id = input("Nhập mã thẻ: ").strip()
        card = find_card(card_id)
        if not card:
            print("Không tìm thấy thẻ trong hệ thống!")
            continue
        points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
        print(f"\nKhách hàng: {card.name}")
        card.redeem_points(points_to_use)

    elif choice == "5":
        print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
        print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd} VNĐ")
        new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))
        MemberCard.update_point_value(new_value)

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-6.")
