"""
(1) Phân tích lỗi
Vì sao new_prescription.append("Oresol") làm thay đổi cả yesterday_prescription?
Vì dòng new_prescription = old_prescription không tạo ra một bản sao mới, mà chỉ tạo thêm một “nhãn” trỏ đến cùng vùng nhớ của list gốc. Do đó, mọi thay đổi trên new_prescription cũng tác động trực tiếp lên old_prescription.
Cách tạo bản sao độc lập của List:
Có nhiều cách, ví dụ:
Dùng cú pháp cắt (slice): new_prescription = old_prescription[:]
Dùng hàm list(): new_prescription = list(old_prescription)
Dùng copy() hoặc copy.deepcopy() từ module copy (đặc biệt hữu ích với list lồng nhau).
Vì sao new_prescription[0].replace("Panadol", "Paracetamol") không có tác dụng?
Vì .replace() trả về một chuỗi mới, nhưng lập trình viên không gán lại chuỗi đó vào phần tử list. Do đó, giá trị trong list vẫn giữ nguyên.
Cú pháp đúng để cập nhật phần tử:
new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

"""

# (2) Sửa lỗi – Source Code đúng chuẩn
# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    """
    Tạo bản sao đơn thuốc từ ngày hôm qua và cập nhật cho ngày hôm nay.
    - Đổi tên 'Panadol' thành 'Paracetamol'
    - Thêm 'Oresol' vào cuối danh sách
    Parameters:
        old_prescription (list): đơn thuốc ngày hôm qua
    Returns:
        list: đơn thuốc ngày hôm nay đã cập nhật
    """
    # Tạo bản sao độc lập để không ảnh hưởng đến list gốc
    new_prescription = old_prescription[:]

    # Đổi tên thuốc ở vị trí đầu tiên
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")

    return new_prescription

# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
