"""Kiểm tra"""

# Dữ liệu sản phẩm ban đầu
products = [
    {"id": "P01", "name": "Coca Cola", "price": 15000},
    {"id": "P02", "name": "Bánh mì", "price": 20000},
]


def display_menu() -> str:
    """Hiển thị menu

    Returns:
        str: Trả về giá trị
    """
    print(
        f"{"="*50}\n"
        f"{"QUẢN LÝ CỦA HÀNG - MINI STORE":^50}\n"
        f"{"="*50}\n"
        "1. Xem danh sách sản phẩm hiện có\n"
        "2. Thêm mới một sản phẩm\n"
        "3. Cập nhật giá sản phẩm theo ID\n"
        "4. Thoát chương trình\n"
        f"{"="*50}\n"
    )
    return input("Vui lòng chọn 1-5: ")


def display_products():
    """Hiển thị danh sách"""
    if not products:
        products("Cửa hàng hiện chưa có sản phẩm nào!")
        return

    title = f"{'ID':<5} | {'Tên sản phẩm':<20} | {'Giá bán':<15} |"
    print("--- DANH SÁCH SẢN PHẨM ---")
    print(title)
    print("-" * len(title))
    for item in products:
        print(
            f"{item.get("id", "Lỗi"):<5} | "
            f"{item.get("name", "Lỗi"):<20} | "
            f"{item.get("price", "Lỗi"):<15,} |"
        )


def add_product():
    """Thêm sản phẩm mới vào list"""
    check = True
    check_price = True
    print("--- THÊM SẢN PHẨM MỚI ---")
    while True:
        if check is True:
            id = input("Nhập mã sản phẩm (ID): ").strip()
        else:
            id = input("Nhập lại: ").strip()

        if not id:
            print("Mã sản phẩm không được để trống")
            check = False
            continue
        value_list = [item for item in products if item["id"].lower() == id.lower()]
        if value_list:
            print("Mã sản phẩm đã trùng!")
            check = False
            continue
        break
    name_product = input("Nhập tên sản phẩm: ").strip()

    while True:
        if check_price is True:
            price = input("Nhập giá bán: ").strip()
        else:
            price = input("Nhập lại: ").strip()

        try:
            price = int(price)
            if price <= 0:
                print("Giá bán phải lớn hơn 0!")
                check_price = False
                continue
        except ValueError:
            print("Vui lòng nhập số nguyên!")
            check_price = False
            continue
        break

    products.append({"id": id, "name": name_product, "price": price})
    print("Đã thêm sản phẩm thành công")


def update_price(products_list):
    found = False
    find_id = input("Nhập ID sản phẩm cần thay đổi giá : ").strip().upper()
    for item in products_list:
        if item["id"] == find_id:
            found = True
            print(f"Tìm thấy sản phẩm : {item['name']} (Giá hiện tại: {item['price']})")
            while True :
                update_price =input("Nhập giá bán mới : ")
                if int(update_price) < 0:
                    print("Vui lòng nhập lại giá !")
                else:
                    break
            item["price"] = int(update_price)
            print("Cập nhật giá thành công!")
            break
    if not found:
        print(f"Không tìm thấy sản phẩm có mã [{find_id}]!")


def main():
    """Thực thi chương trình"""
    while True:
        choice = display_menu()

        match choice:
            case "1":
                display_products()
            case "2":
                add_product()
            case "3":
                update_price(products)
            case "4":
                print("Đã thoát")
                break
            case _:
                print("Vui lòng nhập 1-5")


if __name__ == "__main__":
    main()
