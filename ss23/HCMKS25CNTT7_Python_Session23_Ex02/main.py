"""
Phần 1: Phân tích & Thiết kế Kiến trúc (Architecture Review)
Tác hại của from datetime import *

Nó nhập toàn bộ các lớp/hàm của datetime vào namespace hiện tại → dễ gây xung đột tên.

Ví dụ: nếu có biến global time = 120, sau khi import, lớp datetime.time sẽ ghi đè biến time. Kết quả: biến time không còn là số nguyên 120 nữa mà trở thành một đối tượng lớp time, gây lỗi logic khó phát hiện.

Giải pháp:
import datetime
# hoặc chỉ import cần thiết
from datetime import datetime
Hàm thay thế os.mkdir()

Thư viện os cung cấp os.makedirs(path, exist_ok=True).

Ưu điểm: tạo được thư mục lồng nhau (ví dụ: media_vault/2026/video) và không văng lỗi nếu thư mục cha đã tồn tại.

Cấu trúc cây thư mục khoa học (Folder Tree)

rikkei_media/
├── storage/
│   ├── __init__.py
│   ├── disk_manager.py
│   └── io_helper.py
├── analytics/
│   ├── __init__.py
│   └── time_validator.py
├── main.py
└── raw_files_data.py   # (tuỳ chọn, tách dữ liệu thô ra riêng)
Phần 2: Refactoring & Modularization
"""

from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10",
    },
    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31",
    },
    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15",
    },
]

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
safe_create_dir("media_vault")
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("---------------------------------------------------------------------------")

success_count = 0

for file in raw_files:
    filename = file["filename"]
    size_bytes = file["size_bytes"]
    upload_at = file["upload_at"]

    print(f"[TỆP TIN: {filename}]")

    upload_date = parse_and_inspect_date(upload_at)
    if not upload_date:
        print(
            f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)\n"
        )
        continue

    blocks = calculate_disk_blocks(size_bytes)
    print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
    print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")

    # Phân loại theo định dạng
    if filename.endswith(".mp3"):
        category = "audio"
    elif filename.endswith(".mp4"):
        category = "video"
    else:
        category = "other"

    safe_create_dir(f"media_vault/{upload_date.year}/{category}")
    print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category}')\n")
    success_count += 1

print("========================================================")
print(
    f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{len(raw_files)} tệp tin thành công. Hệ thống ổn định."
)
