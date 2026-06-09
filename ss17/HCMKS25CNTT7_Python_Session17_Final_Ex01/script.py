"""
BTTH 1
"""

# Hệ thống khởi tạo một danh sách toàn cục chứa các log thô (Raw Logs)
processed_logs = []
raw_logs = []


def display_menu():
    """Hiện menu"""
    print(
        "\n============= SECURITY LOG ANALYZER =============\n"
        "1. Nhập và làm sạch dữ liệu Log thô\n"
        "2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)\n"
        "3. Mã hóa địa chỉ IP (Masking)\n"
        "4. Đóng hệ thống\n"
        "=================================================\n"
    )


def add_data():
    """Nạp dữ liệu

    Args:
        string (str): Nhập dữ liệu

    Returns:
        list: _description_
    """
    # Những ký tự cần xóa
    chars_to_remove = "!@#$"

    in_string = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ").strip()

    table = str.maketrans("", "", chars_to_remove)
    string = in_string.translate(table)

    list_raw_logs = [log.strip() for log in string.split(";") if log.strip()]

    raw_logs.extend(list_raw_logs)
    print(f"Đã làm sạch và lưu {len(list_raw_logs)} dòng vào hệ thống")


def filter_log(list: list) -> str:
    """Lọc và cảnh báo

    Args:
        list (list): Nhập list

    Returns:
        str: Cảnh báo
    """
    if not list:
        print("Không có dữ liệu. Vui lòng chạy 1 để có")
        return

    filter_list = [
        log for log in list if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    print("\n--- LỌC CẢNH BÁO ---")
    if filter_list:
        processed_logs.extend(filter_list)
        print(f"Tìm thấy {len(filter_list)} cảnh báo nguy hiểm:")
        for log in filter_list:
            print(f"- {log}")
    else:
        print("Không tìm thấy cảnh báo nào")


def mask_ips(list: list) -> str:
    """Mã hóa ip

    Args:
        list (list): danh sách cần mã hóa

    Returns:
        str: in ra báo cáo
    """
    if not list:
        print("Không có dữ liệu. Vui lòng chạy 1-2 để có")
        return

    masked_log = []

    for log in list:
        words = log.split()
        new_words = []

        for word in words:
            if "." in word:
                parts = word.split(".")
                if len(parts) == 4:
                    masked_ip = f"{parts[0]}.{parts[1]}.*.*"
                    new_words.append(masked_ip)
                else:
                    new_words.append(word)
            else:
                new_words.append(word)
        masked_log.append(" ".join(new_words))

    print("\n--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")
    for i, log in enumerate(masked_log, start=1):
        print(f"{i}. {log}")


def main():
    """Chạy chương trình"""
    while True:
        display_menu()

        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                add_data()
            case "2":
                filter_log(raw_logs)
            case "3":
                mask_ips(processed_logs)
            case "4":
                print("Đã thoát")
                break
            case _:
                print("Vui lòng nhập 1-4")


if __name__ == "__main__":
    main()
