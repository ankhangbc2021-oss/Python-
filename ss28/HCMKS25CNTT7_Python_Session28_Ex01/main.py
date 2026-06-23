from abc import ABC, abstractmethod

# ==========================================
# 1. CỔNG THANH TOÁN (DUCK TYPING CLASSES)
# ==========================================

class VietcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print(f"[Hệ thống VCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print(f"Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.employee_code}.\n")

class TechcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print(f"[Hệ thống TCB Business API]: Đang thiết lập kết nối an toàn...")
        print(f"Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.employee_code}.\n")


# Hàm toàn cục thực hiện chi trả lương áp dụng cơ chế Duck Typing
def execute_payroll(payment_service, employee, amount):
    # Edge Case 4: Kiểm tra sự tồn tại của phương thức transfer_salary
    if not hasattr(payment_service, "transfer_salary") or not callable(getattr(payment_service, "transfer_salary")):
        raise AttributeError("Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết liên thông kỹ thuật.")
    payment_service.transfer_salary(employee, amount)


# ==========================================
# 2. KIẾN TRÚC LỚP NHÂN SỰ (HR CLASSES)
# ==========================================

class BaseEmployee(ABC):
    """
    Abstract Base Class (ABC) - Định nghĩa bộ khung chuẩn cho mọi nhân sự tại Rikkei Education.
    """
    company_name = "Rikkei Education"
    base_salary_rate = 3000000  # Mức lương cơ sở mặc định

    def __init__(self, employee_code, name):
        self._employee_code = employee_code
        self.name = name  # Sẽ kích hoạt setter để chuẩn hóa tên
        self.__working_hours = 0  # Thuộc tính private đóng gói nghiêm ngặt công nhật

    # Encapsulation qua Property (Chỉ có getter, không có setter trực tiếp)
    @property
    def working_hours(self):
        return self.__working_hours

    @property
    def employee_code(self):
        return self._employee_code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Chuẩn hóa họ tên: In hoa và loại bỏ khoảng trắng thừa
        self._name = " ".join(value.strip().split()).upper()

    def add_working_hours(self, hours):
        """Phương thức nội bộ để tăng giờ làm việc hợp lệ"""
        if hours <= 0:
            raise ValueError("Số giờ làm việc cộng thêm không được nhỏ hơn hoặc bằng 0.")
        self.__working_hours += hours

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng tính lương bắt buộc ghi đè"""
        pass

    @abstractmethod
    def update_kpi(self, progress):
        """Phương thức trừu tượng cập nhật KPI bắt buộc ghi đè"""
        pass

    # @staticmethod: Hàm tiện ích kiểm tra định dạng mã nhân sự độc lập với trạng thái đối tượng
    @staticmethod
    def validate_employee_code(emp_code):
        return len(emp_code) == 10 and emp_code.startswith("RKE")

    # @classmethod: Phương thức thao tác trên cấp độ Lớp, ảnh hưởng đến toàn bộ instance
    @classmethod
    def update_base_salary_rate(cls, new_rate):
        if new_rate <= 0:
            raise ValueError("Mức lương cơ sở phải lớn hơn 0.")
        cls.base_salary_rate = new_rate

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        # Edge Case 3: Kiểm tra kiểu dữ liệu đối ứng
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours + other.working_hours

    # Operator Overloading: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        # Edge Case 3: Kiểm tra kiểu dữ liệu đối ứng
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours < other.working_hours


class Lecturer(BaseEmployee):
    """Subclass quản lý đội ngũ Giảng viên"""
    def __init__(self, employee_code, name):
        super().__init__(employee_code, name)
        self.teaching_slots = 0

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)

    def update_kpi(self, progress):
        # Giả định tiến độ là tỷ lệ phần trăm hoặc số ca hoàn thành thêm
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0.")
        print(f"[Lecturer KPI] Đã cập nhật tiến độ giảng dạy: Đạt {progress}% kế hoạch.")

    def conduct_class(self):
        """Tự động tăng 1 ca dạy và cộng 2 giờ làm việc"""
        self.teaching_slots += 1
        self.add_working_hours(2)


class AdmissionStaff(BaseEmployee):
    """Subclass quản lý đội ngũ Tuyển sinh"""
    def __init__(self, employee_code, name, kpi_target=100000000):
        super().__init__(employee_code, name)
        self.revenue_generated = 0
        self.kpi_target = kpi_target

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05)

    def update_kpi(self, progress):
        # Đối với tuyển sinh, progress chính là doanh thu hợp đồng mới mang về
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0.")
        self.revenue_generated += progress


class HybridManager(Lecturer, AdmissionStaff):
    """Multiple Inheritance Subclass kế thừa từ cả Lecturer và AdmissionStaff"""
    def __init__(self, employee_code, name):
        # Sử dụng super().__init__ tuân theo cơ chế MRO để khởi tạo đúng chuỗi lớp
        super().__init__(employee_code, name)
        # Khởi tạo riêng các thuộc tính của nhánh AdmissionStaff do Lecturer độc lập không có
        self.revenue_generated = 0
        self.kpi_target = 100000000

    def calculate_salary(self):
        # Tích hợp cả lương cứng, phụ cấp ca dạy của Lecturer và hoa hồng của AdmissionStaff
        base_and_slots = (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)
        commission = self.revenue_generated * 0.05
        return base_and_slots + commission

    def update_kpi(self, progress):
        # Hybrid Manager có thể nhận cập nhật KPI tùy biến, ở đây xử lý mặc định tăng doanh số
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0.")
        self.revenue_generated += progress


# ==========================================
# 3. HỆ THỐNG MENU ĐIỀU KHIỂN CHƯƠNG TRÌNH (CLI)
# ==========================================

def main():
    employees = []
    current_employee = None

    # Tạo sẵn dữ liệu mẫu để dễ dàng test chức năng so sánh / gộp giờ công ở Chức năng 5
    sample_emp = Lecturer("RKE0099999", "Nguyen Van An")
    sample_emp.add_working_hours(180)
    employees.append(sample_emp)

    while True:
        print("\n===== RIKKEI EDUCATION HR SIMULATOR PRO =====")
        print("1. Tuyển dụng nhân sự mới (Chọn loại hợp đồng nhân sự)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Ghi nhận công nhật & Cập nhật KPI (Tính đa hình)")
        print("4. Tổng hợp quỹ lương và ngân sách chi trả")
        print("5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất (Overloading)")
        print("6. Giải ngân lương qua Cổng thanh toán đối tác (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == "1":
            print("\n--- CHỌN LOẠI NHÂN SỰ KHỞI TẠO ---")
            print("1. Lecturer (Giảng viên chuyên trách)")
            print("2. Admission Staff (Nhên viên Tuyển sinh)")
            print("3. Hybrid Manager (Quản lý kiêm Giảng dạy)")
            emp_type = input("Chọn loại nhân sự (1-3): ").strip()
            
            emp_code = input("Nhập mã nhân sự 10 ký tự: ").strip()
            # Sử dụng staticmethod để kiểm tra tính hợp lệ của mã nhân sự
            if not BaseEmployee.validate_employee_code(emp_code):
                print("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
                continue
                
            name = input("Nhập họ và tên: ")

            try:
                if emp_type == "1":
                    current_employee = Lecturer(emp_code, name)
                    print(f"Tuyển dụng Giảng viên thành công!")
                elif emp_type == "2":
                    current_employee = AdmissionStaff(emp_code, name)
                    print(f"Tuyển dụng Nhân viên Tuyển sinh thành công!")
                elif emp_type == "3":
                    current_employee = HybridManager(emp_code, name)
                    print(f"Tuyển dụng Quản lý Hybrid thành công!")
                else:
                    print("Lựa chọn loại nhân sự không hợp lệ.")
                    continue
                
                # Mặc định kích hoạt thêm 160 giờ làm việc nền cho nhân sự mới để chạy demo tính lương
                current_employee.add_working_hours(160)
                employees.append(current_employee)
                print(f"Tên nhân sự (đã chuẩn hóa): {current_employee.name}")

            except TypeError as e:
                # Edge Case 1: Đánh bẫy nếu vô tình cố khởi tạo trực tiếp BaseEmployee
                print(f"[LỖI HỆ THỐNG]: Không thể khởi tạo trực tiếp lớp trừu tượng! Chi tiết: {e}")

        elif choice == "2":
            if not current_employee:
                print("Vui lòng thực hiện tuyển dụng nhân sự (Chức năng 1) trước.")
                continue
            
            print("\n--- THÔNG TIN NHÂN SỰ HIỆN TẠI ---")
            print(f"Loại nhân sự: {type(current_employee).__name__}")
            print(f"Tổ chức: {current_employee.company_name}")
            print(f"Mã nhân sự: {current_employee.employee_code}")
            print(f"Họ và tên: {current_employee.name}")
            print(f"Số giờ làm việc: {current_employee.working_hours} giờ")
            
            if isinstance(current_employee, Lecturer):
                print(f"Số ca đã dạy: {current_employee.teaching_slots} ca")
            if isinstance(current_employee, AdmissionStaff):
                print(f"Doanh số mang về: {current_employee.revenue_generated:,.0f} VND")
                
            print(f"\n[MRO CHECK] Thứ tự tìm kiếm phương thức (MRO):")
            for cls in type(current_employee).__mro__:
                print(f" -> {cls.__name__}")

        elif choice == "3":
            if not current_employee:
                print("Vui lòng thực hiện tuyển dụng nhân sự trước.")
                continue

            print("\n--- GHI NHẬN CÔNG NHẬT & HIỆU SUẤT ---")
            print("1. Ghi nhận tham gia đứng lớp (Chỉ dành cho Giảng viên/Hybrid)")
            print("2. Cập nhật tiến độ KPI / Doanh số")
            task = input("Chọn tác vụ (1-2): ").strip()

            try:
                if task == "1":
                    if isinstance(current_employee, Lecturer):
                        current_employee.conduct_class()
                        print("Ghi nhận thành công! Thầy/Cô đã hoàn thành thêm 1 ca dạy.")
                        print(f"Số ca dạy hiện tại: {current_employee.teaching_slots} ca.")
                        print(f"Số giờ làm việc tích lũy: {current_employee.working_hours} giờ.")
                    else:
                        print("Lỗi: Nhân sự hiện tại không có chức năng giảng dạy!")
                elif task == "2":
                    val = float(input("Nhập giá trị hiệu suất / doanh số mới mang về: ").strip())
                    # Tính Đa Hình thể hiện ở đây: Cùng gọi update_kpi nhưng hành vi chạy tự thích ứng
                    current_employee.update_kpi(val)
                    print("Cập nhật KPI thành công!")
                    if hasattr(current_employee, 'revenue_generated'):
                        print(f"Doanh số tích lũy mới: {current_employee.revenue_generated:,.0f} VND.")
                else:
                    print("Tác vụ không hợp lệ.")
            except ValueError as e:
                # Edge Case 2: Bắt lỗi số âm hoặc sai định dạng dữ liệu đầu vào
                print(f"[LỖI DỮ LIỆU]: {e}")

        elif choice == "4":
            if not current_employee:
                print("Vui lòng tuyển dụng nhân sự trước.")
                continue

            # Đa hình qua phương thức calculate_salary()
            salary = current_employee.calculate_salary()
            print("\n--- CHI TIẾT QUỸ LƯƠNG NHÂN SỰ ---")
            print(f"Nhân sự: {current_employee.name} (Loại: {type(current_employee).__name__})")
            print(f"Mức lương cơ sở hệ thống: {current_employee.base_salary_rate:,.0f} VND")
            print(f"Số giờ làm việc tích lũy: {current_employee.working_hours} giờ")
            print(f"Tổng lương thực nhận tháng này: {salary:,.0f} VND")

        elif choice == "5":
            if not current_employee:
                print("Vui lòng tuyển dụng nhân sự trước.")
                continue

            print("\n--- ĐỒNG BỘ & SO SÁNH GIỜ CÔNG (OPERATOR OVERLOADING) ---")
            print(f"Nhân sự hiện tại (A): {current_employee.name} (Giờ công: {current_employee.working_hours} giờ)")
            print(f"Danh sách nhân sự đối ứng trong hệ thống:")
            
            for idx, emp in enumerate(employees):
                print(f" [{idx}] {emp.employee_code} - {emp.name} (Giờ công: {emp.working_hours} giờ)")
                
            try:
                target_idx = int(input("Chọn số chỉ mục nhân sự đối ứng (B) từ danh sách: ").strip())
                if target_idx < 0 or target_idx >= len(employees):
                    print("Chỉ mục không hợp lệ.")
                    continue
                
                emp_b = employees[target_idx]
                
                # Thực hiện so sánh qua Overloading __lt__
                is_less = current_employee < emp_b
                if is_less == NotImplemented:
                    print("[LỖI EXCEPTION]: Đối tượng so sánh không tương thích hệ thống.")
                else:
                    res_str = "ÍT HƠN" if is_less else "KHÔNG ÍT HƠN"
                    print(f"[Kết quả So sánh (__lt__)]: Giờ công cống hiến của nhân sự A {res_str} nhân sự B.")
                
                # Thực hiện cộng gộp qua Overloading __add__
                total_hours = current_employee + emp_b
                if total_hours == NotImplemented:
                    print("[LỖI EXCEPTION]: Đối tượng cộng gộp không hợp lệ.")
                else:
                    print(f"[Kết quả Tổng hợp (__add__)]: Tổng số giờ làm việc của cả 2 nhân sự là: {total_hours} giờ.")
            except Exception as e:
                print(f"Đã xảy ra lỗi khi tính toán: {e}")

        elif choice == "6":
            if not current_employee:
                print("Vui lòng tuyển dụng nhân sự trước.")
                continue

            print("\n--- CHI TRẢ LƯƠNG QUA CỔNG ĐỐI TÁC TRUNG GIAN ---")
            print("1. Chi trả qua tài khoản Doanh nghiệp Vietcombank")
            print("2. Chi trả qua tài khoản Doanh nghiệp Techcombank")
            print("3. Giả lập lỗi Cổng dịch vụ không hợp lệ (Kiểm試 Edge Case)")
            bank_choice = input("Chọn cổng ngân hàng (1-3): ").strip()

            amount = current_employee.calculate_salary()

            if bank_choice == "1":
                service = VietcombankCorporateService()
            elif bank_choice == "2":
                service = TechcombankCorporateService()
            elif bank_choice == "3":
                service = "Một chuỗi text không phải Class Ngân Hàng hợp lệ"
            else:
                print("Lựa chọn không hợp lệ.")
                continue

            try:
                # Gọi hàm giải ngân áp dụng Duck Typing độc lập
                execute_payroll(service, current_employee, amount)
            except AttributeError as e:
                # Edge Case 4: Xử lý ngoại lệ lỗi sai lệch cấu trúc phương thức ngân hàng đối tác
                print(f"[LỖI BẢO MẬT API]: {e}")

        elif choice == "7":
            print("\nCảm ơn đã sử dụng hệ thống Quản lý Nhân sự Rikkei Education Pro!")
            break
        else:
            print("Vui lòng chọn lại các tính năng từ 1 đến 7.")

if __name__ == "__main__":
    main()