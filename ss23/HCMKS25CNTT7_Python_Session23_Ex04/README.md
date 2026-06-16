# HỆ THỐNG QUẢN LÝ TIỆN ÍCH HỌC TẬP - RIKKEI ACADEMY

## 1. Cấu trúc cây thư mục (Folder Tree)

```
rikkei_learning_tools/
├── main.py
├── data/
│   └── students.py
├── utils/
│   ├── init.py
│   ├── score_utils.py
│   ├── string_utils.py
│   └── random_utils.py
└── reports/
    ├── init.py
    └── report_generator.py
```

## 2. Thiết kế module và hàm

### Module `utils/score_utils.py`
- **Vai trò**: Xử lý điểm số.
- **Hàm chính**:
  - `calculate_average(scores)`: Tính điểm trung bình, bỏ qua giá trị không hợp lệ.
  - `classify_student(average)`: Phân loại học lực theo thang điểm.
- **Kiểu import**: `from utils.score_utils import calculate_average`

### Module `utils/string_utils.py`
- **Vai trò**: Chuẩn hóa chuỗi tên sinh viên.
- **Hàm chính**:
  - `normalize_student_names(records)`: Chuẩn hóa tên (strip, viết hoa chữ cái đầu).
- **Kiểu import**: `import utils.string_utils as s_utils`

### Module `utils/random_utils.py`
- **Vai trò**: Sinh mã bài tập ngẫu nhiên.
- **Hàm chính**:
  - `generate_assignment_code()`: Sinh mã theo định dạng `PY-XXXX`.
- **Kiểu import**: `from utils.random_utils import generate_assignment_code`

### Module `reports/report_generator.py`
- **Vai trò**: Hiển thị và xuất báo cáo học tập.
- **Hàm chính**:
  - `display_student_scores(records)`: Hiển thị danh sách sinh viên và điểm trung bình.
  - `export_learning_report(records)`: Xuất báo cáo ra file `.txt`.
- **Kiểu import**: `import reports.report_generator`

### Module `main.py`
- **Vai trò**: Menu điều hướng.
- **Hàm chính**:
  - `main()`: Vòng lặp `while True`, gọi các chức năng từ module khác.

---

## 3. Phân tích hàm nghiệp vụ

### `calculate_average(scores)`
- **Input**: Danh sách điểm (list).
- **Output**: Điểm trung bình (float).
- **Module**: `utils/score_utils.py`
- **Luồng xử lý**:
  - Lọc bỏ giá trị không hợp lệ.
  - Nếu danh sách rỗng → trả về 0.
  - Tính tổng / số lượng.

### `classify_student(average)`
- **Input**: Điểm trung bình (float).
- **Output**: Chuỗi phân loại.
- **Module**: `utils/score_utils.py`
- **Luồng xử lý**: So sánh theo thang điểm (Giỏi, Khá, Trung bình, Yếu).

### `display_student_scores(records)`
- **Input**: Danh sách sinh viên.
- **Output**: In ra terminal.
- **Module**: `reports/report_generator.py`
- **Luồng xử lý**: Duyệt danh sách, gọi `calculate_average`, `classify_student`, in kết quả.

### `normalize_student_names(records)`
- **Input**: Danh sách sinh viên.
- **Output**: In tên đã chuẩn hóa.
- **Module**: `utils/string_utils.py`
- **Luồng xử lý**: Strip, split, capitalize từng từ.

### `generate_assignment_code()`
- **Input**: Không.
- **Output**: Chuỗi mã ngẫu nhiên.
- **Module**: `utils/random_utils.py`
- **Luồng xử lý**: Dùng `random` + `string` để sinh 4 ký tự, ghép với tiền tố `PY-`.

### `export_learning_report(records)`
- **Input**: Danh sách sinh viên.
- **Output**: File `learning_report.txt`.
- **Module**: `reports/report_generator.py`
- **Luồng xử lý**: Tính tổng số SV, số đạt yêu cầu, số cần cải thiện. Ghi file với thời gian tạo bằng `datetime`. In thông báo thành công bằng `colorama`.

### `main()`
- **Input**: Người dùng nhập lựa chọn menu.
- **Output**: Gọi các chức năng tương ứng.
- **Module**: `main.py`
- **Luồng xử lý**: Vòng lặp `while True`, bẫy lỗi nhập sai, gọi hàm từ các module.

---

## 4. Import và Module sử dụng

- **Module chuẩn**: `random`, `string`, `datetime`.
- **Third-party module**: `colorama`.
- **Kiểu import**:
  - `import module`
  - `from module import function`
  - `import module as alias`

---

## 5. Edge Cases xử lý

- **Danh sách sinh viên rỗng**: In thông báo, không lỗi.
- **Danh sách điểm rỗng**: ĐTB = 0.
- **Điểm không hợp lệ**: Bỏ qua khi tính trung bình.
- **Sai chức năng menu**: In thông báo, không crash.

---
