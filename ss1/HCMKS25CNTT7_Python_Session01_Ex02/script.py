# Phân tích lỗi
# Dò luồng thực thi (trace code):
# Chương trình in ra tiêu đề "--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---".
# Người dùng nhập:
# name_patient (tên bệnh nhân).
# weight (cân nặng bệnh nhân).
# Sau đó in ra thông tin đã nhập và kiểm tra kiểu dữ liệu bằng type(weight).
# Đặc điểm của hàm input() trong Python:
# input() luôn trả về chuỗi (string), bất kể người dùng nhập số hay chữ.
# Ví dụ: nhập 70 thì giá trị nhận được là "70" (chuỗi), không phải số.
# Nguyên nhân dữ liệu nhập là số nhưng lại được lưu dưới dạng chuỗi:
# Vì không có bước ép kiểu dữ liệu (type casting) sau khi dùng input().
# Do đó, biến weight vẫn giữ kiểu str, dẫn đến sai sót nghiêm trọng khi lưu trữ hoặc tính toán (ví dụ: không thể cộng/trừ nhân chia trực tiếp).
# (2) Sửa lỗi

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân (kg): "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Kiểm tra kiểu dữ liệu sau khi ép kiểu
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))
