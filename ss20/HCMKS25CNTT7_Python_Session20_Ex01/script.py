"""
(1) Phân tích lỗi (Code Review)
Vì sao xuất hiện ZeroDivisionError?
Khi xử lý ShowMaker, số lần bị hạ gục (Deaths) = 0. Công thức KDA là
(
𝐾
𝑖
𝑙
𝑙
𝑠
+
𝐴
𝑠
𝑠
𝑖
𝑠
𝑡
𝑠
)
/
𝐷
𝑒
𝑎
𝑡
ℎ
𝑠
. Phép chia cho 0 trong Python gây ra lỗi ZeroDivisionError: division by zero, làm chương trình sập ngay lập tức.

Nếu xóa ShowMaker, lỗi khi xử lý Chovy là gì?
API trả về chuỗi "ba" thay vì số. Khi gọi int("ba"), Python không thể ép kiểu sang số nguyên, dẫn đến lỗi ValueError: invalid literal for int() with base 10: 'ba'.

Đánh giá cách đặt tên biến ds, x, n, k, d, a:
Đây là tên viết tắt, khó hiểu, không tự giải thích. Theo chuẩn Clean Code, nên đổi thành:

ds → player_stats_list

x → player_stats

n → name

k → kills

d → deaths

a → assists

Lợi ích của việc tách hàm calculate_kda:

Giúp code tái sử dụng (DRY – không lặp lại logic).

Dễ dàng test riêng biệt hàm tính toán.

Code trở nên modular, dễ bảo trì và mở rộng.

Giảm độ phức tạp của hàm chính, tăng tính dễ đọc.


"""

# (2) Sửa Refactoring & Exception Handling
# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),  # Bình thường
    ("ShowMaker", "15", "0", "10"),  # Deaths = 0
    ("Chovy", "12", "ba", "5"),  # Lỗi dữ liệu
]


def calculate_kda(kills, deaths, assists):
    """Hàm tính toán KDA"""
    return (kills + assists) / deaths


def process_player_stats(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for player_stats in player_stats_list:
        name, kills_str, deaths_str, assists_str = player_stats

        try:
            kills = int(kills_str)
            deaths = int(deaths_str)
            assists = int(assists_str)

            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.1f}")

        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")

    print("--- HOÀN TẤT ---")


# Chạy hệ thống
process_player_stats(data)
