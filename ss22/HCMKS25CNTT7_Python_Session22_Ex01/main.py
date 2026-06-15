"""
Ktra sáng
"""

import logging

# Cấu hình logging hệ thống (Đã sửa level sang DEBUG để hiển thị tất cả các mức log)
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_discount_rate(tier: str, quantity: int) -> float:
    """Trả về tỷ lệ chiết khấu dựa trên hạng thành viên và số lượng"""
    logger.debug(f"Đang tính toán chiết khấu cho hạng {tier} với số lượng {quantity}")

    if quantity <= 0:
        # Đã sửa lỗi Runtime: Ném ra ngoại lệ ValueError để chặn dữ liệu đầu vào sai
        raise ValueError("Quantity must be positive")

    # Xác định tỷ lệ chiết khấu cơ bản
    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        rate = 0.0

    # Thưởng thêm nếu mua số lượng lớn (từ 50 sản phẩm trở lên)
    if quantity >= 50:
        rate += 0.05  # Đã sửa lỗi logic: sử dụng cộng dồn thay vì gán giá trị

    return rate


def calculate_agency_total(price: float, quantity: int, tier: str) -> float:
    """Tính tổng tiền sau chiết khấu cho đại lý"""
    if price < 0:
        raise ValueError("Đơn giá không được âm")

    # Hàm get_discount_rate giờ đây có thể ném ValueError nếu quantity <= 0
    rate = get_discount_rate(tier, quantity)

    final_price = price * (1 - rate) * quantity

    logger.info(f"Kết quả: Tổng tiền = {final_price}")
    return final_price


# Khúc code chạy thử của Intern
if __name__ == "__main__":
    # Case kiểm tra lỗi logic biên (Sẽ trả về 4250.0 sau khi sửa)
    calculate_agency_total(100, 50, "gold")

    # Case kiểm tra lỗi dữ liệu đầu vào
    # (Sẽ ném ra ValueError, cần try/except để chương trình không dừng)
    try:
        calculate_agency_total(100, -5, "silver")
    except ValueError as e:
        logger.error(f"Lỗi đầu vào đã được chặn: {e}")
