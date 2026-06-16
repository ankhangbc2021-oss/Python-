import math


def show_flight_schedule(flight_list):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for idx, flight in enumerate(flight_list, start=1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(
            f"{idx}. Mã: {flight['flight_id']} | Khởi hành: {flight['depart_time']} | "
            f"Số khách: {flight['passengers']} | Dự phòng: {water_boxes} thùng nước."
        )
