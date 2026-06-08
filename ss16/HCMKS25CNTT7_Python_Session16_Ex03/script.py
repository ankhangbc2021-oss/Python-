"""
(1) Phân tích & Thiết kế giải pháp
Input/Output cho từng hàm:
display_patients(patient_list)
Input: danh sách bệnh nhân (list of lists)
Output: in ra màn hình, không return
validate_gender(gender_input)
Input: chuỗi giới tính (string)
Output: True/False (boolean)
add_patient(patient_list)
Input: danh sách bệnh nhân (list of lists)
Output: danh sách đã cập nhật (list)
find_patient_index(patient_list, patient_id)
Input: danh sách bệnh nhân, mã BN (string)
Output: index (int) hoặc -1 nếu không tìm thấy
update_diagnosis(patient_list)
Input: danh sách bệnh nhân (list of lists)
Output: danh sách đã cập nhật (list)
search_by_disease(patient_list)
Input: danh sách bệnh nhân (list of lists)
Output: in ra kết quả tìm kiếm, không return
Giải pháp:
Chuỗi (String) được chuẩn hóa bằng .strip(), .upper(), .title(), .capitalize(), .lower().
Danh sách (List) lưu từng bệnh nhân dưới dạng list con.
Khi truyền patient_list vào hàm, thực chất là truyền tham chiếu (reference). Vì vậy, mọi thay đổi trong hàm sẽ ảnh hưởng trực tiếp đến danh sách gốc, trừ khi ta tạo bản sao.

"""

# (2) Triển khai Code
patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def display_patients(patient_list):
    """Hiển thị danh sách bệnh nhân hiện tại."""
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
    else:
        print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
        for i, p in enumerate(patient_list, start=1):
            print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

def validate_gender(gender_input):
    """Kiểm tra giới tính hợp lệ (nam/nu)."""
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]

def find_patient_index(patient_list, patient_id):
    """Tìm index bệnh nhân theo mã BN."""
    pid = patient_id.strip().upper()
    for i, p in enumerate(patient_list):
        if p[0] == pid:
            return i
    return -1

def add_patient(patient_list):
    """Tiếp nhận bệnh nhân mới và thêm vào danh sách."""
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    pid = input("Nhập mã bệnh nhân: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, pid) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return

    gender = input("Nhập giới tính Nam/Nu: ")
    while not validate_gender(gender):
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
        gender = input("Nhập giới tính Nam/Nu: ")
    gender = gender.strip().capitalize()

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if not diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list.append([pid, name, gender, diagnosis])
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    """Cập nhật chẩn đoán bệnh theo mã BN."""
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    pid = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if not pid:
        print("Mã bệnh nhân không được để trống!")
        return
    idx = find_patient_index(patient_list, pid)
    if idx == -1:
        print(f"Không tìm thấy hồ sơ mang mã {pid}!")
        return
    print(f"Tìm thấy bệnh nhân: {patient_list[idx][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[idx][3]}")
    new_diag = input("Nhập chẩn đoán mới: ").strip().capitalize()
    if not new_diag:
        print("Chẩn đoán bệnh không được để trống!")
        return
    patient_list[idx][3] = new_diag
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    """Tìm kiếm bệnh nhân theo từ khóa bệnh."""
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip().lower()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    results = [p for p in patient_list if keyword in p[3].lower()]
    if results:
        print("Kết quả tìm kiếm:")
        for i, p in enumerate(results, start=1):
            print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    print(f"Có tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")

def main():
    """Vòng lặp menu chính."""
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")
        choice = input("Nhập lựa chọn của bạn: ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
        choice = int(choice)
        if choice == 1:
            display_patients(patients)
        elif choice == 2:
            add_patient(patients)
        elif choice == 3:
            update_diagnosis(patients)
        elif choice == 4:
            search_by_disease(patients)
        elif choice == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

if __name__ == "__main__":
    main()
