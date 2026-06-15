import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

devices = [
    {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
    {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
]

def show_devices(devices):
    if not devices:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return
    print("__ DANH SÁCH THIẾT BỊ GIÁM SÁT __")
    print(f"{'MÃ TB':<5} | {'VỊ TRÍ':<20} | {'CHỈ SỐ CŨ':<10} | {'CHỈ SỐ MỚI':<10} | {'TRẠNG THÁI':<10}")
    print("-" * 60)
    for d in devices:
        print(f"{d['id']:<5} | {d['location']:<20} | {d['old_index']:<10} | {d['new_index']:<10} | {d['status']:<10}")

def update_indices(devices):
    device_id = input("Nhập mã thiết bị: ")
    for d in devices:
        if d['id'] == device_id:
            try:
                old_index = int(input("Nhập chỉ số cũ: "))
                new_index = int(input("Nhập chỉ số mới: "))
                if new_index < old_index:
                    print("[Lỗi] (ERR-E02): Chỉ số mới không được nhỏ hơn chỉ số cũ!")
                    return
                d['old_index'] = old_index
                d['new_index'] = new_index
                print(f"[Thành công]: Thiết bị {device_id} đã được cập nhật số liệu mới")
                return
            except ValueError:
                print("[Lỗi] Nhập sai kiểu dữ liệu!")
                return
    print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong hệ thống")

def activate_warning(devices):
    device_id = input("Nhập mã thiết bị cần duyệt: ")
    for d in devices:
        if d['id'] == device_id:
            consumption = d['new_index'] - d['old_index']
            if d['status'] == "Overload":
                print("[Lỗi] (ERR-E04): Thiết bị này đã ở trạng thái OVERLOAD từ trước!")
                return
            if consumption > 5000:
                d['status'] = "Overload"
                logging.warning(f"Thiết bị {device_id} vượt ngưỡng an toàn, chuyển sang OVERLOAD!")
                print(f"[Thành công]: Thiết bị {device_id} đã được kích hoạt trạng thái OVERLOAD!")
                return
            else:
                print("Thiết bị chưa vượt ngưỡng an toàn.")
                return
    print("[Lỗi] (ERR-E01): Không tìm thấy mã thiết bị!")

def calculate_energy_financials(devices):
    total_consumption = sum(d['new_index'] - d['old_index'] for d in devices)
    base_price = 3000
    discount = 0.03 if total_consumption >= 50000 else 0
    total_cost = total_consumption * base_price * (1 - discount)
    return total_consumption, discount * 100, total_cost

def main():
    while True:
        print("\nSMART ENERGY MONITOR – PHÒNG CƠ ĐIỆN")
        print("1. Xem danh sách thiết bị giám sát")
        print("2. Cập nhật chỉ số điện tiêu thụ (Check-in)")
        print("3. Kích hoạt trạng thái cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí năng lượng")
        print("5. Thoát chương trình")

        try:
            choice = int(input("Mời chọn chức năng (1–5): "))
        except ValueError:
            print("[Lỗi] Vui lòng nhập số từ 1–5!")
            continue

        match choice:
            case 1:
                show_devices(devices)
            case 2:
                update_indices(devices)
            case 3:
                activate_warning(devices)
            case 4:
                total, discount, cost = calculate_energy_financials(devices)
                print("── BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG ──")
                print(f"+ Tổng lượng điện tiêu thụ thực tế: {total} kWh")
                print(f"+ Tỷ lệ chiết khấu áp dụng từ nhà nước: {discount}%")
                print(f"+ Tổng chi phí năng lượng phải trả sau chiết khấu: {cost:,} VND")
            case 5:
                print("Cảm ơn bạn đã sử dụng phần mềm Smart Energy Monitor!")
                break
            case _:
                print("[Lỗi] Vui lòng chọn số từ 1–5!")

if __name__ == "__main__":
    main()
