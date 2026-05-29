raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


def get_clean_data(raw):
    """
    Làm sạch dữ liệu data
    """

    raw = raw.strip()
    segments = raw.split("|")
    clean_list = []

    for item in segments:
        parts = [p.strip() for p in item.split(";")]
        parts[0] = parts[0].upper()
        parts[1] = parts[1].strip().title()
        parts[3] = parts[3].upper()
        parts[2] = parts[2].replace("-", "").replace(" ", "")
        clean_list.append(parts)
    return clean_list


data_list = get_clean_data(raw_data)

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    print("-" * 40)
    choice = input("Bạn chọn? ")

    if choice == "1":
        print(raw_data)

    elif choice == "2":
        for i, sub in enumerate(data_list, 1):
            phone = sub[2]
            is_text_phone = any(char.isalpha() for char in sub[2])

            if is_text_phone:
                phone_number = "Invalid Format"
            else:
                phone_number = "******" + phone[6:]

            print(f"Nhân viên thứ {i}:")
            print(f"  - Mã ID:       {sub[0]}")
            print(f"  - Họ tên:      {sub[1]}")
            print(f"  - Số ĐT:       {phone_number}")
            print(f"  - Phòng ban:   {sub[3]}")
            print("-" * 30)

    elif choice == "3":
        search_id = input("Nhập id nhân viên cần tìm (vd: emp-002): ").strip().upper()

        found = False
        for emp in data_list:
            if emp[0] == search_id:
                phone = emp[2]

                is_text_phone = any(char.isalpha() for char in emp[2])

                if is_text_phone:
                    phone_number = "Invalid Format"
                else:
                    phone_number = "******" + phone[6:]

                print(f"  - Mã ID:       {emp[0]}")
                print(f"  - Họ tên:      {emp[1]}")
                print(f"  - Số ĐT:       {phone_number}")
                print(f"  - Phòng ban:   {emp[3]}")
                print("-" * 30)
                break

    elif choice == "4":
        print("Thoát chương trình")
        break
    else:
        print("Nhập sai vui lòng nhập lại")
