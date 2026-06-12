"""
utils/helpers.py

Hàm phụ trợ cho hệ thống quản lý đội hình Rikkei Esports.
"""

from typing import Dict


def calculate_actual_pay(player: Dict) -> float:
    """
    Tính lương thực nhận của một tuyển thủ theo trạng thái.

    - Nếu status == "Active" -> nhận 100% salary.
    - Nếu status == "Benched" -> nhận 50% salary.
    - Nếu salary missing hoặc không hợp lệ -> raise ValueError.

    Args:
        player (Dict): dictionary chứa thông tin tuyển thủ.

    Returns:
        float: số tiền thực nhận.

    Raises:
        ValueError: nếu salary không tồn tại hoặc không phải số dương.
    """
    if player is None:
        raise ValueError("Player data is None")

    status = player.get("status", "Unknown")
    if "salary" not in player:
        raise ValueError("Missing salary for player")

    try:
        salary = float(player["salary"])
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid salary value") from exc

    if salary < 0:
        raise ValueError("Salary must be non-negative")

    if status == "Benched":
        return salary * 0.5
    # Treat any other status (including "Active") as full pay
    return salary


def determine_status_display(name: str, status: str) -> str:
    """
    Trả về tên hiển thị kèm [DỰ BỊ] nếu status == 'Benched'.
    """
    if status == "Benched":
        return f"{name} [DỰ BỊ]"
    return name
