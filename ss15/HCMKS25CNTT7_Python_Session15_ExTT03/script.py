# Global variables
available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

def calculate_ticket_cost(quantity: int, seat_class: int) -> float:
    """
    Tính toán tổng chi phí đặt vé.
    Parameters:
        quantity (int): số lượng vé
        seat_class (int): hạng vé (1: Economy, 2: Business)
    Returns:
        float: tổng chi phí sau khi cộng phí dịch vụ
    """
    if seat_class == 1:
        price_per_ticket = BASE_PRICE
    elif seat_class == 2:
        price_per_ticket = BASE_PRICE * 1.5
    else:
        return -1.0  # báo lỗi hạng vé không hợp lệ

    subtotal = price_per_ticket * quantity
    service_fee = subtotal * 0.05
    total_cost = subtotal + service_fee

    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {'Economy' if seat_class == 1 else 'Business'}")
    print(f"Tạm tính: ${subtotal}")
    print(f"Phí dịch vụ (5%): ${service_fee}")
    print(f"Tổng thanh toán: ${total_cost}")
    return total_cost

def process_booking(quantity: int, total_cost: float, seat_class: int):
    """
    Xử lý logic đặt vé.
    Parameters:
        quantity (int): số lượng vé
        total_cost (float): tổng chi phí đã tính
        seat_class (int): hạng vé
    """
    global available_seats, flight_revenue
    if quantity <= 0:
        print("Số lượng vé không hợp lệ.")
        return
    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return

    available_seats -= quantity
    flight_revenue += total_cost
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

def process_refund(quantity: int) -> float:
    """
    Xử lý hoàn vé.
    Parameters:
        quantity (int): số lượng vé muốn hủy
    Returns:
        float: số tiền hoàn lại
    """
    global available_seats, flight_revenue
    if quantity <= 0:
        print("Số lượng vé không hợp lệ.")
        return 0.0
    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0.0

    refund_amount = BASE_PRICE * 0.8 * quantity
    available_seats += quantity
    flight_revenue -= refund_amount
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund_amount} (80% giá cơ bản).")
    print(f"Ghế trống hiện tại: {available_seats}")
    return refund_amount

def display_flight_status():
    """
    In ra tình trạng chuyến bay hiện tại.
    Docstring:
        Hiển thị báo cáo gồm sức chứa tối đa, số ghế đã đặt, số ghế trống, tổng doanh thu.
    """
    global available_seats, flight_revenue
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {50 - available_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")

def main():
    """
    Vòng lặp menu chính của hệ thống SkyBooking.
    """
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            print("--- ĐẶT VÉ MÁY BAY ---")
            qty_str = input("Nhập số lượng vé: ")
            if not qty_str.isdigit():
                print("Vui lòng nhập số hợp lệ.")
                continue
            quantity = int(qty_str)

            seat_class_str = input("Chọn hạng vé (1: Economy, 2: Business): ")
            if not seat_class_str.isdigit():
                print("Vui lòng nhập số hợp lệ.")
                continue
            seat_class = int(seat_class_str)

            total_cost = calculate_ticket_cost(quantity, seat_class)
            if total_cost == -1.0:
                print("Hạng vé không hợp lệ.")
                continue
            process_booking(quantity, total_cost, seat_class)

        elif choice == "2":
            print("--- HỦY VÉ & HOÀN TIỀN ---")
            qty_str = input("Nhập số lượng vé muốn hủy: ")
            if not qty_str.isdigit():
                print("Vui lòng nhập số hợp lệ.")
                continue
            quantity = int(qty_str)
            process_refund(quantity)

        elif choice == "3":
            display_flight_status()

        elif choice == "4":
            print("Hệ thống đóng lại. Cảm ơn đã sử dụng dịch vụ!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình
if __name__ == "__main__":
    main()
