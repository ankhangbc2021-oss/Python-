"""Miniproject"""

# Dữ liệu ban đầu
orders = [
    {"id": "HD01", "name": "Dai ly Hoang Long", "price": 45000000, "status": "Paid"},
    {"id": "HD02", "name": "Tap hoa Minh Thu", "price": 15000000, "status": "Unpaid"},
]


def get_validate_input(prompt: str, input_type: str = "str") -> str:
    """Nhập và kiểm tra

    Args:
        prompt (str): Câu hỏi
        input_type (str, optional): dữ liệu kiểm tra. Defaults to "str".

    Returns:
        str: trả về
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Dữ liệu không được để trống")
            continue

        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu không được âm và bằng 0")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ. Nhập lại")
                continue
        return user_input


def display_menu() -> str:
    """Hiển thị menu

    Returns:
        str: trả về giá trị
    """

    print(
        f"{'='*50}\n"
        f"{"QUẢN LÝ ĐƠN HÀNG - AGENT ORDER":^50}\n"
        f"{'='*50}\n"
        "1. Xem danh sách đơn hàng hiện có\n"
        "2. Tạo mới đơn hàng đại lý\n"
        "3. Cập nhật trạng thái thanh toán\n"
        "4. Tính tổng doanh thu & Chiết khấu\n"
        "5. Thoát chương trình\n"
        f"{'='*50}"
    )
    return input("Bạn chọn 1-5: ")


def display_list(my_list: list) -> str:
    """Hiện thành phần trong mảng

    Args:
        my_list (list): list hiện

    Returns:
        str: trả về print
    """
    for order in my_list:
        print(
            f"{order.get("id", "Lỗi"):<7} | "
            f"{order.get("name", "Lỗi"):<20} | "
            f"{order.get("price", "Lỗi"):<15} | "
            f"{order.get("status", "Lỗi"):<10} |"
        )


def display_order():
    """Xem danh sách hàng"""
    if not orders:
        print("Hệ thống hiện chưa có đơn nào!")
        return

    title = f"{'MÃ ĐƠN':<7} | {'TÊN ĐẠI LÝ':<20} | {'GIÁ TRỊ (VNĐ)':<15} | {'TRẠNG THÁI':<10} |"
    print("--- DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ---")
    print(title)
    print("-" * len(title))
    display_list(orders)

def main():
    """Thực thi chức năng"""
    while True:
        choice = display_menu()

        match choice:
            case "1":
                display_order()
            case "2":
                print()
            case "3":
                print()
            case "4":
                print()
            case "5":
                print("Đã thoát")
                break
            case _:
                print("Vui lòng nhập 1-5")


if __name__ == "__main__":
    main()
