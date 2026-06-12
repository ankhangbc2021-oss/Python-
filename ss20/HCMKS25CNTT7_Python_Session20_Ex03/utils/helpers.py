"""
utils/helpers.py

Hàm phụ trợ cho hệ thống quản lý giải đấu.
"""

from typing import Dict


def determine_winner(match: Dict) -> str:
    """
    Xác định đội thắng trong một trận đấu.

    Logic:
    - Nếu status == "Pending" -> "Not Started"
    - Nếu score_a > score_b -> team_a
    - Nếu score_b > score_a -> team_b
    - Nếu bằng nhau -> "Draw"

    Args:
        match: dict chứa keys: team_a, team_b, score_a, score_b, status

    Returns:
        str: Tên đội thắng, "Draw" nếu hòa, hoặc "Not Started" nếu Pending.
    """
    try:
        status = match.get("status", "Pending")
        if status == "Pending":
            return "Not Started"

        score_a = int(match.get("score_a", 0))
        score_b = int(match.get("score_b", 0))

        if score_a > score_b:
            return match.get("team_a", "Unknown")
        if score_b > score_a:
            return match.get("team_b", "Unknown")
        return "Draw"
    except KeyError:
        # Nếu thiếu key, trả về "Unknown" và caller có thể log nếu cần
        return "Unknown"
    except (TypeError, ValueError):
        # Nếu giá trị score không thể chuyển thành int
        return "Unknown"
