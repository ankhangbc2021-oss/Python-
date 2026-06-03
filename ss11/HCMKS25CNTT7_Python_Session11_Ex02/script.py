"""
(1) Phân tích lỗi
Dictionary employee gồm những key nào?  
→ "employee_id", "full_name", "department", "status"

Vì sao dòng sau gây lỗi?

employee_id = employee[0]
→ Dictionary không truy cập bằng index số, mà phải dùng key. Key 0 không tồn tại nên gây KeyError.

Dictionary có truy cập phần tử bằng index giống list không?  
→ Không. Dictionary chỉ truy cập bằng key.

Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?

employee_id = employee["employee_id"]
Vì sao dòng sau gây lỗi?

full_name = employee["name"]
→ Key "name" không tồn tại. Key đúng là "full_name".

Key đúng để lấy họ tên nhân viên là gì?  
→ "full_name"

Vì sao dòng sau chưa cập nhật đúng trạng thái nhân viên?

employee["employee_status"] = "official"
→ Key "employee_status" không tồn tại. Trạng thái nhân viên đang lưu ở key "status".

Muốn cập nhật trạng thái nhân viên, cần dùng key nào?  
→ "status"

Vì sao dòng sau gây lỗi?

employee.append("base_salary", 15000000)
→ Dictionary không có phương thức .append(). Đây là phương thức của list.

Dictionary có phương thức append() không?  
→ Không.

Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?

employee["base_salary"] = 15000000
Vì sao dòng sau gây lỗi?

del employee["team"]
→ Key "team" không tồn tại. Phòng ban được lưu bằng key "department".

Muốn xóa thông tin phòng ban, cần dùng key nào?  
→ "department"

(2) Sửa lỗi – Source Code chuẩn
"""

# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa phòng ban
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)