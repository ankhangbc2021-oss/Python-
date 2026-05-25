# Phân tích lỗi
#  Dò luồng thực thi (trace code):
# Chương trình bắt đầu bằng print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ').
# Người dùng nhập:
# name_patient (tên bệnh nhân).
# age (tuổi, ép kiểu int).
# symptom (triệu chứng).
# Sau đó in ra phần "PHIẾU KHÁM BỆNH".
# Vấn đề xảy ra ở đoạn in kết quả:
# python

# print('Tên bệnh nhân:', symptom);
# print('Tuổi:', name_patient);
# print('Triệu chứng:', age);

# Biến symptom (triệu chứng) lại được gán cho "Tên bệnh nhân".
# Biến name_patient (tên bệnh nhân) lại được gán cho "Tuổi".
# Biến age (tuổi) lại được gán cho "Triệu chứng".
#  Giải thích vì sao không bị crash:
# Python không báo lỗi vì tất cả biến đều tồn tại và có giá trị hợp lệ.
# Tuy nhiên, dữ liệu bị in sai vị trí do lỗi logic (nhầm lẫn biến khi in ra).
#  Nguyên nhân gây lỗi logic:  
# Lập trình viên đã sử dụng sai biến trong phần print(). Đây là lỗi gán nhãn sai, không phải lỗi cú pháp hay kiểu dữ liệu.

# (2) Sửa lỗi

print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ')
name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print('\n --- PHIẾU KHÁM BỆNH --- ')
print('Tên bệnh nhân:', name_patient)
print('Tuổi:', age)
print('Triệu chứng:', symptom)
