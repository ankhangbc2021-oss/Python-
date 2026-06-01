"""
while True:
    in ra menu
    nhập lựa chọn
    nếu lựa chọn không phải số hoặc ngoài 1-5:
        báo lỗi và yêu cầu nhập lại
    nếu == 1:
        nhập dữ liệu video
        kiểm tra tên tài khoản và mô tả không rỗng
        xử lý chuẩn hóa và in báo cáo
    nếu == 2:
        nhập tên tài khoản
        kiểm tra rỗng
        chuẩn hóa thành @ + lowercase
    nếu == 3:
        nhập hashtag
        kiểm tra hợp lệ theo quy tắc
        in kết quả
    nếu == 4:
        nhập từ khóa cần tìm và thay thế
        kiểm tra tồn tại trong mô tả
        thay thế và in kết quả
    nếu == 5:
        in "Thoát chương trình"
        break

"""

# Menu
while True:
    print(f"\n+{"="*48}+")
    print("|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK        |")
    print(f"+{"="*48}+")
    print("|    1. nhập và phân tích thông tin video        |")
    print("|    2. Chuẩn hóa tên tài khoản                  |")
    print("|    3. Kiểm tra tính hợp lệ hashtag             |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong mô tả |")
    print("|    5. Thoát chương trình                       |")
    print(f"+{"="*48}+")

    choice = input("> Mời bạn chọn chức năng (1 - 5): ")

    match (choice):
        case "1":
            account = input("Nhập tên tài khoản người đăng video: ").strip()
            if not account:
                print("Tên tài khoản không được rỗng")
                continue

            title = input("Nhập tiêu đề video: ").strip()

            description = input("Nhập mô tả video: ").strip()
            if not description:
                print("Mô tả video không được rỗng")
                continue

            hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            hashtags_list = [h.strip() for h in hashtags.split(",") if h.strip()]

            print("\n--- Báo cáo thống kê ---")
            print("Tên tài khoản:", account)
            print("Tiêu đề:", title.title())
            print("Mô tả:", description)
            print("Độ dài mô tả:", len(description))
            print("Số lượng từ trong mô tả:", len(description.split()))
            print("Danh sách hashtag:", hashtags_list)
            print("Số lượng hashtag:", len(hashtags_list))
            print("Mô tả chữ thường:", description.lower())
            print("Mô tả chữ hoa:", description.upper())

        case "2":
            account = input("Nhập tên tài khoản: ").strip()
            if not account:
                print("Tên tài khoản không được rỗng")
                continue

            normalized = "@" + account.lower()

            print("Tên tài khoản ban đầu:", account)
            print("Tên tài khoản sau khi được chuẩn hoá:", normalized)

        case "3":
            hashtag = input("Nhập hashtag: ").strip()

            if not hashtag:
                print("Hashtag không được rỗng")
                continue
            if not hashtag.startswith("#"):
                print("Hashtag phải bắt đầu bằng ký tự #")
                continue
            if " " in hashtag:
                print("Hashtag không được chứa khoảng trắng")
                continue
            if len(hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự")
                continue
            if not all(c.isalnum() or c == "_" for c in hashtag[1:]):
                print("Hashtag chỉ nên chứa chữ cái, chữ số hoặc dấu gạch dưới")
                continue
            print("Hashtag hợp lệ")
        case "4":
            description = input("Nhập mô tả video: ").strip()
            if not description:
                print("Mô tả video không được rỗng")
                continue
            keyword = input("Nhập từ khóa cần tìm: ")
            replacement = input("Nhập từ khóa thay thế: ")
            count = description.count(keyword)
            if count > 0:
                new_desc = description.replace(keyword, replacement)
                print("Mô tả sau khi thay thế:", new_desc)
                print("Số lần từ khóa xuất hiện:", count)
            else:
                print("Không tìm thấy từ khóa trong mô tả")
        case "5":
            print("Bạn đã thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ hãy nhập từ 1-5")
