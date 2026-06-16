from core.logistics import show_flight_schedule
from core.manager import add_new_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_folder

flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time": "2026-06-15 08:00:00",
        "duration_min": 120,
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time": "2026-06-15 13:30:00",
        "duration_min": 45,
    },
]

while True:
    print("===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
    print("1. Hiển thị lịch trình và Thống kê hậu cần")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính thời gian hạ cánh dự kiến (ETA)")
    print("4. Khởi tạo thư mục lưu trữ log hệ thống")
    print("5. Thoát chương trình")
    print("==================================================")

    try:
        choice = int(input("Nhập lựa chọn của bạn: "))
    except ValueError:
        print(">> Lỗi: Vui lòng nhập số từ 1-5!")
        continue

    if choice == 1:
        show_flight_schedule(flights)
    elif choice == 2:
        add_new_flight(flights)
    elif choice == 3:
        calculate_eta(flights)
    elif choice == 4:
        create_folder()
    elif choice == 5:
        print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
        break
    else:
        print(">> Lỗi: Vui lòng nhập số từ 1-5!")
