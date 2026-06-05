"""
(1) Phân tích & Thiết kế Giải pháp
Input/Output cho từng hàm
display_students(student_list)

Input: danh sách học viên (list chứa dict).

Output: in ra màn hình danh sách hoặc thông báo trống.

validate_score(score_input)

Input: chuỗi nhập từ người dùng.

Output: True/False (hợp lệ hay không). Nếu hợp lệ có thể ép kiểu sang float.

add_student(student_list)

Input: danh sách học viên.

Output: thêm dict mới vào list, in thông báo thành công hoặc lỗi.

find_student_by_id(student_list, student_id)

Input: danh sách học viên, mã học viên.

Output: index hoặc dict học viên, nếu không thấy trả về None.

update_score(student_list)

Input: danh sách học viên.

Output: cập nhật điểm Toán/Anh cho học viên theo mã, in thông báo.

get_rank(average_score)

Input: điểm trung bình (float).

Output: chuỗi xếp loại ("Giỏi", "Khá", "Trung bình", "Yếu").

evaluate_students(student_list)

Input: danh sách học viên.

Output: in ra màn hình danh sách kèm điểm trung bình và xếp loại.

Lý do tách hàm
Dễ bảo trì: mỗi hàm chỉ làm một việc, dễ sửa lỗi.

Tái sử dụng: hàm phụ trợ như validate_score hay find_student_by_id có thể dùng lại ở nhiều chức năng.

Đọc hiểu tốt hơn: code ngắn gọn, rõ ràng, tránh spaghetti code.

Mở rộng dễ dàng: thêm chức năng mới không ảnh hưởng đến các hàm cũ.

"""

# (2) Triển khai Code Python
# =========================
# HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY
# =========================

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0,
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5,
    },
]


def display_students(student_list):
    """Hiển thị danh sách học viên"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
    else:
        for i, st in enumerate(student_list, start=1):
            print(
                f"{i}. Mã: {st['student_id']} | Tên: {st['name']} | Toán: {st['math_score']} | Anh: {st['english_score']}"
            )


def validate_score(score_input):
    """Kiểm tra điểm hợp lệ (0-10)"""
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return score
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
            return None
    except ValueError:
        print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
        return None


def find_student_by_id(student_list, student_id):
    """Tìm học viên theo mã"""
    for idx, st in enumerate(student_list):
        if st["student_id"] == student_id:
            return idx
    return None


def add_student(student_list):
    """Thêm học viên mới"""
    student_id = input("Nhập mã học viên: ").strip().upper()
    if find_student_by_id(student_list, student_id) is not None:
        print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        return

    name = input("Nhập tên học viên: ").strip().title()
    if not name:
        print("Tên học viên không được để trống!")
        return

    math_score = None
    while math_score is None:
        math_score = validate_score(input("Nhập điểm Toán: "))

    english_score = None
    while english_score is None:
        english_score = validate_score(input("Nhập điểm Anh: "))

    student_list.append(
        {
            "student_id": student_id,
            "name": name,
            "math_score": math_score,
            "english_score": english_score,
        }
    )
    print("Thêm học viên thành công!")


def update_score(student_list):
    """Cập nhật điểm thi theo mã học viên"""
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    idx = find_student_by_id(student_list, student_id)
    if idx is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    math_score = None
    while math_score is None:
        math_score = validate_score(input("Nhập điểm Toán mới: "))

    english_score = None
    while english_score is None:
        english_score = validate_score(input("Nhập điểm Anh mới: "))

    students[idx]["math_score"] = math_score
    students[idx]["english_score"] = english_score
    print("Cập nhật điểm thành công!")


def get_rank(average_score):
    """Xếp loại học lực theo điểm trung bình"""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def evaluate_students(student_list):
    """Đánh giá học lực toàn bộ học viên"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    for st in student_list:
        avg = (st["math_score"] + st["english_score"]) / 2
        rank = get_rank(avg)
        print(
            f"Mã: {st['student_id']} | Tên: {st['name']} | ĐTB: {avg:.2f} | Xếp loại: {rank}"
        )


def display_menu():
    """Hiển thị menu chính"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


# =========================
# Main Flow
# =========================
while True:
    display_menu()
    choice = input("Nhập lựa chọn (1-5): ").strip()

    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
