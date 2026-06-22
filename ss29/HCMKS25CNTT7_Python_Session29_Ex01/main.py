"""Mini"""

from abc import ABC, abstractmethod


# Lớp cha ban đầu
class BaseVehicle(ABC):
    """ """

    def __init__(self, plate):
        self.__plate = plate
        self.__odometer = 0

    @property
    def odometer(self):
        """Hiển thị"""
        return self.__odometer

    @property
    def plate(self):
        """Hiển thị"""
        return self.__plate

    @abstractmethod
    def calculate_efficiency(self):
        """Tính hiệu suất tiêu thụ năng lượng"""

    def drive(self, distance):
        """nhận km"""
        if distance > 0:
            self.__odometer += distance
        else:
            print("Số km không đủ")

    def __lt__(self, other):
        """So sánh other có lớn hơn"""
        return self.__odometer < other

    @staticmethod
    def validate_license_plate(plate):
        """Kiểm tra biển số"""
        return len(plate) == 9 and plate.startswith("29")


class AutonomousFeature:
    """Lớp hỗ trợ"""

    def calculate_efficiency(self):
        """Hệ thống tự hành tiêu tốn năng lượng"""
        return 95


class ElectricBus(BaseVehicle):
    """Kết thừa base"""

    def calculate_efficiency(self):
        resule = 100 - (self.odometer * 0.005)
        return max(50, resule)


class RoboBus(ElectricBus, AutonomousFeature):
    """Đa kết thừa"""

    def calculate_efficiency(self):
        eff_bus = ElectricBus.calculate_efficiency(self)
        eff_auto = AutonomousFeature.calculate_efficiency(self)
        return (eff_bus + eff_auto) / 2


def display_menu():
    """Hiển thị menu"""
    print("""
=== SMART TRANSIT MENU ===
1. Khởi tạo và đăng ký xe lai RoboBus mới
2. Giả lặp vận hành và Kiểm tra hiệu xuất
3. Thoát""")
    return input("Chọn chức năng (1-3): ").strip()


def main():
    """Thực thi"""
    current_vehicle = None
    while True:
        choice = display_menu()
        match (choice):
            case "1":
                # Chức năng 1:
                print("--- KHỞI TẠO XE LAI ROBOBUS ---")
                plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ").strip()
                if BaseVehicle.validate_license_plate(plate):
                    current_vehicle = RoboBus(plate)
                    print("[Thành công]: Khởi tạo phương tiện Robobus thành công!")
                    print(
                        "[MRO Architecture]: RoboBus -> ElectriBus -> "
                        + "BaseVehicle -> AutonomousFeature -> object"
                    )
                else:
                    print("[Lỗi]: Biển số xe ko hợp lệ")
            case "2":
                # Chức năng 2:
                if not current_vehicle:
                    print("Lỗi: Chưa có xe được khởi tạo.")
                    continue
                try:
                    km = float(input("Nhập số km di chuyển mới phát sinh: "))
                    current_vehicle.drive(km)
                    print("[Thành công]: Cập nhật lộ trình xe chạy thành công!")
                    print(
                        f"Tổng quãng đường tích lũy (Odometer): {current_vehicle.odometer} km"
                    )
                    print(
                        "Hiệu suất tiêu thụ năng lượng tích hợp: "
                        + f"{current_vehicle.calculate_efficiency():.1f}%"
                    )
                except ValueError:
                    print("Lỗi: Vui lòng nhập số hợp lệ.")

            case _:
                # Lựa chọn không đúng:
                print("Vui lòng chọn 1-3")
        # end match


if __name__ == "__main__":
    main()
