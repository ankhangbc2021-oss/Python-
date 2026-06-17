"""Bank"""


class BankAccount:
    """Lớp"""

    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__account_name = account_name
        self.__balance = 0

    # end alternate constructor

    @property
    def balance(self):
        """Xem số dư"""
        return self.__balance

    @property
    def account_name(self):
        """Xem tên"""
        return self.__account_name

    @account_name.setter
    def update_acc_name(self, new_name):
        clean_name = new_name.strip().upper()
        if clean_name:
            self.__account_name = clean_name
            print("Cập nhật thành công. Tên mới:", self.__account_name)
        else:
            print("Tên tài khoản không được để trống")

    @staticmethod
    def validate_account_number(account_number):
        """Kiểm tra số tk"""
        return len(account_number) == 10 and account_number.isdigit()

    @classmethod
    def update_transaction_fee(cls, new_fee):
        """Cập nhật phí giao dịch"""
        if new_fee > 0:
            cls.transaction_fee = new_fee
            print(
                f"Đã cập nhật phí giao dịch hệ thống thành {cls.transaction_fee:,} VNĐ"
            )
        else:
            print(
                f"Phí giao dịch không được âm\nPhis giao dịch hiện tại {cls.transaction_fee:,} VNĐ"
            )

    def deposit(self, amount):
        """Nạp tiền vào"""
        if amount > 0:
            self.__balance += amount
            print(f"Nạp tiền thành công +{amount:,} VNĐ")
            print(f"Số dư mới: {self.__balance:,} VNĐ")
        else:
            print("Số giao dịch phải lớn hơn 0")

    def withdraw(self, amount):
        """Rút tiền"""
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        total_account = amount + BankAccount.transaction_fee
        if self.__balance >= total_account:
            self.__balance -= total_account
            print(f"Rút tiền thành công: -{amount:,} VNĐ")
            print(f"Phí giao dịch {BankAccount.transaction_fee:,} VNĐ")
            print(f"Số dư mới: {self.__balance:,} VNĐ")
        else:
            print(
                "Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            print(f"Số dư mới: {self.__balance:,} VNĐ")

    def display_info(self):
        """Hiển thị"""
        print(f"""--- THÔNG TIN TÀI KHOẢN ---
Ngân hàng: {BankAccount.bank_name}
Số tài khoản: {self.account_number}
Tên chủ tài khoản: {self.account_name.upper()}
Số dư hiện tại: {self.__balance:,} VNĐ
Phí giao dịch: {BankAccount.transaction_fee:,} VNĐ""")


# ==== MAIN ====
current_account = None


while True:
    print("""
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================""")
    choice = input("Chọn chức năng (1-6): ").strip()
    match choice:
        case "1":
            print("--- MỞ TÀI KHOẢN MỚI ---")
            while True:
                acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                if not BankAccount.validate_account_number(acc_num):
                    print(
                        "Số tài khoản không hợp lệ!\nSố tài khoản phải gồm đúng 10 chữ số."
                    )
                    continue
                break
            acc_name = input("Tên chủ tài khoản: ").strip()
            current_account = BankAccount(acc_num, acc_name)
            print("Mở tài khoản thành công")
        case "2":
            if current_account is None:
                print("Vui lòng mở tài khoản (Chức năng 1) trước")
            else:
                current_account.display_info()
        case "3":
            if current_account is None:
                print("Vui lòng mở tài khoản (Chức năng 1) trước")
                continue

            print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            while True:
                choice_case = input("1. Nạp tiền\n2. Rút tiền\nChọn loại giao dịch (1-2): ")
                if choice_case not in ("1", "2"):
                    print("Lựa chọn không hợp lệ")
                    continue
                break
            while True:
                try:
                    value_amount = int(input("Nhập số tiền giao dịch: "))
                    if not value_amount:
                        print("Số tiền không được để trống")
                        continue
                    break
                except ValueError:
                    print("Vui lòng nhập số nguyên")
                    continue
            match choice_case:
                case "1":
                    current_account.deposit(value_amount)
                case "2":
                    current_account.withdraw(value_amount)
        case "4":
            if current_account is None:
                print("Vui lòng mở tài khoản (Chức năng 1) trước")
                continue

            print("--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
            new_name_account = input("Nhập tên mới: ")
            current_account.update_acc_name = new_name_account
        case "5":
            if current_account is None:
                print("Vui lòng mở tài khoản (Chức năng 1) trước")
                continue

            print("--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VNĐ")
            while True:
                try:
                    value_fee = int(input("Phí giao dịch mới: "))
                    break
                except ValueError:
                    print("Vui lòng nhập số nguyên")
            BankAccount.update_transaction_fee(value_fee)
        case "6":
            print("Đã thoát")
            break
        case _:
            print("Vui lòng chọn 1-6")
