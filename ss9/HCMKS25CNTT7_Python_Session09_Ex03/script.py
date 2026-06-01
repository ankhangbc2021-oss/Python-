"""
(1) Phân tích & Thiết kế giải pháp
Input / Output
Input:

Lựa chọn menu (số nguyên 1–4).

Mã đơn hàng mới (chuỗi).

Mã đơn hàng cần xóa (chuỗi).

Output:

Danh sách đơn hàng hiện tại (theo định dạng yêu cầu).

Thông báo khi thêm hoặc xóa đơn hàng.

Thông báo khi thoát chương trình.

Thông báo lỗi khi nhập sai lựa chọn hoặc mã không tồn tại.

Giải pháp
Sử dụng vòng lặp while True để hiển thị menu liên tục.

Dùng strip() để loại bỏ khoảng trắng, upper() để chuẩn hóa mã đơn hàng.

Dùng append() để thêm đơn hàng mới vào cuối danh sách.

Dùng remove() để xóa đơn hàng theo giá trị, kết hợp kiểm tra tồn tại bằng in.

Edge cases:

Nhập mã đơn hàng viết thường hoặc thừa khoảng trắng → chuẩn hóa.

Xóa mã không tồn tại → thông báo lỗi.

Nhập sai lựa chọn menu hoặc nhập chữ cái → thông báo lỗi.

Pseudocode
Mã
order_list = ["GE001", "GE002", "GE003"]

while True:
    in ra menu
    nhập lựa chọn
    nếu không phải số hoặc ngoài 1-4:
        báo lỗi
    nếu == 1:
        nếu danh sách rỗng:
            in "Danh sách trống"
        ngược lại:
            in danh sách với số thứ tự
    nếu == 2:
        nhập mã mới
        chuẩn hóa
        thêm vào cuối danh sách
    nếu == 3:
        nhập mã cần xóa
        chuẩn hóa
        nếu tồn tại:
            xóa
        ngược lại:
            báo lỗi
    nếu == 4:
        in "Thoát chương trình"
        break

"""
# (2) Source Code Python Hoàn Chỉnh
# Danh sách đơn hàng ban đầu
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("> Mời bạn chọn chức năng (1-4): ")

    # Kiểm tra lựa chọn hợp lệ
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            if order_list:
                print("Danh sách đơn hàng hiện tại:")
                for i, order in enumerate(order_list, start=1):
                    print(f"{i}. {order}")
            else:
                print("Danh sách đơn hàng hiện đang trống.")

        case 2:
            new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
            if new_order:
                order_list.append(new_order)
                print(f"Đã thêm đơn hàng {new_order} vào danh sách.")
            else:
                print("Mã đơn hàng không được bỏ trống!")

        case 3:
            del_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
            if del_order in order_list:
                order_list.remove(del_order)
                print(f"Đã xóa đơn hàng {del_order} khỏi danh sách.")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")

        case 4:
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
