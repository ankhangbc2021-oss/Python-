"""
Rikkei RPG - LÒ RÈN VŨ KHÍ (Blacksmith System)
Design notes (System Design Document)
------------------------------------
1) Equipment (Abstract Base Class)
   - Vai trò: khuôn mẫu cho mọi trang bị; không thể khởi tạo trực tiếp.
   - @abstractmethod calculate_total_damage() ép lớp con phải định nghĩa công thức sát thương.
   - Ngăn lỗi "quên override" khi dev thêm loại trang bị mới.

2) MagicMixin (Mixin)
   - Cung cấp thuộc tính phép thuật và hành vi phụ trợ (cast_glow).
   - Không kế thừa từ Equipment; dùng cùng Weapon qua đa kế thừa.

3) MagicSword (Multiple Inheritance)
   - MRO (đơn giản): MagicSword -> Weapon -> Equipment -> ABC -> object
     và MagicSword -> MagicMixin -> object (Mixin không can thiệp vào Equipment).
   - __init__ phải khởi tạo cả Weapon và MagicMixin (gọi Weapon.__init__ và MagicMixin.__init__).

4) Polymorphism
   - inventory chứa các đối tượng Equipment (Weapon, MagicSword).
   - Khi hiển thị kho, gọi item.calculate_total_damage() cho mọi item; Python chọn method phù hợp theo loại.

5) Operator Overloading (Weapon)
   - __gt__(self, other): so sánh sát thương tổng; kiểm tra isinstance(other, Equipment).
   - __add__(self, other): dung hợp hai trang bị -> trả về Weapon mới.
     Pseudocode:
       if not isinstance(other, Equipment): raise TypeError(...)
       new_name = f"Fusion({self.name} + {other.name})"
       new_base = self.base_damage + other.base_damage
       new_level = self.upgrade_level + other.upgrade_level
       return Weapon(new_name, new_base, new_level)
   - Các magic method phải xử lý edge cases và trả về lỗi rõ ràng nếu tham số không hợp lệ.

6) Edge cases xử lý
   - Không thể khởi tạo Equipment trực tiếp (ABC).
   - Giá trị base_damage, upgrade_level, magic_power phải > 0; nếu không, báo lỗi và không tạo.
   - Khi __add__ hoặc __gt__ nhận tham số không phải Equipment -> raise TypeError với thông báo tiếng Việt.
   - Khi dung hợp, kết quả luôn là một đối tượng Weapon (không phải MagicSword).

File này chứa cả phần thiết kế ngắn và code thực thi CLI.
"""

from abc import ABC, abstractmethod


# ===== LỚP TRỪU TƯỢNG =====
class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        """Trả về sát thương tổng (int/float)."""
        pass


# ===== LỚP VŨ KHÍ VẬT LÝ =====
class Weapon(Equipment):
    def __init__(self, name: str, base_damage: int, upgrade_level: int = 0):
        # Validate inputs
        if base_damage <= 0:
            raise ValueError("Giá trị phải lớn hơn 0!")
        if upgrade_level < 0:
            raise ValueError("Giá trị phải lớn hơn hoặc bằng 0!")
        self.name = name.title()
        self.base_damage = int(base_damage)
        self.upgrade_level = int(upgrade_level)

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể so sánh giữa các trang bị!")
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp giữa các trang bị!")
        # Lấy base_damage và upgrade_level từ other (MagicSword cũng có)
        try:
            other_base = other.base_damage
            other_level = other.upgrade_level
        except AttributeError:
            raise TypeError("Thiếu thuộc tính cần thiết để dung hợp!")
        new_name = f"Fusion({self.name} + {other.name})"
        new_base_damage = self.base_damage + other_base
        new_upgrade_level = self.upgrade_level + other_level
        # Trả về Weapon mới (không phải MagicSword)
        return Weapon(new_name, new_base_damage, new_upgrade_level)


# ===== MIXIN PHÉP THUẬT =====
class MagicMixin:
    def __init__(self, magic_power: int):
        if magic_power <= 0:
            raise ValueError("Giá trị phải lớn hơn 0!")
        self.magic_power = int(magic_power)

    def cast_glow(self):
        print(f"✨ {self.name} phát sáng nhờ sức mạnh phép thuật!")


# ===== KIẾM MA THUẬT (ĐA KẾ THỪA) =====
class MagicSword(Weapon, MagicMixin):
    def __init__(
        self, name: str, base_damage: int, upgrade_level: int, magic_power: int
    ):
        # Gọi khởi tạo Weapon và MagicMixin rõ ràng để đảm bảo thuộc tính đầy đủ
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10 + self.magic_power


# ===== KHO VŨ KHÍ (inventory) =====
inventory = [
    # Mẫu khởi tạo ban đầu (để dễ test)
    Weapon("Iron Sword", 100, 2),  # sát thương: 100 + 2*10 = 120
    MagicSword("Flame Saber", 120, 3, 80),  # sát thương: 120 + 3*10 + 80 = 230
]


# ===== HÀM TIỆN ÍCH =====
def print_inventory():
    print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
        return
    print("STT | Tên vũ khí                | Loại        | Cấp | Sát thương tổng")
    print("-" * 72)
    for idx, item in enumerate(inventory, 1):
        item_type = type(item).__name__
        dmg = item.calculate_total_damage()
        print(
            f"{idx:<3} | {item.name:<25} | {item_type:<11} | {item.upgrade_level:<3} | {dmg}"
        )
    print("-" * 72)


