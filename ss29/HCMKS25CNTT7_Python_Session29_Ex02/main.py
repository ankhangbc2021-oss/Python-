import logging
from abc import ABC, abstractmethod

# Cấu hình module logging doanh nghiệp để ghi vết hệ thống thay thế cho print thô
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# =====================================================================
# 1. CÁC LỚP CỔNG NGOẠI VI TRUNG GIAN (DUCK TYPING GATEWAYS)
# =====================================================================


class MQTTEngineGateway:
    def process_stream(self, device_object):
        print("[Hệ thống MQTT Engine]: Đang khởi tạo băng thông kết nối dữ liệu IoT...")
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        print(
            f"Dữ liệu của thiết bị {device_object.device_code} đã được đóng gói và xuất chuỗi luồng thành công.\n"
        )


class ERPReportGateway:
    def process_stream(self, device_object):
        print(
            "[Hệ thống ERP Gateway]: Đang kết nối phân hệ quản trị tài sản doanh nghiệp..."
        )
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        print(
            f"Chỉ số vận hành của thiết bị {device_object.device_code} đã được đồng bộ hóa vào báo cáo ERP.\n"
        )


# Hàm toàn cục lỏng lẻo (Loosely Coupled) áp dụng Duck Typing
def export_telemetry_data(data_gateway, device_object):
    # ERR-IOT-05: Kiểm tra cấu hình cổng ngoại vi có tương thích phương thức hay không
    if not hasattr(data_gateway, "process_stream") or not callable(
        getattr(data_gateway, "process_stream")
    ):
        raise AttributeError(
            "[Lỗi] (ERR-IOT-05): Xung đột kiến trúc! Không thể xuất dữ liệu do cấu hình cổng ngoại vi không tương thích."
        )
    data_gateway.process_stream(device_object)


# =====================================================================
# 2. KIẾN TRÚC LỚP ĐỐI TƯỢNG THIẾT BỊ IOT (IOT DEVICE CLASSES)
# =====================================================================


class BaseDevice(ABC):
    """
    Abstract Base Class (ABC) - Thiết lập khung nguyên mẫu ép buộc cho toàn bộ thiết bị.
    """

    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, name):
        self._device_code = device_code
        self.name = name  # Gọi qua setter để chuẩn hóa tên
        self.__operating_hours = 0.0  # Biến private đóng gói nghiêm ngặt số giờ chạy

    # Encapsulation bằng @property: Chỉ cho phép đọc, chặn sửa đổi tùy tiện từ bên ngoài
    @property
    def operating_hours(self):
        return self.__operating_hours

    @property
    def device_code(self):
        return self._device_code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Chuẩn hóa chuỗi: In hoa, loại bỏ khoảng trắng thừa ở hai đầu và giữa các từ
        self._name = " ".join(value.strip().split()).upper()

    def add_operating_hours(self, hours):
        """Phương thức nội bộ để tích lũy giờ chạy sau khi đã thẩm định dữ liệu lớn hơn 0"""
        if hours <= 0:
            raise ValueError(
                "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
            )
        self.__operating_hours += hours

    @abstractmethod
    def track_performance(self, *args, **kwargs):
        """Phương thức trừu tượng tính toán hiệu suất thiết bị."""
        pass

    @abstractmethod
    def run_diagnostic(self):
        """Phương thức trừu tượng thực thi chẩn đoán lỗi."""
        pass

    # @staticmethod: Hàm tĩnh độc lập để kiểm tra tính hợp lệ của mã thiết bị đầu vào
    @staticmethod
    def validate_device_code(device_code):
        return len(device_code) == 10 and device_code[0].isalpha()

    # @classmethod: Thay đổi thuộc tính ở cấp độ lớp cho toàn bộ thực thể
    @classmethod
    def update_maintenance_cost(cls, new_cost):
        if new_cost < 0:
            raise ValueError(
                "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
            )
        cls.base_maintenance_cost = new_cost

    # Operator Overloading: Nạp chồng toán tử cộng (+) gộp giờ vận hành tải
    def __add__(self, other):
        # ERR-IOT-04: Đánh bẫy nếu đối tượng so sánh/cộng gộp nằm ngoài hệ thống thiết bị
        if not isinstance(other, BaseDevice):
            raise TypeError(
                "[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống."
            )
        return self.operating_hours + other.operating_hours

    # Operator Overloading: Nạp chồng toán tử nhỏ hơn (<) so sánh mức độ hao mòn
    def __lt__(self, other):
        # ERR-IOT-04: Đánh bẫy nếu đối tượng so sánh nằm ngoài hệ thống thiết bị
        if not isinstance(other, BaseDevice):
            raise TypeError(
                "[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống."
            )
        return self.operating_hours < other.operating_hours


