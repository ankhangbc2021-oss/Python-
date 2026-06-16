# HỆ THỐNG QUẢN LÝ LỊCH TRÌNH BAY - RIKKEI AVIATION

## 1. Cấu trúc cây thư mục (Folder Tree)
```folder tree
rikkei_aviation/
├── core/
│   ├── init.py
│   ├── logistics.py      # Hiển thị lịch trình & hậu cần
│   └── manager.py        # Tiếp nhận chuyến bay mới
├── utils/
│   ├── init.py
│   ├── time_helper.py    # Tính ETA
│   └── file_helper.py    # Khởi tạo thư mục log
├── main.py               # Menu điều hướng
└── flights_data.py       # (tuỳ chọn) dữ liệu 
```
## 2. Giải thích kiến trúc

- **main.py**: Chỉ chứa vòng lặp `while` để hiển thị menu và gọi hàm từ các module.
- **core/logistics.py**: Quản lý hiển thị lịch trình và tính toán hậu cần (sử dụng `math.ceil`).
- **core/manager.py**: Tiếp nhận chuyến bay mới, kiểm tra trùng mã, bẫy lỗi nhập sai định dạng thời gian.
- **utils/time_helper.py**: Tính toán ETA bằng `datetime.strptime` và `timedelta`.
- **utils/file_helper.py**: Khởi tạo thư mục log bằng `os.path.exists` và `os.mkdir`.
## 3. Tại sao không dùng `from math import *`

- **Ô nhiễm namespace**: Toàn bộ hàm/hằng số của `math` sẽ tràn vào không gian tên hiện tại.
- **Xung đột tên**: Ví dụ có biến `ceil` trong code, sẽ bị ghi đè bởi `math.ceil`.
- **Mất tính tường minh**: Khó biết hàm đến từ đâu khi đọc code.

Giải pháp an toàn:
```python
import math
# hoặc
from math import ceil
```
## 4. Edge Cases được xử lý
- **Trùng mã chuyến bay**: Không cho thêm mới, báo lỗi ngay.
- **Sai định dạng thời gian**: Bẫy ValueError, báo lỗi và yêu cầu nhập lại.
- **Trùng thư mục log**: Nếu đã tồn tại thì bỏ qua, không văng lỗi.
- **Sai lựa chọn menu**: Bẫy ValueError, yêu cầu nhập lại từ 1-5.
