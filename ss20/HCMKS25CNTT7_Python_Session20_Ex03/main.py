"""
main.py

Hệ thống quản lý giải đấu Rikkei Esports.
Chứa menu chính và các chức năng: hiển thị, thêm trận, cập nhật tỷ số, báo cáo, thoát.
"""

import json
import logging
import os
import traceback
from typing import Dict, List

from utils.helpers import determine_winner

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "tournament_app.log")


def setup_logging() -> None:
    """
    Thiết lập logging cho ứng dụng.
    Tạo thư mục logs nếu chưa tồn tại và cấu hình format theo yêu cầu.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Nếu đã có handler, tránh thêm handler trùng lặp khi import nhiều lần
    if logger.handlers:
        return

    formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


# Dữ liệu mẫu
matches: List[Dict] = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed",
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending",
    },
]


def display_matches(match_list: List[Dict]) -> None:
    """
    Hiển thị danh sách trận đấu với định dạng cột rõ ràng.
    Ghi log INFO khi người dùng xem danh sách.
    Args:
        match_list: Danh sách các trận (list of dict).
    """
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        logging.info("User viewed the match list.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print("Mã trận   | Đội A           | Đội B           | Tỷ số   | Trạng thái")
    print("-" * 70)
    for match in match_list:
        try:
            match_id = match["match_id"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            score_a = match.get("score_a", 0)
            score_b = match.get("score_b", 0)
            status = match.get("status", "Pending")
            print(
                f"{match_id:<10}| {team_a:<15}| {team_b:<15}| "
                f"{score_a}-{score_b:<5}| {status}"
            )
        except KeyError as exc:
            logging.error("Missing key in match data: %s", exc)
    logging.info("User viewed the match list.")


def add_match(match_list: List[Dict]) -> None:
    """
    Thêm trận đấu mới.
    Kiểm tra mã trùng, mã rỗng, tên đội rỗng. Ghi log tương ứng.
    Args:
        match_list: Danh sách các trận (list of dict).
    """
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    try:
        match_id = input("Nhập mã trận đấu: ").strip()
    except Exception:
        logging.error("Unexpected error reading match ID:\n%s", traceback.format_exc())
        print("Đã xảy ra lỗi khi đọc mã trận. Vui lòng thử lại.")
        return

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    if any(m.get("match_id") == match_id for m in match_list):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning("Match ID %s already exists.", match_id)
        return

    try:
        team_a = input("Nhập tên Đội A: ").strip()
        team_b = input("Nhập tên Đội B: ").strip()
    except Exception:
        logging.error("Unexpected error reading team names:\n%s", traceback.format_exc())
        print("Đã xảy ra lỗi khi đọc tên đội. Vui lòng thử lại.")
        return

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending",
    }
    match_list.append(new_match)
    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info("Match %s added successfully", match_id)


def _read_non_negative_int(prompt: str) -> int:
    """
    Đọc một số nguyên không âm từ input, lặp lại cho đến khi hợp lệ.
    Ghi log ERROR khi ValueError xảy ra, ghi log ERROR khi số âm.
    Args:
        prompt: Chuỗi hiển thị cho input.
    Returns:
        int: Giá trị số nguyên >= 0.
    """
    while True:
        try:
            raw = input(prompt)
        except Exception:
            logging.error("Unexpected input error:\n%s", traceback.format_exc())
            print("Đã xảy ra lỗi khi nhập. Vui lòng thử lại.")
            continue

        try:
            value = int(raw)
        except ValueError as exc:
            logging.error("Invalid score input. Error: %s", exc)
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            continue

        if value < 0:
            logging.error("Negative score input detected: %d", value)
            print("Điểm số phải lớn hơn hoặc bằng 0.")
            continue

        return value


def update_score(match_list: List[Dict]) -> None:
    """
    Cập nhật tỷ số trận đấu.
    Bắt lỗi khi mã trận không tồn tại, bắt ValueError cho điểm, xử lý 0-0 theo yêu cầu.
    Args:
        match_list: Danh sách các trận (list of dict).
    """
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    try:
        match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    except Exception:
        logging.error("Unexpected error reading match ID:\n%s", traceback.format_exc())
        print("Đã xảy ra lỗi khi đọc mã trận. Vui lòng thử lại.")
        return

    match = next((m for m in match_list if m.get("match_id") == match_id), None)
    if not match:
        print(f"Không tìm thấy trận đấu mang mã {match_id}.")
        logging.warning("User tried to update non-existing match %s", match_id)
        return

    try:
        team_a = match.get("team_a", "Unknown")
        team_b = match.get("team_b", "Unknown")
        status = match.get("status", "Pending")
        print(f"Trận đấu: {team_a} vs {team_b} ({status})")
    except KeyError:
        logging.error("Missing key when showing match info for %s", match_id)
        print("Dữ liệu trận đấu không hợp lệ.")
        return

    score_a = _read_non_negative_int("Nhập điểm Đội A: ")
    score_b = _read_non_negative_int("Nhập điểm Đội B: ")

    match["score_a"] = score_a
    match["score_b"] = score_b

    # Chú ý bẫy logic: chỉ set Completed nếu ít nhất 1 đội > 0 hoặc trọng tài xác nhận
    if score_a == 0 and score_b == 0:
        while True:
            try:
                confirm = input(
                    "Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): "
                ).strip().lower()
            except Exception:
                logging.error("Unexpected input error during 0-0 confirmation:\n%s", traceback.format_exc())
                print("Đã xảy ra lỗi khi nhập. Vui lòng thử lại.")
                continue

            if confirm in ("y", "n"):
                match["status"] = "Completed" if confirm == "y" else "Pending"
                break
            else:
                print("Vui lòng nhập 'y' hoặc 'n'.")

    else:
        match["status"] = "Completed"

    print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info("Match %s score updated successfully", match_id)


def generate_report(match_list: List[Dict]) -> None:
    """
    Sinh báo cáo thống kê: liệt kê các trận đã Completed và tên đội thắng.
    Gọi helper determine_winner.
    Args:
        match_list: Danh sách các trận (list of dict).
    """
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_matches = [m for m in match_list if m.get("status") == "Completed"]

    if not completed_matches:
        print("Chưa có trận đấu nào hoàn thành.")
        print("Tổng số trận đã hoàn thành: 0")
        logging.info("User generated tournament report.")
        return

    for match in completed_matches:
        try:
            winner = determine_winner(match)
            print(
                f"{match.get('match_id')}: {match.get('team_a')} "
                f"{match.get('score_a')}-{match.get('score_b')} {match.get('team_b')} | Kết quả: {winner}"
            )
        except KeyError as exc:
            logging.error("Missing key when generating report: %s", exc)
    print(f"Tổng số trận đã hoàn thành: {len(completed_matches)}")
    logging.info("User generated tournament report.")


def main() -> None:
    """
    Hàm chính chạy menu hệ thống.
    Bẫy lựa chọn ngoài 1-5 và ghi log WARNING.
    """
    setup_logging()
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        try:
            choice = input("Chọn chức năng (1-5): ").strip()
        except Exception:
            logging.error("Unexpected input error in menu:\n%s", traceback.format_exc())
            print("Đã xảy ra lỗi khi nhập. Vui lòng thử lại.")
            continue

        if choice == "1":
            display_matches(matches)
        elif choice == "2":
            add_match(matches)
        elif choice == "3":
            update_score(matches)
        elif choice == "4":
            generate_report(matches)
        elif choice == "5":
            logging.info("System closed by user.")
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5.")
            logging.warning("Invalid menu choice selected")


if __name__ == "__main__":
    main()
