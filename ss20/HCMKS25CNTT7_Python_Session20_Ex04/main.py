"""
main.py

Ứng dụng CLI quản lý đội hình Rikkei Esports.
"""

import logging
import os
import traceback
from typing import Dict, List

from utils.helpers import calculate_actual_pay, determine_status_display

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "roster_app.log")


def setup_logging() -> None:
    """
    Thiết lập logging: tạo thư mục logs nếu cần và cấu hình file handler.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Tránh thêm handler nhiều lần khi import
    if logger.handlers:
        return

    formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


# Dữ liệu mẫu
roster: List[Dict] = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active",
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active",
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched",
    },
]


def _normalize_id(raw_id: str) -> str:
    """
    Chuẩn hóa mã ID: strip và uppercase.
    """
    if raw_id is None:
        return ""
    return raw_id.strip().upper()


def display_roster(roster_list: List[Dict]) -> None:
    """
    Hiển thị danh sách tuyển thủ dạng bảng.
    Ghi log INFO: "Coach viewed the team roster."
    """
    if not roster_list:
        print("Đội hình hiện đang trống.")
        logging.info("Coach viewed the team roster.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print("ID       | Tên tuyển thủ        | Vị trí          | Lương        | Trạng thái")
    print("-" * 80)
    for player in roster_list:
        try:
            pid = player.get("player_id", "Unknown")
            name = player.get("name", "Unknown")
            role = player.get("role", "Unknown")
            salary = player.get("salary", 0.0)
            status = player.get("status", "Unknown")
            display_name = determine_status_display(name, status)
            print(f"{pid:<9}| {display_name:<20}| {role:<15}| {salary:>12,.1f} | {status}")
        except Exception:
            logging.error("Error displaying player: %s", traceback.format_exc())
            print("Lỗi khi hiển thị một tuyển thủ.")
    logging.info("Coach viewed the team roster.")


def _read_positive_float(prompt: str) -> float:
    """
    Đọc một số thực dương từ input, lặp lại cho đến khi hợp lệ.
    Ghi log WARNING khi nhập sai, ERROR khi có ngoại lệ bất ngờ.
    """
    while True:
        try:
            raw = input(prompt)
        except Exception:
            logging.error("Unexpected input error:\n%s", traceback.format_exc())
            print("Đã xảy ra lỗi khi nhập. Vui lòng thử lại.")
            continue

        try:
            value = float(raw)
        except ValueError:
            logging.warning("Failed to parse salary input: %s", raw)
            print("Lương phải là số. Vui lòng nhập lại.")
            continue

        if value <= 0:
            logging.warning("Non-positive salary input: %s", raw)
            print("Lương phải là số dương. Vui lòng nhập lại.")
            continue

        return value


def sign_player(roster_list: List[Dict]) -> None:
    """
    Chiêu mộ tuyển thủ mới.
    Kiểm tra mã trùng, mã rỗng, tên/vị trí rỗng, và lương hợp lệ.
    """
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    try:
        raw_id = input("Nhập mã tuyển thủ: ")
    except Exception:
        logging.error("Unexpected input error:\n%s", traceback.format_exc())
        print("Đã xảy ra lỗi khi đọc mã tuyển thủ.")
        return

    player_id = _normalize_id(raw_id)
    if not player_id:
        print("Mã tuyển thủ không được để trống.")
        logging.warning("Failed to sign player - Empty player ID")
        return

    if any(p.get("player_id") == player_id for p in roster_list):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning("Failed to sign player - Duplicate player ID %s", player_id)
        return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()
    if not name or not role:
        print("Tên và vị trí không được để trống.")
        logging.warning("Failed to sign player - Empty name or role")
        return

    # đọc lương hợp lệ
    salary = _read_positive_float("Nhập mức lương hàng tháng: ")

    new_player = {
        "player_id": player_id,
        "name": name.title(),
        "role": role.title(),
        "salary": salary,
        "status": "Active",
    }
    roster_list.append(new_player)
    print(f"Thành công: Đã chiêu mộ tuyển thủ {new_player['name']}.")
    logging.info("Signed new player %s with salary %s", new_player["name"], salary)


def update_player_status(roster_list: List[Dict]) -> None:
    """
    Cập nhật lương hoặc trạng thái thi đấu cho một tuyển thủ.
    Bắt lỗi khi mã không tồn tại, lặp lại khi nhập lương không hợp lệ.
    """
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    raw_id = input("Nhập mã tuyển thủ cần cập nhật: ")
    player_id = _normalize_id(raw_id)
    player = next((p for p in roster_list if p.get("player_id") == player_id), None)

    if not player:
        print(f"Không tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning("Failed to update player - Player ID %s not found", player_id)
        return

    name = player.get("name", "Unknown")
    role = player.get("role", "Unknown")
    salary = player.get("salary", 0.0)
    status = player.get("status", "Unknown")

    print(f"\nTuyển thủ: {name}")
    print(f"Vị trí: {role}")
    print(f"Lương hiện tại: {salary:,.1f}")
    print(f"Trạng thái hiện tại: {status}\n")

    print("Bạn muốn cập nhật:")
    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")
    choice = input("Chọn chức năng cập nhật (1-2): ").strip()

    if choice == "1":
        new_salary = _read_positive_float("Nhập mức lương mới: ")
        old_salary = player.get("salary", 0.0)
        player["salary"] = new_salary
        print(f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
        logging.info("Updated player %s salary from %s to %s", player_id, old_salary, new_salary)
    elif choice == "2":
        print("\nChọn trạng thái mới:")
        print("1. Active")
        print("2. Benched")
        st_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
        if st_choice == "1":
            new_status = "Active"
        elif st_choice == "2":
            new_status = "Benched"
        else:
            print("Lựa chọn trạng thái không hợp lệ.")
            logging.warning("Invalid status choice when updating player %s", player_id)
            return
        old_status = player.get("status", "Unknown")
        player["status"] = new_status
        print(f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
        logging.info("Updated player %s status from %s to %s", player_id, old_status, new_status)
    else:
        print("Lựa chọn không hợp lệ.")
        logging.warning("Invalid update choice selected for player %s", player_id)


def generate_payroll_report(roster_list: List[Dict]) -> None:
    """
    Sinh báo cáo quỹ lương hàng tháng.
    - Active: 100% salary
    - Benched: 50% salary
    Nếu thiếu salary key cho bất kỳ tuyển thủ nào -> log ERROR và in thông báo lỗi.
    """
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        logging.info("Generated monthly payroll report. Total: 0.0")
        return

    total = 0.0
    header_printed = False
    try:
        for player in roster_list:
            if "salary" not in player:
                logging.error("Missing key while generating payroll report: 'salary'")
                print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
                print("-" * 80)
                print("Tổng quỹ lương hàng tháng: 0.0")
                return

        print("ID       | Tên tuyển thủ   | Trạng thái | Lương gốc    | Lương thực nhận")
        print("-" * 80)
        for player in roster_list:
            pid = player.get("player_id", "Unknown")
            name = player.get("name", "Unknown")
            status = player.get("status", "Unknown")
            salary = float(player.get("salary", 0.0))
            actual = calculate_actual_pay(player)
            total += actual
            print(f"{pid:<9}| {name:<15}| {status:<10}| {salary:>12,.1f} | {actual:>12,.1f}")
        print("-" * 80)
        print(f"Tổng quỹ lương hàng tháng: {total:,.1f}")
        logging.info("Generated monthly payroll report. Total: %s", total)
    except Exception:
        logging.error("Unexpected error generating payroll report:\n%s", traceback.format_exc())
        print("Đã xảy ra lỗi khi sinh báo cáo quỹ lương.")


def main() -> None:
    """
    Vòng lặp menu chính.
    """
    setup_logging()
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        choice = input("Chọn chức năng (1-5): ").strip()
        if choice == "1":
            display_roster(roster)
        elif choice == "2":
            sign_player(roster)
        elif choice == "3":
            update_player_status(roster)
        elif choice == "4":
            generate_payroll_report(roster)
        elif choice == "5":
            logging.info("System closed by user.")
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5.")
            logging.warning("Invalid menu choice selected")


if __name__ == "__main__":
    main()
