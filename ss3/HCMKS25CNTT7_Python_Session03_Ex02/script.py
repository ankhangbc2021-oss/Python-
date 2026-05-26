# (1) Phân tích lỗi
# Trace code khi nhập số ngày công = 0:
# Vòng lặp bắt đầu xử lý nhân viên số 2.

# working_days = 0 → điều kiện if working_days == 0: đúng, chương trình in ra cảnh báo:


# CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.
# Tuy nhiên, sau đó chương trình không dừng mà tiếp tục chạy xuống:

# bonus_amount = working_days * 200000
# print("> Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng!")
# Kết quả: vẫn tính thưởng (0 VND) và gửi email, dù đã cảnh báo không xét duyệt.

# Nguyên nhân:
# Vấn đề nằm ở cấu trúc điều kiện trong vòng lặp. Lập trình viên chỉ dùng if để in cảnh báo, nhưng không có else hoặc continue để bỏ qua phần tính thưởng.

# Đây là lỗi logic kinh điển: không tách nhánh xử lý, dẫn đến việc khối lệnh sau vẫn chạy dù điều kiện cảnh báo đã đúng.

# (2) Sửa lỗi
# Giải pháp:

# Khi số ngày công = 0, in cảnh báo và dùng continue để chuyển ngay sang vòng lặp kế tiếp, bỏ qua phần tính thưởng và gửi email.

print("---- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ----")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("---- Đang xử lý nhân viên số", employee_number, "----")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        # Bỏ qua phần tính thưởng và gửi email, chuyển sang nhân viên tiếp theo
        continue

    # Tính thưởng cho nhân viên đủ ngày công
    bonus_amount = working_days * 200000
    print("> Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng!")
    print("__________________________________________\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
