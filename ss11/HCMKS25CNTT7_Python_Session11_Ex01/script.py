"""
(1) Phân tích lỗi
Tuple product_info ban đầu có bao nhiêu phần tử?
→ Có 4 phần tử: "SP001", "Áo polo nam", "Size L", 299000.

Phần tử "SP001" đang nằm ở index nào?
→ Nằm ở index 0 (phần tử đầu tiên).

Vì sao dòng sau lấy sai mã sản phẩm?


product_code = product_info[1]
→ Index 1 là "Áo polo nam", không phải mã sản phẩm. Mã sản phẩm phải lấy ở index 0.

Phần tử "Áo polo nam" đang nằm ở index nào?
→ Nằm ở index 1.

Vì sao dòng sau lấy sai tên sản phẩm?


product_name = product_info[2]
→ Index 2 là "Size L", không phải tên sản phẩm. Tên sản phẩm phải lấy ở index 1.

Vì sao dòng sau gây lỗi?


product_length = product_info.length()
→ Tuple không có phương thức .length(). Python dùng hàm len() để đếm số phần tử.

Muốn đếm số phần tử trong tuple, cần dùng hàm nào?
→ Dùng len(product_info).

Vì sao dòng sau không hợp lệ?


product_info[3] = 279000
→ Vì tuple là immutable (không thể thay đổi trực tiếp phần tử).

Tuple có cho phép sửa trực tiếp phần tử không?
→ Không cho phép.

Muốn cập nhật giá bán từ 299000 thành 279000, cần xử lý như thế nào?
→ Tạo một tuple mới với giá trị đã thay đổi, ví dụ:


updated_product_info = (product_info[0], product_info[1], product_info[2], 279000)
(2) Sửa lỗi – Source Code chuẩn
"""

# code sửa

# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Tạo tuple mới sau khi cập nhật giá bán
product_info = (product_info[0], product_info[1], product_info[2], 279000)

# Hiển thị kết quả
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)
