# (1) Phân tích lỗi
# Trace code với test case heart_rate = 135:
# Chương trình bắt đầu, in tiêu đề.
# Nhập nhịp tim: heart_rate = 135.
# Kiểm tra điều kiện:
# if heart_rate > 100: → đúng, vì 135 > 100. Khối này được thực thi ngay, in ra "Priority: YELLOW - Abnormal. Monitor closely.".

# Các khối elif phía sau không được xét nữa vì trong cấu trúc if-elif-else, khi một điều kiện đúng thì chương trình dừng kiểm tra các nhánh tiếp theo.
# Kết quả: chỉ in YELLOW, mặc dù 135 > 120 đáng lẽ phải là RED.
# Khái niệm “luồng thực thi từ trên xuống dưới” trong if-elif-else:

# Python sẽ kiểm tra lần lượt từng điều kiện từ trên xuống.
# Khi gặp điều kiện đúng, nó thực thi khối lệnh tương ứng và bỏ qua toàn bộ các nhánh sau.
# Do đó, thứ tự sắp xếp điều kiện rất quan trọng.
# Nguyên nhân khối RED bị bỏ qua:
# Điều kiện if heart_rate > 100 được đặt trước elif heart_rate > 120.
# Với heart_rate = 135, điều kiện >100 đã đúng, nên chương trình dừng tại đó và không bao giờ xét đến elif >120.
# (2) Sửa lỗi
# Giải pháp:
# Sắp xếp lại thứ tự điều kiện từ mức nghiêm trọng nhất xuống mức nhẹ hơn.
# Đảm bảo rằng heart_rate > 120 được kiểm tra trước heart_rate > 100.
# Code đã sửa:

print("---- EMERGENCY TRIAGE SYSTEM ----")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
