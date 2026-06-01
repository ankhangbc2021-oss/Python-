"""
(1) Phân tích & Thiết kế giải pháp
Input / Output
Input:

Lựa chọn menu chính (1–4).

Lựa chọn menu con (1–4) khi cập nhật đơn hàng.

Mã đơn hàng (chuỗi).

Trạng thái đơn hàng (chuỗi).

Vị trí đơn hàng (số nguyên).

Output:

Danh sách đơn hàng hiện tại.

Thông báo thêm, sửa, xóa đơn hàng.

Thống kê số lượng đơn hàng theo trạng thái.

Thông báo thoát chương trình.

Thông báo lỗi khi nhập sai dữ liệu.

Giải pháp
Sử dụng vòng lặp while True để hiển thị menu chính.

Dùng strip() để loại bỏ khoảng trắng, upper() để chuẩn hóa mã và trạng thái.

Thêm đơn hàng bằng append().

Sửa đơn hàng bằng gán giá trị qua index (sau khi kiểm tra hợp lệ).

Xóa đơn hàng bằng pop(index) (sau khi kiểm tra hợp lệ).

Thống kê bằng cách duyệt qua danh sách, tách trạng thái và đếm.

Edge cases:

Nhập sai menu → báo lỗi.

Nhập sai vị trí → báo lỗi.

Nhập chữ thay vì số → báo lỗi.

Danh sách rỗng → hiển thị số lượng 0.

Pseudocode
Mã
order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]

while True:
    in ra menu chính
    nhập lựa chọn
    nếu không hợp lệ → báo lỗi
    nếu == 1 → hiển thị danh sách
    nếu == 2 → hiển thị menu con
        nếu chọn 1 → thêm đơn hàng
        nếu chọn 2 → sửa đơn hàng theo vị trí
        nếu chọn 3 → xóa đơn hàng theo vị trí
        nếu chọn 4 → quay lại menu chính
    nếu == 3 → thống kê đơn hàng theo trạng thái
    nếu == 4 → thoát

"""

# (2) Source Code Python Hoàn Chỉnh
# Danh sách đơn hàng ban đầu
order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("> Mời bạn chọn chức năng (1-4): ")

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
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")

                sub_choice = input("> Mời bạn chọn chức năng (1-4): ")

                if not sub_choice.isdigit():
                    print("Lựa chọn không hợp lệ!")
                    continue

                sub_choice = int(sub_choice)

                match sub_choice:
                    case 1:
                        code = input("Nhập mã đơn hàng: ").strip().upper()
                        status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                        if code and status:
                            order_list.append(f"{code} - {status}")
                            print(f"Đã thêm đơn hàng: {code} - {status}")
                        else:
                            print("Mã đơn hàng và trạng thái không được bỏ trống!")

                    case 2:
                        pos = input("Nhập vị trí đơn hàng cần sửa: ")
                        if not pos.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue
                        pos = int(pos) - 1
                        if 0 <= pos < len(order_list):
                            code = input("Nhập mã đơn hàng mới: ").strip().upper()
                            status = input("Nhập trạng thái mới: ").strip().upper()
                            if code and status:
                                order_list[pos] = f"{code} - {status}"
                                print(f"Đã cập nhật đơn hàng ở vị trí {pos+1}")
                            else:
                                print("Mã đơn hàng và trạng thái không được bỏ trống!")
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case 3:
                        pos = input("Nhập vị trí đơn hàng cần xóa: ")
                        if not pos.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue
                        pos = int(pos) - 1
                        if 0 <= pos < len(order_list):
                            removed = order_list.pop(pos)
                            print(f"Đã xóa đơn hàng: {removed}")
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case 4:
                        break

                    case _:
                        print("Lựa chọn không hợp lệ!")

        case 3:
            pending = delivering = completed = cancelled = 0
            for order in order_list:
                parts = order.split(" - ")
                if len(parts) == 2:
                    status = parts[1]
                    if status == "PENDING":
                        pending += 1
                    elif status == "DELIVERING":
                        delivering += 1
                    elif status == "COMPLETED":
                        completed += 1
                    elif status == "CANCELLED":
                        cancelled += 1

            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print("PENDING:", pending)
            print("DELIVERING:", delivering)
            print("COMPLETED:", completed)
            print("CANCELLED:", cancelled)
            print("Tổng số đơn hàng:", len(order_list))

        case 4:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

