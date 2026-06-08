"""
(1) Thiết kế Hàm (Phân tích trước khi code)
Hàm phụ trợ:
find_patient_index(records, patient_id)
Input: records (list các chuỗi), patient_id (string)
Output: index (int) hoặc -1 nếu không tìm thấy
Pseudocode:

pid = patient_id.strip().upper()
for i, record in enumerate(records):
    if record.startswith(pid):
        return i
return -1
Chức năng 1: display_records(records)
Input: danh sách hồ sơ (list of strings)
Output: in ra màn hình (None)

Pseudocode:
if records empty:
    print("Hệ thống hiện chưa có hồ sơ nào.")
else:
    for i, record in enumerate(records):
        split record by "-"
        print formatted info
Chức năng 2: add_patient(records)

Input: danh sách hồ sơ (list of strings)
Output: danh sách đã cập nhật (list)
Pseudocode:

nhập pid, name, year, diagnosis
chuẩn hóa pid = strip().upper()
kiểm tra trùng bằng find_patient_index
kiểm tra rỗng
kiểm tra year.isdigit() và 1900 <= year <= current_year
chuẩn hóa name = strip().title().replace("-", " ")
chuẩn hóa diagnosis = strip().capitalize().replace("-", " ")
ghép chuỗi: f"{pid}-{name}-{year}-{diagnosis}"
append vào records
Chức năng 3: update_diagnosis(records)

Input: danh sách hồ sơ (list of strings)
Output: danh sách đã cập nhật (list)
Pseudocode:
nhập pid
idx = find_patient_index(records, pid)
if idx == -1: báo lỗi
else:
    split record thành list [pid, name, year, diag]
    nhập new_diag
    chuẩn hóa new_diag = strip().capitalize().replace("-", " ")
    gán lại phần tử cuối
    join lại bằng "-"
    records[idx] = new_record
Chức năng 4: generate_age_report(records)

Input: danh sách hồ sơ (list of strings)
Output: in báo cáo (None)
Pseudocode:

current_year = datetime.now().year
counters = {child:0, adult:0, senior:0}
for record in records:
    split record
    age = current_year - int(year)
    if age < 16: child++
    elif age <= 60: adult++
    else: senior++
print kết quả
Chức năng 5: Thoát

In thông báo và break vòng lặp.
"""

# (2) Triển khai code
from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    """Tìm index bệnh nhân theo mã BN."""
    pid = patient_id.strip().upper()
    for i, record in enumerate(records):
        if record.startswith(pid):
            return i
    return -1

def display_records(records):
    """Hiển thị danh sách hồ sơ bệnh án."""
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
    else:
        print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
        for i, record in enumerate(records, start=1):
            pid, name, year, diag = record.split("-")
            print(f"{i}. [{pid}] {name:<15} | Năm sinh: {year} | Chẩn đoán: {diag}")
        print("--------------------------------------------------------------------------")

def add_patient(records):
    """Thêm hồ sơ bệnh nhân mới."""
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    pid = input("Nhập mã bệnh nhân: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(records, pid) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title().replace("-", " ")
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return

    year = input("Nhập năm sinh: ").strip()
    current_year = datetime.now().year
    if not year.isdigit() or not (1900 <= int(year) <= current_year):
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return

    diag = input("Nhập chẩn đoán: ").strip().capitalize().replace("-", " ")
    if not diag:
        print("Chẩn đoán bệnh không được để trống!")
        return

    new_record = f"{pid}-{name}-{year}-{diag}"
    records.append(new_record)
    print("Thêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu lưu:", new_record)

def update_diagnosis(records):
    """Cập nhật chẩn đoán theo mã BN."""
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    pid = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    idx = find_patient_index(records, pid)
    if idx == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {pid}!")
        return
    pid, name, year, diag = records[idx].split("-")
    print(f"Tìm thấy bệnh nhân: {name}")
    print(f"Chẩn đoán hiện tại: {diag}")
    new_diag = input("Nhập chẩn đoán mới: ").strip().capitalize().replace("-", " ")
    if not new_diag:
        print("Chẩn đoán bệnh không được để trống!")
        return
    records[idx] = f"{pid}-{name}-{year}-{new_diag}"
    print("Cập nhật chẩn đoán thành công!")

def generate_age_report(records):
    """Báo cáo phân loại bệnh nhân theo độ tuổi."""
    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    current_year = datetime.now().year
    child = adult = senior = 0
    for record in records:
        _, _, year, _ = record.split("-")
        age = current_year - int(year)
        if age < 16:
            child += 1
        elif age <= 60:
            adult += 1
        else:
            senior += 1
    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {senior} bệnh nhân")
    print("--------------------------------------")

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")
        choice = input("Chọn chức năng (1-5): ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
        choice = int(choice)
        if choice == 1:
            display_records(patient_records)
        elif choice == 2:
            add_patient(patient_records)
        elif choice == 3:
            update_diagnosis(patient_records)
        elif choice == 4:
            generate_age_report(patient_records)
        elif choice == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

if __name__ == "__main__":
    main()
