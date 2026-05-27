# (1) Phân tích & Thiết kế Giải Pháp
# Input
# Số lượng phòng học: số nguyên (int).

# Số hàng ghế của từng phòng: số nguyên (int).

# Số ghế trên mỗi hàng: số nguyên (int).

# Output
# Nếu dữ liệu hợp lệ: in sơ đồ chỗ ngồi bằng dấu * theo đúng số hàng và số ghế.

# Nếu dữ liệu không hợp lệ: in thông báo theo từng bẫy (edge case).

# Edge Cases
# Số lượng phòng ≤ 0 → In "Số lượng phòng học không hợp lệ" và kết thúc chương trình.

# Số hàng hoặc số ghế ≤ 0 → In "Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này" và bỏ qua phòng đó.

# Số hàng hoặc số ghế > 10 → In "Phòng quá lớn. Dừng nhập dữ liệu" và kết thúc chương trình.

# Giải pháp
# Dùng vòng lặp for để duyệt qua từng phòng học.

# Với mỗi phòng:

# Kiểm tra dữ liệu nhập (số hàng, số ghế).

# Nếu hợp lệ → in sơ đồ bằng vòng lặp lồng nhau (for hàng, for ghế).

# Nếu không hợp lệ → xử lý theo edge case.

# Nếu gặp phòng quá lớn → dừng toàn bộ chương trình.

# Pseudocode

# nhập số lượng phòng
# nếu số lượng phòng <= 0:
#     in "Số lượng phòng học không hợp lệ"
#     kết thúc

# for mỗi phòng từ 1 đến số lượng phòng:
#     nhập số hàng
#     nhập số ghế
#     nếu số hàng <= 0 hoặc số ghế <= 0:
#         in "Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này"
#         tiếp tục phòng tiếp theo
#     nếu số hàng > 10 hoặc số ghế > 10:
#         in "Phòng quá lớn. Dừng nhập dữ liệu"
#         kết thúc chương trình
#     in sơ đồ bằng vòng lặp:
#         for i in range(số hàng):
#             in "*" lặp lại số ghế lần
# (2) Triển khai Code Python

# Sơ đồ chỗ ngồi phòng học - Rikkei Education

# Nhập số lượng phòng học
room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

# Edge case 1: số lượng phòng không hợp lệ
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, room_count + 1):
        print(f"\nPhòng học {room}:")
        rows = int(input("Nhập số hàng ghế: "))
        seats = int(input("Nhập số ghế trên mỗi hàng: "))

        # Edge case 2: dữ liệu phòng học không hợp lệ
        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        # Edge case 3: phòng quá lớn
        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        # In sơ đồ chỗ ngồi bằng dấu *
        for _ in range(rows):
            print("*" * seats)
