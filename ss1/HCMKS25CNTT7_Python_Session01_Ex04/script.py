# 1) Phân tích và Đề xuất giải pháp
# Phân tích Input/Output:

# Input ban đầu (từ input()):

# Mã bệnh nhân: kiểu str
# Nhiệt độ cơ thể: kiểu str (dù nhập số, input() vẫn trả về chuỗi)
# Nhịp tim: kiểu str
# Output mong muốn:
# Mã bệnh nhân: giữ nguyên kiểu str
# Nhiệt độ cơ thể: ép kiểu thành float
# Nhịp tim: ép kiểu thành int
# In ra thông tin kèm xác nhận kiểu dữ liệu bằng type()
# Đề xuất 2 giải pháp ép kiểu dữ liệu:

# Giải pháp A – Ép kiểu trực tiếp khi nhập:

# temperature = float(input("Nhập nhiệt độ cơ thể: "))
# heartbeat = int(input("Nhập nhịp tim: "))
# Ưu điểm: ngắn gọn, tiết kiệm bộ nhớ, dễ đọc.

# Nhược điểm: nếu nhập sai định dạng (ví dụ nhập chữ), chương trình sẽ báo lỗi ngay.

# Giải pháp B – Nhập chuỗi trước, sau đó ép kiểu:

# temp_str = input("Nhập nhiệt độ cơ thể: ")
# temperature = float(temp_str)
# hb_str = input("Nhập nhịp tim: ")
# heartbeat = int(hb_str)
# Ưu điểm: dễ debug, có thể kiểm tra dữ liệu trước khi ép kiểu.
# Nhược điểm: tốn thêm biến trung gian, code dài hơn.
# Chốt lựa chọn:

# Trong môi trường bệnh viện, Giải pháp B phù hợp hơn vì dữ liệu y tế rất nhạy cảm, 
# cần dễ kiểm tra và xử lý lỗi nhập liệu. Việc có biến trung gian giúp dễ dàng phát hiện 
# và xử lý ngoại lệ trước khi lưu trữ chính thức.
# (2) Triển khai code Python

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")

# Nhập dữ liệu từ điều dưỡng
patient_code = input("Nhập mã bệnh nhân (ví dụ: BN999): ")

# Nhập nhiệt độ cơ thể (chuỗi trước, ép kiểu sau)
temp_str = input("Nhập nhiệt độ cơ thể (°C): ")
temperature = float(temp_str)

# Nhập nhịp tim (chuỗi trước, ép kiểu sau)
hb_str = input("Nhập nhịp tim (nhịp/phút): ")
heartbeat = int(hb_str)

# Hiển thị kết quả chuẩn hóa dữ liệu
print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_code)
print("Nhiệt độ cơ thể:", temperature, "độ C")
print("⇒ Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))
print("Nhịp tim:", heartbeat, "nhịp/phút")
print("⇒ Kiểu dữ liệu hệ thống ghi nhận:", type(heartbeat))
print("---------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
