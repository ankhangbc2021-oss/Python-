"""
Hệ Thống Quản lý Bãi Xe (Smart Parking)
"""

# Dữ liệu lưu trữ
data = []

# id tự tăng
ID_ = 0

# Menu
while True:
    print(
        "\n======================================\n"
        "   QUẢN LÝ BÃI XE - SMART PARKING\n"
        "======================================\n"
        "1. Thêm xe mới vào bãi\n"
        "2. Hiển thị danh sách xe trong bãi\n"
        "3. Xóa xe khỏi bãi (khi xe ra)\n"
        "4. Thoát chương trình\n"
        "======================================"
    )

    choice = input("Nhập chức năng 1-4: ")

    match (choice):
        case "1":
            ID_ += 1

            while True:
                type_str = input("Nhập loại xe (vd: O to, Xe may): ").strip()
                if type_str == "":
                    print("Loại xe không được để trống")
                else:
                    break

            while True:
                owner_str = input("Nhập tên chủ xe: ").strip().title()
                if owner_str == "":
                    print("Chủ xe không được để trống")
                else:
                    break
            data.append({"id": ID_, "type": type_str, "owner": owner_str})

        case "2":
            if not data:
                print("Bãi xe hiện đang trống!")
                continue

            print(f"{"ID":<5}| " f"{"Loại xe":<20}| " f"{"Chủ xe":<25}|")
            print("-" * 55)

            for item in data:
                print(
                    f"{item["id"]:<5}| " f"{item["type"]:<20}| " f"{item["owner"]:<25}|"
                )

        case "3":
            if not data:
                print("Bãi xe hiện đang trống!")
                continue

            while True:
                try:
                    id_search = int(input("Nhập id để xóa: "))
                except ValueError:
                    print("Vui lòng nhập số")
                    continue
                break

            data_search = [item for item in data if item["id"] == id_search]

            if data_search:
                data = [item for item in data if item["id"] != id_search]
                print(f"Đã xóa xe ID [{id_search}] thành công!")
            else:
                print("Không tìm thấy xe để xóa!")
                continue

        case "4":
            print("Bạn đã thoát")
            break

        case _:
            print("Vui lòng nhập 1-4")
