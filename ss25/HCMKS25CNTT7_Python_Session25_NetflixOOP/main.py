"""
(1) Phân tích giải pháp
Name Mangling (Encapsulation):
Trong class NetflixAccount, các thuộc tính nhạy cảm như __password và __plan được đặt private bằng dấu __. Điều này ngăn chặn việc truy cập trực tiếp từ bên ngoài, đảm bảo mật khẩu không bị in ra hoặc sửa trái phép, và gói cước chỉ có thể thay đổi qua phương thức hợp lệ.

Class Method ảnh hưởng toàn hệ thống:
update_max_profiles(cls, new_limit) thay đổi giới hạn số lượng profile cho toàn bộ các tài khoản Netflix. Vì đây là biến class (max_profiles), mọi instance hiện có và sau này đều sẽ áp dụng giới hạn mới ngay lập tức.
"""


# (2) Triển khai code
class NetflixAccount:
    """
    NetflixAccount class quản lý tài khoản Netflix với Encapsulation.
    """

    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = None
        self.__plan = "Basic"
        self.profiles = []

    # Encapsulation: password chỉ hiển thị ********
    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
        else:
            raise ValueError("Password is too short")

    # plan chỉ đọc
    @property
    def plan(self):
        return self.__plan

    # Static Method: kiểm tra email hợp lệ
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    # Class Method: cập nhật giới hạn profile toàn hệ thống
    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit
        print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {cls.max_profiles}")

    # Instance Methods
    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
        else:
            self.profiles.append(profile_name)
            print(f"Đã thêm Profile mới: {profile_name}")

    def upgrade_plan(self, new_plan):
        if new_plan in ["Basic", "Standard", "Premium"]:
            self.__plan = new_plan
            print(f"Gói cước đã được nâng cấp thành {self.__plan}")
        else:
            print("Gói cước không hợp lệ. Chỉ chấp nhận Basic, Standard, Premium.")

    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.__plan}")
        print(
            f"Danh sách Profiles: {', '.join(self.profiles) if self.profiles else 'Chưa có'}"
        )


# ================= MAIN FLOW =================
current_account = None

while True:
    print("\n===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix")
    print("6. Thoát chương trình")
    print("===================================")
    choice = input("Chọn chức năng (1-6): ")

    match choice:
        case "1":
            print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
            email = input("Nhập Email: ")
            if not NetflixAccount.validate_email(email):
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                continue
            current_account = NetflixAccount(email)
            while True:
                try:
                    pwd = input("Nhập mật khẩu (>=6 ký tự): ")
                    current_account.password = pwd
                    break
                except ValueError as e:
                    print(e)
            print("Đăng ký thành công!")
            current_account.display_info()

        case "2":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            else:
                current_account.display_info()

        case "3":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue
            profile_name = input("Nhập tên Profile mới: ")
            current_account.add_profile(profile_name)

        case "4":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue
            print("Các gói cước: Basic, Standard, Premium")
            new_plan = input("Nhập gói cước muốn nâng cấp: ")
            current_account.upgrade_plan(new_plan)

        case "5":
            try:
                new_limit = int(input("Nhập giới hạn Profile mới: "))
                NetflixAccount.update_max_profiles(new_limit)
            except ValueError:
                print("Giới hạn phải là số nguyên!")

        case "6":
            print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-6.")
