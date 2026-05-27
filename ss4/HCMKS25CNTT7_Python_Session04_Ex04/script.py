"""Đoán số may mắn"""
num = 1
output_end = 0
# Start code
while num <= 5:
    number = int(input(f"Lượt đoán {num} - Nhập số của bạn: "))
    
    if number > 79:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")
    elif number < 79:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    else:
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        output_end = 1
        break
    num += 1

print("---Trò chơi kết thúc---")
if(output_end == 1):
    print("Chúc mừng bạn đã trúng thưởng quà đặc biệt")
else:
    print("Bạn đã hết lượt chơi")
