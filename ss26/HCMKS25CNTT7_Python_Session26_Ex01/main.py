"""
(1) Phân tích lỗi (Code Review)
Lỗi AttributeError tại dòng print(f"Chiến binh {w1.name}..."):
Trong lớp Warrior, lập trình viên chỉ gán self.bonus_armor mà không gọi hàm khởi tạo của lớp cha (Character). Do đó, các thuộc tính name, hp, attack_power không được khởi tạo, dẫn đến việc đối tượng Warrior không có thuộc tính name.

Thiếu cú pháp trong hàm __init__:
Cần gọi super().__init__(name, hp, attack_power) để kế thừa và khởi tạo các thuộc tính từ lớp cha.

Cách khác (không khuyến khích) để gọi hàm khởi tạo của lớp cha:
Có thể gọi trực tiếp Character.__init__(self, name, hp, attack_power). Tuy nhiên, cách này ít được dùng vì làm mất tính linh hoạt khi thay đổi cấu trúc kế thừa.

Lỗi khi chạy đến dòng if w1 > w2::
Console sẽ báo lỗi TypeError: '>' not supported between instances of 'Warrior' and 'Warrior'. Nguyên nhân: Python không biết cách so sánh 2 đối tượng tự định nghĩa nếu không có quy tắc so sánh (operator overloading).

Dunder method cần khai báo:
Phải định nghĩa __gt__(self, other) trong lớp Warrior. Hàm này nhận 2 tham số: self và other. Nó trả về True hoặc False dựa trên tiêu chí so sánh (ở đây là get_total_power()).

(2) Sửa lỗi (Refactoring)
"""


# Lớp cha: Nhân vật cơ bản
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


# Lớp con: Chiến binh cận chiến
class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        # Gọi hàm khởi tạo lớp cha
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    # Nạp chồng toán tử >
    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


# --- KỊCH BẢN MATCHMAKING CHUẨN ---
# Tạo 2 đối tượng chiến binh
w1 = Warrior("Arthur", 1000, 150, 50)  # Sức mạnh tổng: 200
w2 = Warrior("Lancelot", 900, 180, 10)  # Sức mạnh tổng: 190

# In thông báo xuất trận
print(f"Chiến binh {w1.name} xuất trận!")

# So sánh sức mạnh bằng toán tử >
if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")
