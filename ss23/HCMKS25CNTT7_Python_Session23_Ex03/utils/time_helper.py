import datetime

def calculate_eta(flight_list):
    print("----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    flight = next((f for f in flight_list if f["flight_id"] == flight_id), None)

    if not flight:
        print(">> Không tìm thấy chuyến bay!")
        return

    depart_time = datetime.datetime.strptime(flight["depart_time"], "%Y-%m-%d %H:%M:%S")
    eta = depart_time + datetime.timedelta(minutes=flight["duration_min"])
    print(f"-> Chuyến bay {flight_id} cất cánh lúc: {flight['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
