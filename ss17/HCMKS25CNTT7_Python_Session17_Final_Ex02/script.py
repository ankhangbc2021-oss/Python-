# QUẢN LÝ CHUYẾN XE ĐƯỜNG DÀI
# Ôn tập Python

chuyen_xe_list = []


# =========================
# HÀM XỬ LÝ NGHIỆP VỤ
# =========================
def tinh_trang_thai(ghe_trong, tong_ghe):
    ty_le = ghe_trong / tong_ghe
    if ghe_trong == 0:
        return "Hết vé"
    elif ty_le < 0.15:
        return "Hút khách"
    elif ty_le <= 0.8:
        return "Bình thường"
    else:
        return "Ế khách"


def cap_nhat_doanh_thu(chuyen_xe):
    ghe_ban = chuyen_xe["tong_ghe"] - chuyen_xe["ghe_trong"]
    chuyen_xe["doanh_thu"] = chuyen_xe["gia_ve"] * ghe_ban
    chuyen_xe["trang_thai"] = tinh_trang_thai(
        chuyen_xe["ghe_trong"], chuyen_xe["tong_ghe"]
    )


def hien_thi_danh_sach():
    if not chuyen_xe_list:
        print("Danh sách chuyến xe trống.")
        return
    print(
        "{:<8} {:<25} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
            "Mã",
            "Tuyến đường",
            "Giá vé",
            "Ghế trống",
            "Tổng ghế",
            "Doanh thu",
            "Trạng thái",
        )
    )
    for cx in chuyen_xe_list:
        print(
            "{:<8} {:<25} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
                cx["ma"],
                cx["tuyen_duong"],
                cx["gia_ve"],
                cx["ghe_trong"],
                cx["tong_ghe"],
                cx["doanh_thu"],
                cx["trang_thai"],
            )
        )


def khai_bao_chuyen_xe():
    ma = input("Nhập mã chuyến xe: ").strip()
    if not ma or any(cx["ma"] == ma for cx in chuyen_xe_list):
        print("Mã chuyến xe không hợp lệ hoặc đã tồn tại.")
        return
    tuyen = input("Nhập tuyến đường: ").strip()
    if not tuyen:
        print("Tuyến đường không được để trống.")
        return
    try:
        gia = int(input("Nhập giá vé: "))
        tong = int(input("Nhập tổng số ghế: "))
        if gia <= 0 or tong <= 0:
            raise ValueError
    except ValueError:
        print("Giá vé và tổng số ghế phải là số nguyên dương.")
        return
    cx = {
        "ma": ma,
        "tuyen_duong": tuyen,
        "gia_ve": gia,
        "ghe_trong": tong,
        "tong_ghe": tong,
        "doanh_thu": 0,
        "trang_thai": tinh_trang_thai(tong, tong),
    }
    chuyen_xe_list.append(cx)
    print("Đã thêm chuyến xe mới.")


def dat_ve():
    ma = input("Nhập mã chuyến xe cần đặt vé: ").strip()
    cx = next((c for c in chuyen_xe_list if c["ma"] == ma), None)
    if not cx:
        print("Không tìm thấy chuyến xe.")
        return
    try:
        so_ve = int(input("Nhập số vé muốn đặt: "))
        if so_ve <= 0 or so_ve > cx["ghe_trong"]:
            raise ValueError
    except ValueError:
        print("Số vé đặt không hợp lệ.")
        return
    cx["ghe_trong"] -= so_ve
    cap_nhat_doanh_thu(cx)
    print("Đặt vé thành công.")


def huy_chuyen():
    ma = input("Nhập mã chuyến xe cần hủy: ").strip()
    cx = next((c for c in chuyen_xe_list if c["ma"] == ma), None)
    if not cx:
        print("Không tìm thấy chuyến xe.")
        return
    xac_nhan = input("Bạn có chắc muốn xóa chuyến xe này? (Y/N): ").strip().lower()
    if xac_nhan == "y":
        chuyen_xe_list.remove(cx)
        print("Đã xóa chuyến xe.")
    else:
        print("Hủy thao tác.")


def tim_kiem():
    lua_chon = input("Tìm theo (1: Mã CX, 2: Tuyến đường): ").strip()
    if lua_chon == "1":
        ma = input("Nhập mã chuyến xe: ").strip()
        ket_qua = [c for c in chuyen_xe_list if c["ma"] == ma]
    else:
        tuyen = input("Nhập tuyến đường: ").strip().lower()
        ket_qua = [c for c in chuyen_xe_list if tuyen in c["tuyen_duong"].lower()]
    if not ket_qua:
        print("Không tìm thấy kết quả.")
    else:
        print(
            "{:<8} {:<25} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
                "Mã",
                "Tuyến đường",
                "Giá vé",
                "Ghế trống",
                "Tổng ghế",
                "Doanh thu",
                "Trạng thái",
            )
        )
        for cx in ket_qua:
            print(
                "{:<8} {:<25} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
                    cx["ma"],
                    cx["tuyen_duong"],
                    cx["gia_ve"],
                    cx["ghe_trong"],
                    cx["tong_ghe"],
                    cx["doanh_thu"],
                    cx["trang_thai"],
                )
            )


def thong_ke():
    thong_ke_dict = {"Hết vé": 0, "Hút khách": 0, "Bình thường": 0, "Ế khách": 0}
    for cx in chuyen_xe_list:
        thong_ke_dict[cx["trang_thai"]] += 1
    print("Thống kê trạng thái chuyến xe:")
    for k, v in thong_ke_dict.items():
        print(f"- {k}: {v}")


# =========================
# MENU CHÍNH
# =========================
def menu():
    while True:
        print("\n=== QUẢN LÝ CHUYẾN XE ===")
        print("1. Hiển thị danh sách chuyến xe")
        print("2. Khai báo chuyến xe mới")
        print("3. Cập nhật đặt vé")
        print("4. Hủy chuyến xe")
        print("5. Tìm kiếm chuyến xe")
        print("6. Thống kê trạng thái")
        print("7. Thoát")
        chon = input("Nhập lựa chọn: ").strip()
        if chon == "1":
            hien_thi_danh_sach()
        elif chon == "2":
            khai_bao_chuyen_xe()
        elif chon == "3":
            dat_ve()
        elif chon == "4":
            huy_chuyen()
        elif chon == "5":
            tim_kiem()
        elif chon == "6":
            thong_ke()
        elif chon == "7":
            print("Cảm ơn đã sử dụng chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ.")


# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================
if __name__ == "__main__":
    menu()
