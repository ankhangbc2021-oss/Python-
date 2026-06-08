"""
BTTH 1
"""


# Hàm menu
def display_menu():
    """Menu hiển thị màn hình để lựa chọn"""
    print(
        "\n========== TECHSTORE MANAGEMENT SYSTEM ==========\n"
        "1. Nhập thêm hàng vào kho\n"
        "2. Bán hàng (Tính toán hóa đơn)\n"
        "3. Xem báo cáo tổng quan\n"
        "4. Thoát chương trình\n"
        "=================================================\n"
    )


class Inventory:
    """
    Lớp này sử lý đơn hàng trong đó có số lượng và doanh thu
    """

    def __init__(self):
        # Sô lượng và doanh thu ban đầu
        self.stock = 100
        self.total_revenue = 0.0

    def add_stock(self, amount: int):
        """Thêm số lượng sp

        Args:
            amount (int): số lượng sp
        """
        self.stock += amount
        print(f"Đã thêm thành công {amount} sản phẩm")

        print("Tồn kho hiện tại:", self.stock)

    def process_sale(self, quantity: int) -> bool:
        """Bán hàng

        Args:
            quantity (int): Số lượng

        Returns:
            bool: True or False
        """

        if quantity > self.stock:
            print(f"Không đủ hàng trong kho.Tồn kho hiện tại còn {self.stock}")
            return False

        return True

    def calculate_final_price(self, quantity: int, price: float) -> float:
        """Tính chi phí

        Args:
            quantity (int): Số lượng
            price (float): Số tiền

        Returns:
            float: Tổng tiền cuối cùng
        """
        subtotal = quantity * price

        print(f"Tạm tính: ${subtotal:,.1f}")

        if subtotal >= 1000:
            discount = subtotal * 0.1
            print(f"Giảm giá (10%): ${discount:,.1f}")
            final_total = subtotal * 0.9
        else:
            final_total = subtotal

        vat = final_total * 0.08
        final_total += vat

        print(f"Thế VAT (8%): ${vat:,.1f}")
        print(f"Tổng thanh toán: ${final_total:,.1f}")

        self.stock -= quantity
        self.total_revenue += final_total
        print("Đã bán thành công!")
        return final_total

    def print_report(self):
        """Hàm hiện báo cáo kinh doanh"""
        print("--- BÁO CÁO KINH DOANH ---")
        print(f"Tồn kho hiện tại: {self.stock} sản phẩm")
        print(f"Tổng doanh thu: ${self.total_revenue:,.1f}")


# Tạo đối tượng
my_store = Inventory()

# Chức năng
while True:
    display_menu()
    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            print("--- NHẬP HÀNG ---")
            in_amount = input("Nhập số lượng sản phẩm muốn thêm: ")

            if in_amount.isdigit():
                in_amount = int(in_amount)

                if in_amount <= 0:
                    print("Số lượng phải lớn hơn 0")
                    continue

                my_store.add_stock(in_amount)
            else:
                print("Số lượng không hợp lệ")
        case "2":
            print("--- BÁN HÀNG ---")
            in_quantity = input("Nhập số lượng mua: ")
            if not in_quantity.isdigit():
                print("Vui lòng nhập số")
                continue

            in_quantity = int(in_quantity)
            if in_quantity <= 0:
                print("Vui lòng nhập số lượng > 0")
                continue

            if my_store.process_sale(in_quantity) is False:
                continue

            in_price = input("Nhập đơn giá ($): ")
            if not in_price.isdigit():
                print("Vui lòng nhập số")
                continue
            in_price = float(in_price)

            if in_price <= 0:
                print("Giá tiền phải lớn hơn 0")
                continue

            my_store.calculate_final_price(in_quantity, in_price)

        case "3":
            my_store.print_report()
        case "4":
            print("Đã thoát")
            break
        case _:
            print("Vui lòng chọn 1-4")
