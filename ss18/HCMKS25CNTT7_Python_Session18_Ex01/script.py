# =========================
# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG ĐẠI LÝ
# =========================


def display_orders(orders):
    """Hiển thị danh sách đơn hàng dưới dạng bảng"""
    if not orders:
        print("Danh sách đơn hàng trống!")
        return
    print(f"{'Mã đơn':<10}{'Tên đại lý':<25}{'Giá trị':>15}{'Trạng thái':>10}")
    print("-" * 60)
    for order in orders:
        print(
            f"{order['id']:<10}{order['name']:<25}{order['price']:>15,}{order['status']:>10}"
        )


def add_order(orders):
    """Thêm mới đơn hàng"""
    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()
        if not order_id:
            print("Mã đơn hàng không được để trống!")
            continue
        if any(o["id"] == order_id for o in orders):
            print("ERR-01: Mã đơn hàng đã tồn tại, hủy thao tác.")
            return
        break

    while True:
        name = input("Nhập tên đại lý: ").strip()
        if not name:
            print("Tên đại lý không được để trống!")
            continue
        break

    while True:
        try:
            price = int(input("Nhập giá trị đơn hàng: "))
            if price <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Giá trị phải là số nguyên!")

    orders.append({"id": order_id, "name": name, "price": price, "status": "Unpaid"})
    print("Thêm đơn hàng thành công!")


def update_order_status(orders):
    """Cập nhật trạng thái thanh toán"""
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    for order in orders:
        if order["id"] == order_id:
            if order["status"] == "Unpaid":
                order["status"] = "Paid"
                print("Cập nhật trạng thái thành công!")
                return
            else:
                print("ERR-04: Đơn hàng đã thanh toán trước đó.")
                return
    print("ERR-03: Không tìm thấy mã đơn hàng.")


def calculate_revenue(orders):
    """Tính tổng doanh thu và chiết khấu"""
    total = sum(o["price"] for o in orders if o["status"] == "Paid")
    discount_percent = 5 if total >= 100_000_000 else 0
    discount_amount = total * discount_percent / 100
    return total, discount_percent, discount_amount


def main():
    orders = [
        {
            "id": "HD01",
            "name": "Dai ly Hoang Long",
            "price": 45000000,
            "status": "Paid",
        },
        {
            "id": "HD02",
            "name": "Tap hoa Minh Thu",
            "price": 15000000,
            "status": "Unpaid",
        },
    ]

    while True:
        print("\n===== MENU QUẢN LÝ ĐƠN HÀNG =====")
        print("1. Xem danh sách đơn hàng")
        print("2. Tạo mới đơn hàng")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & chiết khấu")
        print("5. Thoát chương trình")

        try:
            choice = int(input("Nhập lựa chọn: "))
        except ValueError:
            print("Vui lòng nhập số từ 1-5!")
            continue

        if choice == 1:
            display_orders(orders)
        elif choice == 2:
            add_order(orders)
        elif choice == 3:
            update_order_status(orders)
        elif choice == 4:
            total, percent, discount = calculate_revenue(orders)
            print(f"Tổng doanh thu: {total:,} VND")
            print(f"Chiết khấu: {percent}%")
            print(f"Số tiền chiết khấu: {discount:,} VND")
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


if __name__ == "__main__":
    main()
