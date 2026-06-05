"""
(1) Thiết kế Hàm
Để hệ thống rõ ràng, ta chia nhỏ thành các hàm sau:

Hàm phụ trợ: calculate_average(student)
Input: student (dictionary chứa điểm Toán, Lý, Hóa).

Output: float (điểm trung bình).

Pseudocode:

avg = (student["math"] + student["physics"] + student["chemistry"]) / 3
return avg
Hàm 1: display_grades(records)
Input: records (list các dictionary).

Output: In ra bảng điểm, không trả về giá trị.

Pseudocode:

if records rỗng: in "Hệ thống chưa có dữ liệu sinh viên."
else:
    duyệt từng student:
        avg = calculate_average(student)
        rank = get_rank(avg)
        in thông tin + ĐTB + rank
Hàm phụ trợ: get_rank(average_score)
Input: average_score (float).

Output: Chuỗi xếp loại ("Giỏi", "Khá", "Trung bình", "Yếu").

Pseudocode:

if avg >= 8.0: return "Giỏi"
elif avg >= 6.5: return "Khá"
elif avg >= 5.0: return "Trung bình"
else: return "Yếu"
Hàm 2: update_student_score(records)
Input: records.

Output: Cập nhật điểm trong list, in thông báo.

Pseudocode:

nhập student_id, chuẩn hóa (strip, upper)
tìm student bằng find_student_by_id
nếu không thấy: in lỗi
nếu thấy:
    nhập lựa chọn môn (1-3)
    nhập điểm mới, validate_score
    cập nhật vào dict
    in thông báo thành công
Hàm phụ trợ: validate_score(score_input)
Input: chuỗi nhập.

Output: float hợp lệ hoặc None.

Pseudocode:

try convert float
if 0 <= score <= 10: return score
else: in lỗi, return None
except ValueError: in lỗi, return None
Hàm 3: generate_report(records)
Input: records.

Output: In báo cáo thống kê.

Pseudocode:

if records rỗng: in "Hệ thống chưa có dữ liệu sinh viên."
else:
    total = len(records)
    pass_count = số sinh viên avg >= 5
    fail_count = total - pass_count
    tính % và in báo cáo
Hàm 4: find_valedictorian(records)
Input: records.

Output: In thông tin thủ khoa.

Pseudocode:

if records rỗng: in "Hệ thống chưa có dữ liệu sinh viên."
else:
    tìm student có avg cao nhất
    in thông tin thủ khoa

"""

# (2) Triển khai Code

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0,
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5,
    },
]


def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def get_rank(avg):
    if avg >= 8.0:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for i, st in enumerate(records, start=1):
        avg = calculate_average(st)
        rank = get_rank(avg)
        print(
            f"{i}. [{st['student_id']}] {st['name']} | Toán: {st['math']} | Lý: {st['physics']} | Hóa: {st['chemistry']} | ĐTB: {avg:.2f} - {rank}"
        )
    print("---------------------------")


def validate_score(score_input):
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return score
        else:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
            return None
    except ValueError:
        print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        return None


def find_student_by_id(records, student_id):
    for idx, st in enumerate(records):
        if st["student_id"] == student_id:
            return idx
    return None


def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    idx = find_student_by_id(records, student_id)
    if idx is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
    print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ")
    choice = input().strip()
    subject_map = {"1": "math", "2": "physics", "3": "chemistry"}
    if choice not in subject_map:
        print("Lựa chọn môn học không hợp lệ!")
        return
    new_score = None
    while new_score is None:
        new_score = validate_score(input("Nhập điểm mới: "))
    records[idx][subject_map[choice]] = new_score
    print(
        f">> Đã cập nhật điểm {subject_map[choice].capitalize()} của sinh viên '{records[idx]['name']}' thành {new_score}."
    )


def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    pass_count = sum(1 for st in records if calculate_average(st) >= 5.0)
    fail_count = total - pass_count
    pass_rate = (pass_count / total) * 100
    fail_rate = (fail_count / total) * 100
    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_rate:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_rate:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    best_student = max(records, key=lambda st: calculate_average(st))
    avg = calculate_average(best_student)
    print("--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {best_student['name']} (Mã: {best_student['student_id']})")
    print(f" Điểm Trung Bình: {avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")


def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")


def main():
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        if choice == "1":
            display_grades(student_records)
        elif choice == "2":
            update_student_score(student_records)
        elif choice == "3":
            generate_report(student_records)
        elif choice == "4":
            find_valedictorian(student_records)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