class ProductionRobot(BaseDevice):
    """Subclass điều phối Robot sản xuất lắp ráp"""

    def __init__(self, device_code, name):
        super().__init__(device_code, name)
        self.completed_products = 0

    def track_performance(self, new_hours, new_products):
        if new_hours <= 0 or new_products < 0:
            raise ValueError(
                "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
            )
        self.add_operating_hours(new_hours)
        self.completed_products += new_products
        # Giả lập công thức tính OEE dựa trên tỷ lệ sản phẩm trên thời gian chạy tích lũy
        oee = (self.completed_products / (self.operating_hours * 50)) * 100
        return min(oee, 100.0)

    def run_diagnostic(self):
        print("\n--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
        if self.completed_products > 10000:
            print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(
                f"Kết quả chẩn đoán: Cảnh báo bảo dưỡng: Sản lượng vượt định mức quy định! ({self.completed_products} sản phẩm)"
            )
        else:
            print("[Hệ thống ổn định]: Robot hoạt động trong giới hạn an toàn.")
        print(
            f"Định mức chi phí bảo trì hệ thống dự kiến: {self.base_maintenance_cost:,.0f} VND"
        )


class ThermalSensor(BaseDevice):
    """Subclass điều phối Cảm biến nhiệt độ phân xưởng"""

    def __init__(self, device_code, name, safety_threshold=80.0):
        super().__init__(device_code, name)
        self.current_temperature = 25.0  # Nhiệt độ mặc định phòng thí nghiệm
        self.safety_threshold = safety_threshold

    def track_performance(self, new_hours, temp_reading):
        if new_hours <= 0 or temp_reading <= 0:
            raise ValueError(
                "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
            )
        self.add_operating_hours(new_hours)
        self.current_temperature = temp_reading
        # Biên độ nhiệt độ so với ngưỡng an toàn
        variance = abs(self.safety_threshold - self.current_temperature)
        return variance

    def run_diagnostic(self):
        print("\n--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
        if self.current_temperature > self.safety_threshold:
            print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(
                f"Kết quả chẩn đoán: Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
            )
        else:
            print("[Hệ thống ổn định]: Nhiệt độ môi trường sản xuất an toàn.")
        print(
            f"Định mức chi phí bảo trì hệ thống dự kiến: {self.base_maintenance_cost:,.0f} VND"
        )


class HybridSmartActuator(ProductionRobot, ThermalSensor):
    """Multiple Inheritance Subclass xử lý thiết bị truyền động lai đặc thù"""

    def __init__(self, device_code, name):
        # Khởi tạo chuỗi kế thừa theo cấu trúc MRO quy chuẩn
        super().__init__(device_code, name)
        # Khởi tạo các thuộc tính phân hệ ThermalSensor do nhánh ProductionRobot không quản lý
        self.current_temperature = 25.0
        self.safety_threshold = 80.0

    def track_performance(self, new_hours, new_products=0, temp_reading=25.0):
        """Tích hợp đồng thời cả 2 chỉ số OEE và nhiệt độ phòng máy"""
        if new_hours <= 0 or new_products < 0 or temp_reading <= 0:
            raise ValueError(
                "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
            )

        self.add_operating_hours(new_hours)
        self.completed_products += new_products
        self.current_temperature = temp_reading

        oee = (self.completed_products / (self.operating_hours * 50)) * 100
        return min(oee, 100.0)

    def run_diagnostic(self):
        """Ghi đè phức hợp kiểm tra đồng thời cả 2 điều kiện lỗi từ Robot và Nhiệt độ"""
        print("\n--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
        triggered = False
        if self.current_temperature > self.safety_threshold:
            print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(
                f"Kết quả chẩn đoán: Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
            )
            triggered = True
        if self.completed_products > 10000:
            if not triggered:
                print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(
                f"Kết quả chẩn đoán: Cảnh báo hành trình: Robot tích lũy sản lượng quá cao! ({self.completed_products} sản phẩm)"
            )
            triggered = True

        if not triggered:
            print("[Hệ thống ổn định]: Thiết bị lai thông minh vận hành trơn tru.")
        print(
            f"Định mức chi phí bảo trì hệ thống dự kiến: {(self.base_maintenance_cost * 1.5):,.0f} VND (Hệ số lai nhân 1.5)"
        )


# =====================================================================
# 3. GIAO DIỆN ĐIỀU KHIỂN DÒNG LỆNH TRUNG TÂM (CLI MENU)
# =====================================================================


def main():
    devices_list = []
    current_device = None

    # Khởi tạo sẵn một thiết bị đối chứng nền trong nhà máy để phục vụ Chức năng 5 (Overloading)
    sample_sensor = ThermalSensor("IOT0099999", "CAM BIEN NHIET LO NUNG")
    sample_sensor.add_operating_hours(250)
    devices_list.append(sample_sensor)

    while True:
        print("\n===== RIKKEI SMART FACTORY IOT SIMULATOR =====")
        print("1. Đăng ký & Khởi tạo thiết bị IoT mới")
        print("2. Xem thông tin thiết bị & Thứ tự kế thừa (MRO)")
        print("3. Check-in giờ vận hành & Cập nhật chỉ số hiệu suất (Đa hình)")
        print("4. Thực thi quy trình tự chẩn đoán kỹ thuật (Diagnostic)")
        print("5. Cộng gộp thời gian tải & So sánh hao mòn (Operator Overloading)")
        print("6. Xuất dữ liệu vận hành ra Cổng ngoại vi (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")

        choice = input("Chọn chức năng (1-7): ").strip()

        # ERR-IOT-06: Bẫy nhập sai ngoài dải Menu điều hướng chính
        if choice not in [str(i) for i in range(1, 8)]:
            print(
                "[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7."
            )
            continue

        if choice == "1":
            print("\n--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
            print("1. Production Robot (Robot sản xuất lắp ráp)")
            print("2. Thermal Sensor (Cảm biến nhiệt độ)")
            print("3. Hybrid Smart Actuator (Thiết bị truyền động lai)")
            device_type = input("Chọn phân loại thiết bị (1-3): ").strip()

            code = input("Nhập mã thiết bị 10 ký tự: ").strip()
            # Sử dụng phương thức tĩnh tĩnh để thẩm định mã thiết bị đầu vào
            if not BaseDevice.validate_device_code(code):
                print(
                    "[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định."
                )
                continue

            name_input = input("Nhập tên thiết bị: ")

            if device_type == "1":
                current_device = ProductionRobot(code, name_input)
                print("[Thành công]: Đăng ký Robot sản xuất thành công!")
            elif device_type == "2":
                current_device = ThermalSensor(code, name_input)
                print("[Thành công]: Đăng ký Cảm biến nhiệt độ thành công!")
            elif device_type == "3":
                current_device = HybridSmartActuator(code, name_input)
                print("[Thành công]: Đăng ký Thiết bị truyền động lai thành công!")
            else:
                print("[Lỗi] Lựa chọn phân loại không hợp lệ.")
                continue

            devices_list.append(current_device)
            print(
                f"Tên thiết bị (Đã chuẩn hóa tự động qua Setter): {current_device.name}"
            )

        elif choice in [str(i) for i in range(2, 7)]:
            # ERR-IOT-02: Bẫy thao tác rỗng khi chưa kích hoạt hoặc đăng ký bất kỳ thiết bị nào
            if current_device is None:
                print(
                    "[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động."
                )
                continue

            if choice == "2":
                print("\n--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---")
                print(f"Loại thiết bị: {type(current_device).__name__}")
                print(f"Nhà máy: {current_device.factory_name}")
                print(f"Mã thiết bị: {current_device.device_code}")
                print(f"Tên thiết bị: {current_device.name}")
                print(f"Số giờ vận hành: {current_device.operating_hours} giờ")

                if hasattr(current_device, "completed_products"):
                    print(
                        f"Sản phẩm hoàn thành: {current_device.completed_products} sản phẩm"
                    )
                if hasattr(current_device, "current_temperature"):
                    print(
                        f"Nhiệt độ hiện tại: {current_device.current_temperature} độ C"
                    )

                # In chuỗi định tuyến MRO để kỹ sư giám sát cấu trúc đa kế thừa
                mro_chain = " -> ".join(
                    [cls.__name__ for cls in type(current_device).__mro__]
                )
                print(f"[Hệ thống MRO]: {mro_chain}")

            elif choice == "3":
                print("\n--- GHI NHẬN SỐ LIỆU VẬN HÀNH ---")
                try:
                    hours = float(input("Nhập số giờ chạy mới phát sinh: ").strip())

                    # Đa hình động tự nhận biết kiểu đối tượng để hiển thị đúng tham số yêu cầu nhập
                    if isinstance(current_device, HybridSmartActuator):
                        products = int(
                            input(
                                "Nhập số lượng sản phẩm hoàn thành mới bổ sung: "
                            ).strip()
                        )
                        temp = float(
                            input("Nhập thông số đo nhiệt độ phòng máy mới: ").strip()
                        )
                        perf_score = current_device.track_performance(
                            hours, new_products=products, temp_reading=temp
                        )
                        print("[Thành công]: Đã cập nhật số liệu vận hành.")
                        print(
                            f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ."
                        )
                        print(
                            f"Chỉ số hiệu suất thiết bị tổng thể (OEE): {perf_score:.1f}%"
                        )

                    elif isinstance(current_device, ProductionRobot):
                        products = int(
                            input(
                                "Nhập số lượng sản phẩm hoàn thành mới bổ sung: "
                            ).strip()
                        )
                        perf_score = current_device.track_performance(hours, products)
                        print("[Thành công]: Đã cập nhật số liệu vận hành.")
                        print(
                            f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ."
                        )
                        print(
                            f"Chỉ số hiệu suất thiết bị tổng thể (OEE): {perf_score:.1f}%"
                        )

                    elif isinstance(current_device, ThermalSensor):
                        temp = float(
                            input("Nhập thông số đo nhiệt độ môi trường mới: ").strip()
                        )
                        variance = current_device.track_performance(hours, temp)
                        print("[Thành công]: Đã cập nhật số liệu vận hành.")
                        print(
                            f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ."
                        )
                        print(f"Biên độ lệch nhiệt độ an toàn: {variance:.1f} độ C")
                except ValueError:
                    # ERR-IOT-03: Bẫy ngoại lệ nếu nhập chuỗi ký tự không thể ép kiểu sang số
                    print(
                        "[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0."
                    )

            elif choice == "4":
                # Tính đa hình xử lý đồng nhất qua phương thức run_diagnostic
                current_device.run_diagnostic()

            elif choice == "5":
                print("\n--- KIỂM KÊ & SO SÁNH TẢI (OPERATOR OVERLOADING) ---")
                print(
                    f"Thiết bị hiện tại (A): {current_device.device_code} (Số giờ chạy: {current_device.operating_hours} giờ)"
                )
                print("Danh sách thiết bị đối ứng khả dụng trong mạng nhà máy:")

                for idx, dev in enumerate(devices_list):
                    print(
                        f" [{idx}] {dev.device_code} ({dev.name} - Số giờ chạy: {dev.operating_hours} giờ)"
                    )

                try:
                    target_idx = int(
                        input("Chọn số chỉ mục thiết bị đối ứng (B): ").strip()
                    )
                    if target_idx < 0 or target_idx >= len(devices_list):
                        print("[Lỗi] Chỉ mục nằm ngoài danh sách.")
                        continue

                    device_b = devices_list[target_idx]

                    # Thực thi Nạp chồng toán tử so sánh nhỏ hơn (<)
                    is_less = current_device < device_b
                    res_word = "ÍT HƠN" if is_less else "KHÔNG ÍT HƠN"
                    print(
                        f"[Kết quả So sánh (__lt__)]: Hao mòn (số giờ chạy) của thiết bị A {res_word} thiết bị B."
                    )

                    # Thực thi Nạp chồng toán tử toán học cộng (+)
                    total_load = current_device + device_b
                    print(
                        f"[Kết quả Tổng hợp (__add__)]: Tổng thời gian tải vận hành của cả 2 thiết bị là: {total_load} giờ."
                    )
                except TypeError as te:
                    # ERR-IOT-04: Xử lý triệt để lỗi kiểu dữ liệu khi so sánh với đối tượng lạ bên ngoài
                    print(te)
                except ValueError:
                    print("[Lỗi] Vui lòng nhập số nguyên chỉ mục hợp lệ.")

            elif choice == "6":
                print("\n--- XUẤT DỮ LIỆU VẬN HÀNH RA CỔNG NGOẠI VI ---")
                print("1. Xuất dữ liệu qua cổng MQTT (Cloud Stream)")
                print("2. Đồng bộ số liệu vào hệ thống quản trị ERP")
                print("3. Kích hoạt Cổng dữ liệu giả lập lỗi hệ thống")
                gateway_choice = input("Chọn cổng kết nối ngoại vi (1-3): ").strip()

                if gateway_choice == "1":
                    gateway = MQTTEngineGateway()
                elif gateway_choice == "2":
                    gateway = ERPReportGateway()
                elif gateway_choice == "3":
                    gateway = (
                        "Một đối tượng chuỗi văn bản không chuẩn hóa phương thức API"
                    )
                else:
                    print("[Lỗi] Tùy chọn cổng không kết nối.")
                    continue

                try:
                    # Gọi hàm lỏng lẻo thực thi Duck Typing mã nguồn dữ liệu
                    export_telemetry_data(gateway, current_device)
                except AttributeError as ae:
                    # ERR-IOT-05: Bắt trúng ngoại lệ lỗi sai phương thức cổng kết nối của bên thứ ba
                    print(ae)

        elif choice == "7":
            logging.info("Hệ thống nhận lệnh Shutdown an toàn.")
            print(
                "\nCảm ơn bạn đã sử dụng hệ thống Quản lý Thiết bị Rikkei Smart Factory IoT Pro!"
            )
            break


if __name__ == "__main__":
    main()
