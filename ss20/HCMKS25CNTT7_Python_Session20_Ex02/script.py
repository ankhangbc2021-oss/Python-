"""
(1) Phân tích lỗi (Code Review)
Lỗi IndexError: tuple index out of range ở dòng r = p[2]:  
Với Levi, tuple có đủ 3 phần tử (Tên, Số trận, MMR) nên việc truy cập p[2] hợp lệ. Nhưng với SofM, tuple chỉ có 2 phần tử (Tên, Số trận). Khi chương trình cố lấy phần tử thứ 3 (p[2]), Python báo lỗi vì vượt quá phạm vi mảng.

Nếu sửa SofM thành dữ liệu chuẩn, lỗi tiếp theo ở Optimus:  
Optimus có MMR = "N/A". Khi chương trình gọi int("N/A"), Python không thể ép kiểu chuỗi "N/A" sang số nguyên. Lúc này sẽ phát sinh lỗi ValueError: invalid literal for int() with base 10: 'N/A'.

Kỹ năng Debug với print("Đang xử lý:", p):  
Lệnh này giúp ta biết chương trình đang xử lý hồ sơ nào trước khi sập. Nhờ đó, ta xác định được bản ghi gây lỗi (ví dụ: thấy đang xử lý SofM thì lỗi là do thiếu dữ liệu).

Đánh giá tên biến ds, p, t, m, r, b:  
Đây là tên viết tắt, khó hiểu. Theo chuẩn Clean Code, nên đổi thành:

ds → player_records
p → record
t → name
m → matches
r → mmr
b → bonus
"""

# (2) Refactoring & Exception Handling
# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: thiếu MMR
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: MMR không hợp lệ
]

def calculate_bonus(matches, mmr):
    """Hàm tính tiền thưởng RP"""
    return (matches * 10) + (mmr * 0.5)

def process_player_records(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in player_records:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]

            bonus = calculate_bonus(matches, int(mmr))
            print(f"Tuyển thủ {name} nhận được {bonus:.1f} RP")

        except IndexError:
            print(f"Tuyển thủ {record[0]}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            print(f"Tuyển thủ {record[0]}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
process_player_records(data)
