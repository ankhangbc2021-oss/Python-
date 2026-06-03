"""
Hệ Thống Quản Lý Giỏ Hàng AMAZON
"""

# Dữ liệu ban đầu
cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000},
]

while True:
    print(
        "\n====================================================\n"
        "           SHOPEE CART MANAGEMENT SYSTEM\n"
        "====================================================\n"
        "1. Xem chi tiết giỏ hàng & Tính tổng tiền\n"
        "2. Thêm sản phẩm mới / Cộng dồn số lượng\n"
        "3. Cập nhật số lượng của một sản phẩm\n"
        "4. Xóa sản phẩm khỏi giỏ hàng\n"
        "5. Thoát chương trình\n"
        "===================================================="
    )
    choice = input("Mời bạn chọn chức năng (1-5): ")

    match (choice):
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(
                f"{'STT':<5}| "
                f"{'Mã SP':^6}| "
                f"{'Tên Sản Phẩm':<25}| "
                f"{'SL':^3}| "
                f"{'Đơn giá':<15}| "
                f"{'Thành tiền':<15}"
            )
            print("-" * 78)
            total_number = 0
            total_price = 0
            for i, item in enumerate(cart_items, start=1):
                total_number += item["number"]
                total_price += item["number"] * item["price"]
                print(
                    f"{i:<5}| "
                    f"{item["id"]:^6}| "
                    f"{item["name"]:<25}| "
                    f"{item["number"]:^3}| "
                    f"{f"{item["price"]:,}đ":<15}| "
                    f"{f"{item["number"] * item["price"]:,}đ":<15}"
                )
            print("-" * 78)
            print("=>Tổng số lượng sản phẩm trong giỏ:", total_number)
            print(f"=>TỔNG TIỀN THANH TOÁN: {total_price:,}đ")
        case "2":
            fool = True
            index = -1
            id = input("Mã sản phẩm: ").strip().upper()

            for i, item in enumerate(cart_items, start=0):
                if id == item["id"]:
                    index = i
                    fool = False
                    break

            if fool is True:
                name_item = input("Tên sản phẩm: ").strip()
            try:
                check = True
                quantity = int(input("Số lượng: "))
                if fool is True:
                    price = int(input("Đơn giá: "))
                    if price <= 0:
                        check = False
                if quantity <= 0 or check is False:
                    print("Số lượng/Giá không được âm")
                    continue
            except ValueError:
                print("Số lượng/Giá không được số")
                continue

            if fool is True:
                print("Chưa có đã thêm")
                cart_items.append(
                    {
                        "id": id,
                        "name": name_item,
                        "number": quantity,
                        "price": price,
                    }
                )
            else:
                if index != -1:
                    print("Có rồi đã cộng thêm số lượng")
                    cart_items[index]["number"] += quantity
                else:
                    print("Lỗi")
        case "3":
            update_id = (
                input("Nhập mã sản phẩm cần cập nhật số lượng: ").strip().upper()
            )
            product = next(
                (item for item in cart_items if item["id"] == update_id), None
            )

            if product:
                try:
                    new_qty = int(input(f"Nhập số lượng mới cho {product['name']}: "))
                    if new_qty > 0:
                        product["number"] = new_qty
                        print("Cập nhật số lượng thành công!")
                    else:
                        print("Số lượng phải lớn hơn 0.")
                except ValueError:
                    print("Số lượng phải là số nguyên!")
            else:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
        case "4":
            delete_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()
            product = next(
                (item for item in cart_items if item["id"] == delete_id), None
            )

            if product:
                cart_items.remove(product)
                print(f"Đã xóa sản phẩm {product['name']} khỏi giỏ hàng.")
            else:
                print("Không tìm thấy mã sản phẩm để xóa.")
        case "5":
            print("\nĐã thoát chương trình")
            break
        case _:
            print("\nLỗi. Vui lòng nhập (1-5)")
