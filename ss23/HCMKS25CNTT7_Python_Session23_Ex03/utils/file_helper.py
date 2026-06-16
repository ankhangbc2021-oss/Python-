import os

def create_folder():
    print("----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    folder_name = "aviation_logs"
    if not os.path.exists(folder_name):
        print(f"[SYSTEM] Thư mục '{folder_name}' chưa tồn tại. Đang tiến hành khởi tạo...")
        os.mkdir(folder_name)
        print("[SYSTEM] Tạo thư mục thành công!")
    else:
        print("[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo")
