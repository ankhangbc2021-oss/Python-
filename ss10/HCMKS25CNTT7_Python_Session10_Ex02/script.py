"""
Music Playlist Management System
"""

playlist = []

while True:
    print("\n" + "=" * 50)
    print("        Menu quản lý danh sách")
    print("=" * 50)
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")
    print("=" * 50)

    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            print("\n--- Thêm bài hát ---")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào vị trí bất kỳ")
            sub_choice = input("Chọn cách thêm (1-2): ")
            if sub_choice not in ["1", "2"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue
            song_name = input("Nhập tên bài hát: ")
            if sub_choice == "1":
                playlist.append(song_name)
                print(f"Đã thêm '{song_name}' vào cuối danh sách.")
                print("Số lượng bài hát hiện tại:", len(playlist))
            else:
                try:
                    index = int(input("Nhập vị trí muốn chèn (bắt đầu từ 1): "))
                    if index < 1 or index > len(playlist) + 1:
                        print("Vị trí không hợp lệ.")
                    else:
                        playlist.insert(index - 1, song_name)
                        print(f"Đã chèn '{song_name}' vào vị trí {index}.")
                        print("Số lượng bài hát hiện tại:", len(playlist))
                except ValueError:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

        case "2":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- Danh sách phát ---")
                for i, song in enumerate(playlist, start=1):
                    print(f"{i}. {song}")

        case "3":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n--- Xóa bài hát ---")
            print("1. Xóa theo tên")
            print("2. Xóa theo số thứ tự")
            sub_choice = input("Chọn cách xóa (1-2): ")
            if sub_choice == "1":
                song_name = input("Nhập tên bài hát cần xóa: ")
                if song_name in playlist:
                    playlist.remove(song_name)
                    print(f"Đã xóa bài hát '{song_name}' khỏi danh sách.")
                else:
                    print("Không tìm thấy bài hát trong danh sách phát.")
            elif sub_choice == "2":
                try:
                    index = int(input("Nhập số thứ tự bài hát cần xóa: "))
                    if index < 1 or index > len(playlist):
                        print("Vị trí không hợp lệ.")
                    else:
                        removed_song = playlist.pop(index - 1)
                        print(f"Đã xóa bài hát '{removed_song}' khỏi danh sách.")
                except ValueError:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

        case "4":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n--- Sắp xếp / Trích xuất ---")
            print("1. Sắp xếp theo bảng chữ cái")
            print("2. Nghe thử 3 bài hát đầu tiên")
            sub_choice = input("Chọn chức năng (1-2): ")
            if sub_choice == "1":
                playlist.sort()
                print("Danh sách đã được sắp xếp theo bảng chữ cái.")
            elif sub_choice == "2":
                print("3 bài hát đầu tiên trong danh sách:")
                for i, song in enumerate(playlist[:3], start=1):
                    print(f"{i}. {song}")
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")

        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1-5.")
