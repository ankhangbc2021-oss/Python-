laptop = 0
phone = 0
tablet = 0

while True:
    print("========= MENU =========")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    print("--------------------------")
    choice = input("Nhập lựa chọn của bạn: ")
# chức năng 1: xem báo cáo tồn kho
    if choice == "1":

        print("\n===== BÁO CÁO TỒN KHO =====")
        print(f"Laptop: {laptop}")
        print(f"Phone: {phone}")
        print(f"Tablet: {tablet}")

        print("\n===== BIỂU ĐỒ TỒN KHO =====")

        # Laptop
        stars = ""
        for i in range(laptop):
            stars += "*"
        print(f"Laptop ({laptop}): {stars}")

        # Phone
        stars = ""
        for i in range(phone):
            stars += "*"
        print(f"Phone ({phone}): {stars}")

        # Tablet
        stars = ""
        for i in range(tablet):
            stars += "*"
        print(f"Tablet ({tablet}): {stars}")
# chức năng 2: nhập kho
    elif choice == "2":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = int(input("Chọn mặt hàng cần nhập: "))

        # Kiểm tra số lượng hợp lệ
        while True:
            quantity = int(input("Nhập số lượng cần thêm: "))

            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
            else:
                break

        # Cộng dồn hàng
        if product == 1:
            laptop += quantity
            print("Nhập kho Laptop thành công!")

        elif product == 2:
            phone += quantity
            print("Nhập kho Phone thành công!")

        elif product == 3:
            tablet += quantity
            print("Nhập kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

# chức năng 3: Xuất kho
    elif choice == "3":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = int(input("Chọn mặt hàng cần xuất: "))

        # Kiểm tra số lượng hợp lệ
        while True:
            quantity = int(input("Nhập số lượng cần xuất: "))

            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
            else:
                break

        # Kiểm tra tồn kho và xuất hàng
        if product == 1:

            if quantity > laptop:
                print("Không đủ hàng!")
            else:
                laptop -= quantity
                print("Xuất kho Laptop thành công!")

        elif product == 2:

            if quantity > phone:
                print("Không đủ hàng!")
            else:
                phone -= quantity
                print("Xuất kho Phone thành công!")

        elif product == 3:

            if quantity > tablet:
                print("Không đủ hàng!")
            else:
                tablet -= quantity
                print("Xuất kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")
# chức năng 4: Cảnh báo hàng tồn kho thấp
    elif choice == "4":

        print("\n===== CẢNH BÁO TỒN KHO =====")

        if laptop < 10:
            print(f"[CẢNH BÁO] Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")

        if phone < 10:
            print(f"[CẢNH BÁO] Phone sắp hết (Chỉ còn {phone} sản phẩm)")

        if tablet < 10:
            print(f"[CẢNH BÁO] Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")
# chức năng 5: thoát
    elif choice == "5":

        print("Thoát chương trình...")
        break
    else:
        print("Lựa chọn không hợp lệ!")