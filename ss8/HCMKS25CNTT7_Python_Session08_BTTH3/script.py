"""
(1) Phân tích & Thiết kế giải pháp
Input / Output
Input:

Lựa chọn menu (số nguyên 1–5).
Dữ liệu đơn hàng: tên người gửi, số điện thoại, địa chỉ lấy hàng, tên người nhận, số điện thoại, địa chỉ giao hàng, ghi chú.
Mã đơn hàng.
Từ khóa cần tìm và thay thế trong ghi chú.

Output:
Báo cáo thống kê đơn hàng (chuẩn hóa tên, địa chỉ, ghi chú).
Mã đơn hàng chuẩn hóa.
Số điện thoại đã được ẩn.
Ghi chú sau khi thay thế từ khóa.
Thông báo thoát chương trình.

Giải pháp
Sử dụng vòng lặp while True để hiển thị menu và yêu cầu nhập lựa chọn.
Kiểm tra dữ liệu nhập bằng strip(), title(), lower(), upper().
Chuẩn hóa mã đơn hàng: strip(), upper(), thay khoảng trắng bằng -, thêm tiền tố GRAB- nếu chưa có.
Kiểm tra số điện thoại: chỉ chứa số, độ dài đúng 10, sau đó ẩn bằng cách giữ 3 số đầu + 2 số cuối, phần giữa thay bằng *.
Thay thế từ khóa trong ghi chú bằng replace().
Edge cases: nhập rỗng, nhập sai menu, nhập không phải số, chưa có ghi chú mà chọn chức năng 4.

Pseudocode

while True:
    in ra menu
    nhập lựa chọn
    nếu không phải số hoặc ngoài 1-5:
        báo lỗi
    nếu == 1:
        nhập dữ liệu đơn hàng
        kiểm tra rỗng
        chuẩn hóa và in báo cáo
    nếu == 2:
        nhập mã đơn hàng
        chuẩn hóa và in kết quả
    nếu == 3:
        nhập số điện thoại
        kiểm tra hợp lệ
        ẩn số và in kết quả
    nếu == 4:
        nếu chưa có ghi chú từ chức năng 1:
            báo lỗi
        ngược lại:
            nhập từ khóa cần tìm và thay thế
            thay thế nếu có
    nếu == 5:
        thoát

"""
# (2) Triển khai Code Python với
note = None

while True:
    print("\n+================================================+")
    print("| HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS         |")
    print("+================================================+")
    print("| 1. Nhập dữ liệu đơn hàng và xem báo cáo        |")
    print("| 2. Chuẩn hóa mã đơn hàng                       |")
    print("| 3. Ẩn số điện thoại khách hàng                 |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong ghi chú  |")
    print("| 5. Thoát chương trình                          |")
    print("+================================================+")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    choice = int(choice)

    match choice:
        case 1:
            sender = input("Tên người gửi: ").strip()
            if not sender:
                print("Tên người gửi không được bỏ trống")
                continue
            sender_phone = input("SĐT người gửi: ").strip()
            if not sender_phone:
                print("SĐT người gửi không được bỏ trống")
                continue
            pickup_address = input("Địa chỉ lấy hàng: ").strip()
            if not pickup_address:
                print("Địa chỉ lấy hàng không được bỏ trống")
                continue
            receiver = input("Tên người nhận: ").strip()
            if not receiver:
                print("Tên người nhận không được bỏ trống")
                continue
            receiver_phone = input("SĐT người nhận: ").strip()
            if not receiver_phone:
                print("SĐT người nhận không được bỏ trống")
                continue
            delivery_address = input("Địa chỉ giao hàng: ").strip()
            if not delivery_address:
                print("Địa chỉ giao hàng không được bỏ trống")
                continue
            note = input("Ghi chú giao hàng: ").strip()
            if not note:
                print("Ghi chú giao hàng không được rỗng")
                continue

            print("\n--- Báo cáo thống kê ---")
            print("Tên người gửi:", sender.title())
            print("Tên người nhận:", receiver.title())
            print("Địa chỉ lấy hàng:", " ".join(pickup_address.split()))
            print("Địa chỉ giao hàng:", " ".join(delivery_address.split()))
            print("Ghi chú:", note)
            print("Độ dài ghi chú:", len(note))
            print("Số lượng từ trong ghi chú:", len(note.split()))
            print("Ghi chú chữ thường:", note.lower())
            print("Ghi chú chữ hoa:", note.upper())

        case 2:
            order_code = input("Nhập mã đơn hàng: ").strip()
            if not order_code:
                print("Mã đơn hàng không được bỏ trống")
                continue
            normalized = order_code.upper().replace(" ", "-")
            if not normalized.startswith("GRAB-"):
                normalized = "GRAB-" + normalized
            print("Mã đơn hàng ban đầu:", order_code)
            print("Mã đơn hàng chuẩn hóa:", normalized)

        case 3:
            sender_phone = input("Nhập SĐT người gửi: ").strip()
            receiver_phone = input("Nhập SĐT người nhận: ").strip()

            if not sender_phone.isdigit():
                print("SĐT người gửi không hợp lệ")
            elif len(sender_phone) != 10:
                print("SĐT người gửi không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            else:
                masked_sender = sender_phone[:3] + "*" * 5 + sender_phone[-2:]
                print("SĐT người gửi:", masked_sender)

            if not receiver_phone.isdigit():
                print("SĐT người nhận không hợp lệ")
            elif len(receiver_phone) != 10:
                print("SĐT người nhận không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            else:
                masked_receiver = receiver_phone[:3] + "*" * 5 + receiver_phone[-2:]
                print("SĐT người nhận:", masked_receiver)

        case 4:
            if not note:
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue
            keyword = input("Nhập từ khóa cần tìm: ")
            replacement = input("Nhập từ khóa thay thế: ")
            count = note.count(keyword)
            if count > 0:
                new_note = note.replace(keyword, replacement)
                print("Số lần xuất hiện của từ khóa:", count)
                print("Ghi chú sau khi thay thế:", new_note)
            else:
                print("Không tìm thấy từ khóa trong ghi chú")

        case 5:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
