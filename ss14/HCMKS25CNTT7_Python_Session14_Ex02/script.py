"""
(1) Phân tích lỗi
Biến total_points ở dòng 2
Đây là biến toàn cục (Global) vì được khai báo bên ngoài mọi hàm. Nó có thể được đọc từ bất kỳ đâu trong chương trình.

Giải thích lỗi UnboundLocalError
Khi Python thấy dòng total_points = total_points + points_earned trong hàm, nó tự động coi total_points là một biến cục bộ mới (do có phép gán). Nhưng biến cục bộ này chưa được gán giá trị trước đó, nên khi tham chiếu đến total_points thì báo lỗi "referenced before assignment".

Nếu chỉ đọc (print) biến total_points trong hàm
Ví dụ: print(total_points) thì sẽ không lỗi, vì Python cho phép đọc biến toàn cục bên trong hàm miễn là không có phép gán.

Cách sửa 1 (dùng từ khóa)
Từ khóa global giúp Python hiểu rằng ta muốn dùng và thay đổi biến toàn cục.
Ví dụ:

python
def add_reward_points(points_earned):
    global total_points
    total_points = total_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
Cách sửa 2 (Clean code hơn)
Thay vì can thiệp trực tiếp vào biến toàn cục, ta viết hàm dạng pure function: nhận tổng điểm cũ và điểm mới làm tham số, sau đó return tổng điểm mới. Điều này giúp code dễ hiểu, ít lỗi ngầm.

"""


# (2) Sửa lỗi – Source Code chuẩn (Cách 2)
# Hàm cộng điểm thưởng (pure function)
def add_reward_points(current_points, points_earned):
    new_total = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return new_total


# Tổng điểm ban đầu của khách hàng
total_points = 100

# Khách mua hàng được thưởng 50 điểm
total_points = add_reward_points(total_points, 50)

# In ra kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)
