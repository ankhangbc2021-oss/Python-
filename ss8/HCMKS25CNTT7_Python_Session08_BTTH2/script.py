"""
(1) Phân tích & Thiết kế giải pháp
Input / Output
Input:
Lựa chọn menu (số nguyên 1–5).
Dữ liệu sản phẩm: tên shop, tên sản phẩm, mô tả, danh mục, danh sách từ khóa.
Mã giảm giá.
Từ khóa cần tìm và thay thế trong mô tả.

Output:
Báo cáo thống kê sản phẩm (chuẩn hóa tên, mô tả, danh mục, từ khóa).
Tên shop chuẩn hóa.
Kết quả kiểm tra mã giảm giá (hợp lệ hoặc lý do không hợp lệ).
Mô tả sản phẩm sau khi thay thế từ khóa.

Thông báo thoát chương trình.
Giải pháp
Sử dụng vòng lặp while True để hiển thị menu và yêu cầu nhập lựa chọn.
Kiểm tra dữ liệu nhập bằng strip(), lower(), upper(), title().
Chuẩn hóa tên shop: strip(), lower(), thay khoảng trắng bằng -, thêm tiền tố shop- nếu chưa có.
Kiểm tra mã giảm giá bằng các điều kiện: không rỗng, không chứa khoảng trắng, độ dài 6–12, viết hoa, chỉ chứa chữ cái và số, bắt đầu bằng SALE.
Thay thế từ khóa trong mô tả bằng replace().
Edge cases: nhập rỗng, nhập sai menu, nhập không phải số.

Pseudocode

while True:
    in ra menu
    nhập lựa chọn
    nếu không phải số hoặc ngoài 1-5:
        báo lỗi
    nếu == 1:
        nhập dữ liệu sản phẩm
        kiểm tra shop và mô tả không rỗng
        chuẩn hóa và in báo cáo
    nếu == 2:
        nhập tên shop
        chuẩn hóa và in kết quả
    nếu == 3:
        nhập mã giảm giá
        kiểm tra hợp lệ
    nếu == 4:
        nhập mô tả, từ khóa cần tìm, từ khóa thay thế
        thay thế nếu có
    nếu == 5:
        thoát

"""
# (2) Triển khai Code Python (không dùng hàm)
discount_codes = []

while True:
    print("\n+===========================================+")
    print("| HỆ THỐNG QUẢN LÝ SẢN PHẨM TMĐT            |")
    print("+===========================================+")
    print("| 1. Nhập dữ liệu sản phẩm và xem báo cáo   |")
    print("| 2. Chuẩn hóa tên shop                     |")
    print("| 3. Kiểm tra mã giảm giá hợp lệ            |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả|")
    print("| 5. Thoát chương trình                     |")
    print("+===========================================+")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    choice = int(choice)

    match choice:
        case 1:
            shop_name = input("Nhập tên shop: ").strip()
            if not shop_name:
                print("Tên shop không được bỏ trống")
                continue

            product_name = input("Nhập tên sản phẩm: ").strip()
            description = input("Nhập mô tả sản phẩm: ").strip()
            if not description:
                print("Mô tả sản phẩm không được rỗng")
                continue

            category = input("Nhập danh mục sản phẩm: ").strip().lower()
            keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")
            keywords_list = [k.strip() for k in keywords.split(",") if k.strip()]

            print("\n--- Báo cáo thống kê ---")
            print("Tên shop:", shop_name)
            print("Tên sản phẩm:", product_name.title())
            print("Mô tả sản phẩm:", description)
            print("Độ dài mô tả:", len(description))
            print("Danh mục sản phẩm:", category)
            print("Danh sách từ khóa:", keywords_list)
            print("Số lượng từ khóa:", len(keywords_list))
            print("Mô tả chữ thường:", description.lower())
            print("Mô tả chữ hoa:", description.upper())

        case 2:
            shop_name = input("Nhập tên shop: ").strip()
            if not shop_name:
                print("Tên shop không được bỏ trống")
                continue
            normalized = shop_name.lower().replace(" ", "-")
            if not normalized.startswith("shop-"):
                normalized = "shop-" + normalized
            print("Tên shop ban đầu:", shop_name)
            print("Tên shop chuẩn hóa:", normalized)

        case 3:
            code = input("Nhập mã giảm giá: ").strip()
            if not code:
                print("Mã giảm giá không được rỗng")
                continue
            if " " in code:
                print("Mã giảm giá không được chứa khoảng trắng")
                continue
            if not (6 <= len(code) <= 12):
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
                continue
            if not code.isupper():
                print("Mã giảm giá phải viết hoa toàn bộ")
                continue
            if not code.isalnum():
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
                continue
            if not code.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng SALE")
                continue
            print("Mã giảm giá hợp lệ")
            discount_codes.append(code)
            print("Danh sách mã giảm giá hiện tại:", discount_codes)

        case 4:
            description = input("Nhập mô tả sản phẩm: ").strip()
            if not description:
                print("Mô tả sản phẩm không được rỗng")
                continue
            keyword = input("Nhập từ khóa cần tìm: ")
            replacement = input("Nhập từ khóa thay thế: ")
            count = description.count(keyword)
            if count > 0:
                new_desc = description.replace(keyword, replacement)
                print("Số lần xuất hiện của từ khóa:", count)
                print("Mô tả sau khi thay thế:", new_desc)
            else:
                print("Không tìm thấy từ khóa trong mô tả")

        case 5:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
