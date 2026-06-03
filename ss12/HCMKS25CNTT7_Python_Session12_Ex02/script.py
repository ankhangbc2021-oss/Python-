""""
Hệ Thống Quản Lý Tài Khoản Tiết Kiệm TechBank
"""
# dữ liệu gốc
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active",
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active",
    },
]


while True:
    print("===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("Danh sách sổ tiết kiệm:")
                for i, acc in enumerate(saving_accounts, 1):
                    print(
                        f"{i}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                        f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                        f"Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}"
                    )

        case "2":
            acc_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            if any(acc["account_id"] == acc_id for acc in saving_accounts):
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue
            name = input("Nhập tên khách hàng: ").strip()
            if not name:
                print("Tên khách hàng không được để trống")
                continue
            try:
                balance = int(input("Nhập số tiền gửi: "))
                term = int(input("Nhập kỳ hạn gửi theo tháng: "))
                rate = float(input("Nhập lãi suất năm: "))
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")
                continue
            if balance <= 0 or term <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
            if rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
            saving_accounts.append(
                {
                    "account_id": acc_id,
                    "customer_name": name,
                    "balance": balance,
                    "term_months": term,
                    "interest_rate": rate,
                    "status": "active",
                }
            )
            print("Đã mở sổ tiết kiệm mới thành công!")

        case "3":
            acc_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            acc = next((a for a in saving_accounts if a["account_id"] == acc_id), None)
            if not acc:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
            if acc["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                continue
            name = input("Nhập tên khách hàng mới: ").strip()
            if not name:
                print("Tên khách hàng không được để trống")
                continue
            try:
                balance = int(input("Nhập số tiền gửi mới: "))
                term = int(input("Nhập kỳ hạn mới theo tháng: "))
                rate = float(input("Nhập lãi suất năm mới: "))
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")
                continue
            if balance <= 0 or term <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
            if rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
            acc.update(
                {
                    "customer_name": name,
                    "balance": balance,
                    "term_months": term,
                    "interest_rate": rate,
                }
            )
            print("Đã cập nhật thông tin sổ tiết kiệm!")

        case "4":
            acc_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            acc = next((a for a in saving_accounts if a["account_id"] == acc_id), None)
            if not acc:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            acc["status"] = "closed"
            print("Đã tất toán sổ tiết kiệm!")

        case "5":
            acc_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            acc = next((a for a in saving_accounts if a["account_id"] == acc_id), None)
            if not acc:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue
            interest = (
                acc["balance"] * acc["interest_rate"] / 100 * acc["term_months"] / 12
            )
            total = acc["balance"] + interest
            print(f"Tiền lãi dự kiến: {interest:.2f}")
            print(f"Tổng tiền nhận khi đến hạn: {total:.2f}")

        case "6":
            acc_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            acc = next((a for a in saving_accounts if a["account_id"] == acc_id), None)
            if not acc:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue
            try:
                months = int(input("Nhập số tháng thực gửi: "))
            except ValueError:
                print("Số tháng thực gửi không hợp lệ!")
                continue
            if months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue
            if months < acc["term_months"]:
                rate = 0.5
                print("Khách hàng rút trước hạn, áp dụng lãi suất 0.5%/năm")
            else:
                rate = acc["interest_rate"]
                print("Khách hàng đủ kỳ hạn, áp dụng lãi suất ban đầu")
            interest = acc["balance"] * rate / 100 * months / 12
