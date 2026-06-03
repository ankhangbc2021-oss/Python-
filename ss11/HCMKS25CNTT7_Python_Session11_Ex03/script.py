"""
(1) Phân tích và thiết kế giải pháp
Input / Output
Input: Người dùng nhập lựa chọn menu (1–5) và có thể nhập thêm thông tin sản phẩm (mã, tên, giá, số lượng).

Output: Hiển thị danh sách sản phẩm, thông báo thêm/cập nhật/xóa thành công hoặc thông báo lỗi (mã trùng, không tồn tại, dữ liệu không hợp lệ, lựa chọn sai).

Giải pháp
Sử dụng list chứa các dictionary để quản lý sản phẩm.

Dùng vòng lặp while True để hiển thị menu liên tục cho đến khi chọn thoát.

Chuẩn hóa mã sản phẩm bằng .strip().upper().

Kiểm tra dữ liệu hợp lệ:

Mã sản phẩm không trùng khi thêm.

Giá và số lượng phải là số nguyên dương (isdigit() và >0).

Khi cập nhật/xóa, kiểm tra sản phẩm có tồn tại trong danh sách.

Xử lý nhập sai menu bằng try/except và kiểm tra phạm vi.

Pseudocode
while True:
    hiển thị menu
    nhập lựa chọn
    nếu lựa chọn == 1:
        hiển thị danh sách sản phẩm
    nếu lựa chọn == 2:
        nhập thông tin sản phẩm mới
        chuẩn hóa mã
        kiểm tra trùng mã
        kiểm tra giá và số lượng hợp lệ
        nếu hợp lệ -> thêm vào danh sách
    nếu lựa chọn == 3:
        nhập mã sản phẩm cần cập nhật
        chuẩn hóa mã
        tìm sản phẩm
        nếu tồn tại -> cho phép cập nhật tên, giá, số lượng
        nếu không -> báo lỗi
    nếu lựa chọn == 4:
        nhập mã sản phẩm cần xóa
        chuẩn hóa mã
        tìm sản phẩm
        nếu tồn tại -> xóa
        nếu không -> báo lỗi
    nếu lựa chọn == 5:
        thoát chương trình
    ngược lại:
        báo "Lựa chọn không hợp lệ"
(2) Triển khai Code Python
"""

# sp ban đầu
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15,
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10,
    },
]

# Menu
while True:
    print(
        "\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====\n"
        "1. Hiển thị danh sách sản phẩm\n"
        "2. Thêm sản phẩm mới\n"
        "3. Cập nhật thông tin sản phẩm\n"
        "4. Xóa sản phẩm theo mã\n"
        "5. Thoát chương trình"
    )
    choice = input("Chọn chức nắng 1-5: ")
    match (choice):
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
                continue

            print("\nDanh sách sản phẩm hiện tại:")
            for i, item in enumerate(product_list, start=1):
                print(
                    f"{i}. Mã SP: {item["product_id"]:<6} | "
                    f"Tên: {item["product_name"]:<20} | "
                    f"Giá: {item["price"]:<15,} | "
                    f"Số lượng: {item["quantity"]:<3}"
                )
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            exit_ids = {item["product_id"] for item in product_list}

            if product_id in exit_ids:
                print("Mã sản phẩm bị trùng")
                continue
            product_name = input("Nhập tên sản phẩm: ")

            try:
                price = int(input("Nhập giá sản phẩm: "))
                quantity = int(input("Nhập số lượng sản phẩm: "))
                if price <= 0 or quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                    continue
            except ValueError:
                print("Giá/Số lượng không hợp lệ")
                continue
            product_list.append(
                {
                    "product_id": product_id,
                    "product_name": product_name,
                    "price": price,
                    "quantity": quantity,
                }
            )
            print("Thêm sản phẩm thành công")
        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            for p in product_list:
                if p["product_id"] == product_id:
                    p["product_name"] = input("Nhập tên sản phẩm mới: ").strip()
                    try:
                        price = int(input("Nhập giá sản phẩm mới: ").strip())
                        quantity = int(input("Nhập số lượng tồn kho mới: ").strip())
                        if price <= 0 or quantity <= 0:
                            print("Giá/Số lượng không hợp lệ!")
                            continue
                        p["price"] = price
                        p["quantity"] = quantity
                        print("Cập nhật sản phẩm thành công!")
                    except ValueError:
                        print("Giá/Số lượng không hợp lệ!")
                    continue
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
        case "4":
            check = False
            product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            for p in product_list:
                if p["product_id"] == product_id:
                    product_list.remove(p)
                    check = True
                    break

            if check is True:
                print("Xóa sản phẩm thành công!")
            else:
                print("Không tìm thấy mã sản phẩm cần xoá!")
        case "5":
            print("Đã thoát")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
