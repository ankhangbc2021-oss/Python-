"""
Shopee Cart Management System - Bài tập tổng hợp ss10
"""

cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000],
]

while True:
    print("\n" + "=" * 50)
    print("         SHOPEE CART MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("=" * 50)
    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            print("\n----CHI TIẾT GIỎ HÀNG ---")
            print(
                f"{'STT':<3}|{'Mã SP':^6}|{'Tên Sản Phẩm':<25}|{'SL':^5}|{'Đơn giá':<15}|{'Thành tiền':<15}"
            )
            print("-" * 69)
            total_price = 0
            total_quantity = 0
            for i, item in enumerate(cart_items, start=1):
                id_product, name_product, quantity, price = item
                total_amount = quantity * price
                format_amount = f"{total_amount:,}"
                format_price = f"{price:,}"
                total_quantity += quantity
                total_price += total_amount
                print(
                    f"{i:<3}|{id_product:^6}|{name_product:<25}|{quantity:^5}|{format_price + 'đ':<15}|{format_amount + 'đ':<15}"
                )
            print("-" * 69)
            print("=> Tổng số lượng sản phẩm trong giỏ:", total_quantity)
            print(f"=> TỔNG TIỀN THANH TOÁN {total_price:,}đ")

        case "2":
            product_id = input("Nhập mã sản phẩm: ")
            name = input("Nhập tên sản phẩm: ")
            try:
                quantity = int(input("Nhập số lượng: "))
                price = int(input("Nhập đơn giá: "))
            except ValueError:
                print("Số lượng và đơn giá phải là số nguyên.")
                continue

            if quantity <= 0 or price < 0:
                print("Số lượng phải > 0 và đơn giá ≥ 0.")
                continue

            found = False
            for item in cart_items:
                if item[0] == product_id:
                    item[2] += quantity
                    found = True
                    print("Đã cộng dồn số lượng.")
                    break
            if not found:
                cart_items.append([product_id, name, quantity, price])
                print("Đã thêm sản phẩm mới.")

        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ")
            try:
                new_quantity = int(input("Nhập số lượng mới: "))
            except ValueError:
                print("Số lượng phải là số nguyên.")
                continue

            if new_quantity <= 0:
                print("Số lượng phải > 0.")
                continue

            found = False
            for item in cart_items:
                if item[0] == product_id:
                    item[2] = new_quantity
                    found = True
                    print("Đã cập nhật số lượng.")
                    break
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ")
            found = False
            for item in cart_items:
                if item[0] == product_id:
                    cart_items.remove(item)
                    found = True
                    print("Đã xóa sản phẩm.")
                    break
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "5":
            print("Bạn đã thoát chương trình.")
            break

        case _:
            print("Vui lòng nhập số từ 1-5.")
