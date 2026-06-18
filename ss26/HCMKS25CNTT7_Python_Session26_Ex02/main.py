"""
(1) Phân tích lỗi (Code Review)
Đa hình (Polymorphism):
Vòng lặp for hero in team_heroes: hero.use_ultimate() cho thấy tính đa hình vì cùng một lời gọi use_ultimate() nhưng hành vi thực tế phụ thuộc vào lớp con cụ thể. Mage tung chiêu “Mưa Sao Băng”, Assassin lẽ ra phải tung “Ám Sát”. Python không cần biết kiểu cụ thể, chỉ cần biết rằng mọi đối tượng đều có phương thức use_ultimate().

Lỗi NotImplementedError xuất hiện khi nào:
Với code cũ, đối tượng Assassin vẫn được tạo ra bình thường và thêm vào danh sách. Lỗi chỉ phát sinh tại thời điểm giao tranh khi hệ thống gọi hero.use_ultimate(). Đây là báo lỗi muộn (runtime error), gây thảm họa vì người chơi đã vào trận, game đang chạy thì mới sập.

Nếu dùng abc và @abstractmethod:
Khi lớp Assassin không ghi đè use_ultimate(), lỗi sẽ văng ngay lúc khởi tạo đối tượng (tức là ở giai đoạn loading trận đấu). Python không cho phép tạo instance từ lớp con chưa triển khai đầy đủ các phương thức trừu tượng.

Nguyên lý Fail Fast:
Abstract Base Class ép buộc lớp con phải định nghĩa đầy đủ các phương thức cần thiết. Nhờ đó, lỗi được phát hiện sớm (ngay khi khởi tạo), thay vì để đến lúc chạy thực tế mới văng. Điều này giúp hệ thống ổn định hơn và trải nghiệm người chơi không bị gián đoạn.

(2) Sửa lỗi (Refactoring)
"""

from abc import ABC, abstractmethod


# Lớp cha: Khuôn mẫu Tướng
class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        pass


# Lớp con 1: Pháp Sư
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Lớp con 2: Sát Thủ
class Assassin(Hero):
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# --- KỊCH BẢN CHUẨN ---
print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()]
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()