def craft_weapon():
    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")
    try:
        name = input("Nhập tên vũ khí: ").strip()
        if not name:
            print("Tên vũ khí không được để trống!")
            return
        base = int(input("Nhập sát thương gốc: ").strip())
        level = int(input("Nhập cấp cường hóa: ").strip())
        if base <= 0:
            print("Giá trị phải lớn hơn 0!")
            return
        if level < 0:
            print("Giá trị phải lớn hơn hoặc bằng 0!")
            return
        w = Weapon(name, base, level)
        inventory.append(w)
        print("\n>> Rèn vũ khí vật lý thành công!")
        print(f"Tên vũ khí: {w.name}")
        print("Loại: Weapon")
        print(f"Cấp cường hóa: {w.upgrade_level}")
        print(f"Sát thương tổng: {w.calculate_total_damage()}")
    except ValueError:
        print("Giá trị nhập không hợp lệ. Vui lòng nhập số nguyên hợp lệ.")


def craft_magic_sword():
    print("\n--- RÈN KIẾM MA THUẬT ---")
    try:
        name = input("Nhập tên kiếm ma thuật: ").strip()
        if not name:
            print("Tên kiếm không được để trống!")
            return
        base = int(input("Nhập sát thương gốc: ").strip())
        level = int(input("Nhập cấp cường hóa: ").strip())
        magic = int(input("Nhập sức mạnh phép thuật: ").strip())
        if base <= 0 or level < 0 or magic <= 0:
            print("Giá trị phải lớn hơn 0 (cấp có thể bằng 0 cho upgrade_level).")
            return
        ms = MagicSword(name, base, level, magic)
        inventory.append(ms)
        print("\n>> Rèn kiếm ma thuật thành công!")
        print(f"Tên vũ khí: {ms.name}")
        print("Loại: MagicSword")
        print(f"Cấp cường hóa: {ms.upgrade_level}")
        print(f"Sát thương gốc: {ms.base_damage}")
        print(f"Sức mạnh phép thuật: {ms.magic_power}")
        print(f"Sát thương tổng: {ms.calculate_total_damage()}")
        print("\nGiải thích phép tính:")
        phys = ms.base_damage + ms.upgrade_level * 10
        print(
            f"Sát thương vật lý = {ms.base_damage} + {ms.upgrade_level} * 10 = {phys}"
        )
        print(f"Sát thương phép  = {ms.magic_power}")
        print(
            f"Sát thương tổng = {phys} + {ms.magic_power} = {ms.calculate_total_damage()}"
        )
    except ValueError:
        print("Giá trị nhập không hợp lệ. Vui lòng nhập số nguyên hợp lệ.")


def appraise_weapons():
    print("\n--- THẨM ĐỊNH VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
        return
    w1 = inventory[0]
    w2 = inventory[1]
    print("Vũ khí thứ nhất:")
    print(
        f"{w1.name} | Loại: {type(w1).__name__} | Sát thương: {w1.calculate_total_damage()}"
    )
    print("\nVũ khí thứ hai:")
    print(
        f"{w2.name} | Loại: {type(w2).__name__} | Sát thương: {w2.calculate_total_damage()}"
    )
    try:
        if w1 > w2:
            print(f"\nKết quả: {w1.name} mạnh hơn {w2.name}.")
        elif w2 > w1:
            print(f"\nKết quả: {w2.name} mạnh hơn {w1.name}.")
        else:
            print("\nKết quả: Hai vũ khí có sức mạnh ngang nhau.")
    except TypeError as e:
        print(e)


def fuse_weapons():
    print("\n--- DUNG HỢP VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
        return
    w1 = inventory.pop(0)
    w2 = inventory.pop(0)
    print("Đang dung hợp 2 vũ khí đầu tiên trong kho...")
    print(
        f"\nVũ khí 1: {w1.name} | Cấp: {w1.upgrade_level} | Sát thương: {w1.calculate_total_damage()}"
    )
    print(
        f"Vũ khí 2: {w2.name} | Cấp: {w2.upgrade_level} | Sát thương: {w2.calculate_total_damage()}"
    )
    try:
        new_weapon = w1 + w2  # __add__ trả về Weapon mới
        print("\n>> Dung hợp vũ khí thành công!")
        print(f"Đã xóa khỏi kho: {w1.name}")
        print(f"Đã xóa khỏi kho: {w2.name}")
        inventory.insert(0, new_weapon)  # thêm vào đầu kho
        print(f"\nVũ khí mới: {new_weapon.name}")
        print("Loại: Weapon")
        print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
        print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
        # Giải thích
        new_base = new_weapon.base_damage
        new_level = new_weapon.upgrade_level
        print("\nGiải thích:")
        print(f"Base damage mới = {w1.base_damage} + {w2.base_damage} = {new_base}")
        print(
            f"Cấp cường hóa mới = {w1.upgrade_level} + {w2.upgrade_level} = {new_level}"
        )
        print(
            f"Sát thương tổng = {new_base} + {new_level} * 10 = {new_weapon.calculate_total_damage()}"
        )
    except TypeError as e:
        print(e)
        # Nếu lỗi, trả 2 vũ khí về kho (ở cuối)
        inventory.insert(0, w2)
        inventory.insert(0, w1)


def main_menu():
    while True:
        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS ===================")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý (Tạo Weapon)")
        print("3. Rèn Kiếm Ma Thuật (Tạo MagicSword)")
        print("4. Thẩm định vũ khí (So sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")
        print("======================================================")
        choice = input("Chọn chức năng (1-6): ").strip()
        if choice == "1":
            print_inventory()
        elif choice == "2":
            craft_weapon()
        elif choice == "3":
            craft_magic_sword()
        elif choice == "4":
            appraise_weapons()
        elif choice == "5":
            fuse_weapons()
        elif choice == "6":
            print("\nThoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại (1-6).")


if __name__ == "__main__":
    main_menu()
