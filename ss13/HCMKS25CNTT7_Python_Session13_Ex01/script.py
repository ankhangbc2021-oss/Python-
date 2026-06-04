"""
SRS - Smart Parking System
"""

# Data lưu trữ
data = []
# Menu
id = 0

while True:
    print(
        "\n=============================================\n"
        "       QUẢN LÝ BÃI XE - SMART PARKING\n"
        "=============================================\n"
        "1. Check-in (Đăng ký xe vào)\n"
        "2. Báo cáo tồn kho (Hiển thị danh sách)\n"
        "3. Tìm kiếm xe (Theo biển số)\n"
        "4. Check-out (Xử lý xe ra & Tính phí)\n"
        "5. Thoát chương trình\n"
        "============================================="
    )

    choice = input("Nhập lựa chọn của bạn (1-5): ")
    if choice == "1":
        id += 1
        plate = input("Nhập mã định danh xe: ").strip()
        list_item = [item for item in data if item["plate"] == plate]
        if list_item:
            print("Đã có mã định danh này rồi")
            continue

        entry_time = -1
        while True:
            try:
                type_int = int(
                    input("\nNhập loại xe :\n1. (Xe máy)\n2. (Ô tô)\nBạn chọn?")
                )

                if type_int not in (1, 2):
                    print("Vui lòng chọn 1-2")
                    continue

            except ValueError:
                print("Vui lòng nhập số")
                continue
            break

        while True:
            try:

                entry_time = int(input("Giờ vào (0-24): "))
                if entry_time < 0 and entry_time > 24:
                    print("Vui lòng nhập từ 0-24")
                    continue
            except ValueError:
                print("Vui lòng nhập số")
                continue
            break

        data.append(
            {"id": id, "plate": plate, "type": type_int, "entry_time": entry_time}
        )
        print(f"[Thành công]: Xe [{plate}] đã được đăng ký vào bãi")

    elif choice == "2":
        if len(data) == 0:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue

        print(f"{"ID":<5}| {"Biển số xe":<10}| {"Loại xe":<10}| {"Giờ vào":<8}")
        print("-" * 45)
        for item in data:

            if item["type"] == 1:
                TYPE_TEXT = "Xe máy"
            else:
                TYPE_TEXT = "Ô tô"

            print(
                f"{item["id"]:<5}| "
                f"{item["plate"]:<10}| "
                f"{TYPE_TEXT:<10}| "
                f"{item["entry_time"]:<8}"
            )

    elif choice == "3":

        if len(data) == 0:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue

        plate_search = input("Nhập biển số cần tìm: ").strip()

        plate_value = [item for item in data if item["plate"] == plate_search]
        if plate_value:
            print("Thông tin chi tiết:", *plate_value)
        else:
            print(f"[Lỗi]: Không tìm thây biển số {plate_search} trong hệ thống!")
    elif choice == "4":

        if len(data) == 0:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue

        plate_search = input("Nhập biển số cần ra: ").strip()
        plate_value = [item for item in data if item["plate"] == plate_search]

        if not plate_value:
            print(f"[Lỗi]: Không tìm thây biển số [{plate_search}] trong hệ thông!")
            continue

        for item in plate_value:
            id_resule = item["id"]
            entry_time = item["entry_time"]
            break

        exit_time = -1
        while True:
            try:
                exit_time = int(input("Nhập giờ ra: "))
                if exit_time < 0 and exit_time > 24:
                    print("Vui lòng nhập từ 0-24")
                    continue
            except ValueError:
                print("[Lỗi]: Vui lòng nhập số")
                continue
            break

        if exit_time < entry_time:
            print("[Lõi]: Giờ ra phải sau hoặc băng giờ vào!")
            continue
        else:
            total_price = (exit_time - entry_time) * 7500
            print(f"Tổng phí phải trả: {total_price:,}VNĐ")

            data = [item for item in data if item["id"] != id_resule]
            print(f"[Thành công]: Đã xóa xe ID {id_resule} thành công!")

    elif choice == "5":
        print("Đã thoát")
        break
    else:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
