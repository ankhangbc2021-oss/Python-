"""
(1) Phân tích & Thiết kế Giải pháp
Sơ đồ cấu trúc kế thừa

Champion (ABC)
   ├── Warrior (Concrete Class)
   └── Mage (Concrete Class)
Champion: Lớp trừu tượng, không thể khởi tạo trực tiếp.

Warrior, Mage: Lớp con cụ thể, kế thừa thuộc tính chung và tự định nghĩa kỹ năng riêng.

Phân tích Đa hình (Polymorphism)
Hàm calculate_skill_damage() được định nghĩa trừu tượng trong Champion.

Mỗi lớp con (Warrior, Mage) ghi đè theo cách riêng:

Warrior: dựa trên giáp cộng thêm.

Mage: dựa trên hệ số phép thuật.

Khi hệ thống gọi champion.calculate_skill_damage(), Python tự động chọn đúng phiên bản theo loại tướng.

Lợi ích: dễ mở rộng. Nếu sau này thêm Assassin, Ranger, chỉ cần định nghĩa lại calculate_skill_damage() mà không phải sửa code vòng lặp.

Phân tích Nạp chồng toán tử
__add__: Cho phép cộng hai đối tượng Champion → trả về tổng chiến lực.

Nếu cộng với số (int hoặc float), thì trả về combat_power + số.

Điều này giúp dễ dàng tính tổng đội hình bằng cách khởi tạo từ 0.

__gt__: Cho phép so sánh hai Champion bằng toán tử > dựa trên combat_power.

(2) Refactoring Source Code
"""

from abc import ABC, abstractmethod


# ===== LỚP TRỪU TƯỢNG =====
class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented


# ===== LỚP CON =====
class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


# ===== BỂ TƯỚNG BAN ĐẦU =====
champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 1.5),
]


# ===== CHỨC NĂNG =====
def display_champion_pool():
    print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    print(
        "Mã     | Tên tướng          | Hệ       | HP    | ATK   | Chỉ số riêng    | Chiến lực"
    )
    print("-" * 100)
    for champ in champion_pool:
        if isinstance(champ, Warrior):
            extra = f"Armor: {champ.shield_bonus}"
            system = "Warrior"
        elif isinstance(champ, Mage):
            extra = f"AP: {champ.ability_power}"
            system = "Mage"
        print(
            f"{champ.champion_id:<6} | {champ.name:<18} | {system:<8} | {champ.base_hp:<5} | {champ.base_atk:<5} | {extra:<15} | {int(champ.get_combat_power())}"
        )
    print("-" * 100)


def add_champion():
    system_choice = input("Chọn hệ (1 - Warrior, 2 - Mage): ")
    champ_id = input("Nhập mã tướng: ")
    if any(c.champion_id == champ_id for c in champion_pool):
        print(f"Mã tướng {champ_id} đã tồn tại, không thể thêm!")
        return

    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))

    if system_choice == "1":
        shield = int(input("Nhập Armor: "))
        new_champ = Warrior(champ_id, name, hp, atk, shield)
    elif system_choice == "2":
        ap = float(input("Nhập Ability Power: "))
        new_champ = Mage(champ_id, name, hp, atk, ap)
    else:
        print("Hệ không hợp lệ!")
        return

    champion_pool.append(new_champ)
    print(f"Thêm tướng {name} thành công!")
    print(
        f"Mã: {champ_id} | Tên: {name} | Chiến lực: {int(new_champ.get_combat_power())}"
    )


def compare_champions():
    id1 = input("Nhập mã tướng thứ nhất: ")
    id2 = input("Nhập mã tướng thứ hai: ")
    champ1 = next((c for c in champion_pool if c.champion_id == id1), None)
    champ2 = next((c for c in champion_pool if c.champion_id == id2), None)

    if not champ1:
        print(f"Mã tướng {id1} không hợp lệ, bỏ qua!")
        return
    if not champ2:
        print(f"Mã tướng {id2} không hợp lệ, bỏ qua!")
        return

    print("Thông tin so sánh:")
    print(
        f"{champ1.champion_id} - {champ1.name} | Chiến lực: {int(champ1.get_combat_power())}"
    )
    print(
        f"{champ2.champion_id} - {champ2.name} | Chiến lực: {int(champ2.get_combat_power())}"
    )

    if champ1 > champ2:
        print(
            f"Kết quả: {champ1.champion_id} - {champ1.name} mạnh hơn {champ2.champion_id} - {champ2.name}."
        )
    else:
        print(
            f"Kết quả: {champ2.champion_id} - {champ2.name} mạnh hơn hoặc bằng {champ1.champion_id} - {champ1.name}."
        )


def calculate_team_power():
    ids = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ").split(",")
    total_power = 0
    print("Danh sách đội hình:")
    for i, champ_id in enumerate(ids, 1):
        champ_id = champ_id.strip()
        champ = next((c for c in champion_pool if c.champion_id == champ_id), None)
        if champ:
            print(
                f"{i}. {champ.champion_id} - {champ.name} | Chiến lực: {int(champ.get_combat_power())}"
            )
            total_power = champ + total_power
        else:
            print(f"Mã tướng {champ_id} không hợp lệ, bỏ qua!")
    print(f"Tổng chiến lực đội hình: {int(total_power)}")


# ===== MENU CHÍNH =====
def main():
    while True:
        print("\n--- MENU AUTO-BATTLER ---")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát chương trình")
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_champion_pool()
        elif choice == "2":
            add_champion()
        elif choice == "3":
            compare_champions()
        elif choice == "4":
            calculate_team_power()
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


if __name__ == "__main__":
    main()
