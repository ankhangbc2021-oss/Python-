"""(1) Phân tích lỗi
Vì sao strip() và title() không thay đổi chuỗi gốc?  
Trong Python, String là immutable (bất biến). Các phương thức như .strip(), .title(), .upper()… không chỉnh sửa trực tiếp chuỗi ban đầu mà trả về một chuỗi mới. Nếu không gán lại cho biến, giá trị cũ vẫn giữ nguyên.
Cú pháp gán biến đúng:
raw_diagnosis = raw_diagnosis.strip()
raw_diagnosis = raw_diagnosis.title()
Như vậy biến raw_diagnosis sẽ được cập nhật với chuỗi đã chuẩn hóa.
Vì sao extend() gây lỗi?  
list.extend() nhận một iterable và thêm từng phần tử của iterable đó vào list. Khi truyền vào một chuỗi, Python coi chuỗi là một iterable của các ký tự, nên từng ký tự 'v', 'i', 'E'… bị thêm riêng lẻ.
Cách khắc phục:  
Dùng list.append() để thêm nguyên vẹn cả chuỗi "Viem Phe Quan" vào list.

"""

# (2) Sửa lỗi – Source Code đúng chuẩn
# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    """
    Chuẩn hóa tên bệnh và thêm vào hồ sơ bệnh án.
    Parameters:
        raw_diagnosis (str): tên bệnh nhập thô từ bác sĩ
        current_list (list): danh sách chẩn đoán hiện tại
    Returns:
        list: danh sách chẩn đoán đã cập nhật
    """
    # Chuẩn hóa chuỗi: bỏ khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()

    # Thêm nguyên vẹn chẩn đoán vào danh sách
    current_list.append(raw_diagnosis)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)
