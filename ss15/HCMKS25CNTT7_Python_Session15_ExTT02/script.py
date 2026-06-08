# Global variables
atm_vault_balance = 50000000  # 50 triệu
user_account_balance = 10000000  # 10 triệu


def display_balances():
    """
    Hiển thị số dư tài khoản và ATM (debug).
    Không nhận tham số, sử dụng biến toàn cục.
    """
    global atm_vault_balance, user_account_balance
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản và ATM.
    Parameters:
        amount (int): số tiền muốn nạp
    Returns:
        bool: True nếu thành công, False nếu thất bại
    """
    global atm_vault_balance, user_account_balance
    if amount <= 0:
        print("Số tiền không hợp lệ.")
        return False
    user_account_balance += amount
    atm_vault_balance += amount
    print(
        f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND."
    )
    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.
    Parameters:
        amount (int): số tiền muốn rút
    Returns:
        str: trạng thái ("INSUFFICIENT_FUNDS", "ATM_OUT_OF_CASH", "INVALID_AMOUNT", "INVALID_MULTIPLE", "OK")
    """
    global atm_vault_balance, user_account_balance
    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID_AMOUNT"
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện rút tiền, cập nhật số dư.
    Parameters:
        total_deduction (int): tổng số tiền bị trừ (bao gồm phí)
        amount_to_dispense (int): số tiền mặt trả cho khách
    Returns:
        None
    """
    global atm_vault_balance, user_account_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    """
    Vòng lặp menu chính của hệ thống ATM.
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == "1":
            display_balances()
        elif choice == "2":
            amount_str = input("Nhập số tiền muốn nạp: ")
            if not amount_str.isdigit():
                print("Vui lòng nhập số hợp lệ (chỉ gồm chữ số).")
                continue
            amount = int(amount_str)
            deposit_money(amount)
        elif choice == "3":
            amount_str = input("Nhập số tiền cần rút: ")
            if not amount_str.isdigit():
                print("Vui lòng nhập số hợp lệ (chỉ gồm chữ số).")
                continue
            amount = int(amount_str)
            status = check_withdrawal_rules(amount)
            if status == "INVALID_AMOUNT":
                print("Số tiền không hợp lệ.")
            elif status == "INVALID_MULTIPLE":
                print("Số tiền rút phải là bội số của 50,000.")
            elif status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Số dư tài khoản không đủ.")
            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
            elif status == "OK":
                fee = 1100
                total_deduction = amount + fee
                execute_withdrawal(total_deduction, amount)
        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


# Chạy chương trình
if __name__ == "__main__":
    main()
