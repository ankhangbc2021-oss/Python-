class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""
        # Tự động tính toán khi khởi tạo đối tượng
        self.calculate_final_score()
        self.classify_academic_rank()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def theory_score(self):
        return self.__theory_score

    @property
    def practice_score(self):
        return self.__practice_score

    @property
    def project_score(self):
        return self.__project_score

    @property
    def final_score(self):
        return self.__final_score

    @property
    def academic_rank(self):
        return self.__academic_rank

    def update_scores(self, theory, practice, project):
        self.__theory_score = theory
        self.__practice_score = practice
        self.__project_score = project
        # Cập nhật lại điểm tổng kết và học lực sau khi sửa đổi
        self.calculate_final_score()
        self.classify_academic_rank()

    def calculate_final_score(self):
        self.__final_score = (
            (self.__theory_score * 0.2)
            + (self.__practice_score * 0.3)
            + (self.__project_score * 0.5)
        )

    def classify_academic_rank(self):
        if self.__final_score >= 8.5:
            self.__academic_rank = "Gioi"
        elif self.__final_score >= 7.0:
            self.__academic_rank = "Kha"
        elif self.__final_score >= 5.0:
            self.__academic_rank = "Trung binh"
        else:
            self.__academic_rank = "Yeu"


class StudentManager:
    def __init__(self):
        self.students: list[Student] = []

    def _validate_score(self, prompt):
        """Hàm bổ trợ kiểm tra nhập điểm số từ 0.0 đến 10.0 và bọc lỗi ép kiểu"""
        while True:
            try:
                score = float(input(prompt))
                if 0.0 <= score <= 10.0:
                    return score
                print("Loi: Diem so phai nam trong khoang tu 0.0 den 10.0!")
            except ValueError:
                print("Loi: Vui long nhap so hop le!")

    def add_student(self):
        print("\n--- THEM SINH VIEN MOI ---")
        stu_id = input("Nhap Ma SV: ").strip()
        if not stu_id:
            print("Loi: Ma sinh vien khong duoc de trong!")
            return

        # Kiểm tra trùng mã sinh viên
        for stu in self.students:
            if stu.id.lower() == stu_id.lower():
                print("Loi: Ma sinh vien da ton tai trong he thong!")
                return

        stu_name = input("Nhap Tên SV: ").strip()
        if not stu_name:
            print("Loi: Ten sinh vien khong duoc de trong!")
            return

        stu_theory_score = self._validate_score("Nhap diem ly thuyet: ")
        stu_practice_score = self._validate_score("Nhap diem thuc hanh: ")
        stu_project_score = self._validate_score("Nhap diem do an: ")

        new_student = Student(
            stu_id, stu_name, stu_theory_score, stu_practice_score, stu_project_score
        )
        self.students.append(new_student)
        print("Thong bao: Them sinh vien thanh cong!")

    def show_all(self, custom_list=None):
        # Hỗ trợ hiển thị danh sách truyền vào (dùng cho hàm tìm kiếm) hoặc toàn bộ hệ thống
        list_to_show = custom_list if custom_list is not None else self.students

        if not list_to_show:
            print("\nDanh sach sinh vien trong.")
            return

        print("\n" + "=" * 125)
        print(
            f"{'Ma SV':<12} | {'Ho ten':<25} | {'Diem Ly Thuyet':<16} | {'Diem Thuc Hanh':<16} | {'Diem Do An':<14} | {'Diem Tong Ket':<16} | {'Hoc Luc':<12}"
        )
        print("-" * 125)
        for stu in list_to_show:
            print(
                f"{stu.id:<12} | {stu.name:<25} | {stu.theory_score:<16.1f} | {stu.practice_score:<16.1f} | {stu.project_score:<14.1f} | {stu.final_score:<16.2f} | {stu.academic_rank:<12}"
            )
        print("=" * 125)

    def update_student(self):
        print("\n--- CAP NHAT THONG TIN SINH VIEN ---")
        stu_id = input("Nhap ma SV can cap nhat: ").strip()

        for stu in self.students:
            if stu.id.lower() == stu_id.lower():
                print(f"Dang cap nhat diem cho sinh vien: {stu.name}")
                stu_theory_score = self._validate_score("Nhap diem ly thuyet moi: ")
                stu_practice_score = self._validate_score("Nhap diem thuc hanh moi: ")
                stu_project_score = self._validate_score("Nhap diem do an moi: ")

                stu.update_scores(
                    stu_theory_score, stu_practice_score, stu_project_score
                )
                print("Thong bao: Cap nhat thanh cong!")
                return

        print("Loi: Khong tim thay sinh vien co ma vua nhap.")

    def delete_student(self):
        print("\n--- XOA SINH VIEN ---")
        stu_id = input("Nhap ma SV can xoa: ").strip()

        for stu in self.students:
            if stu.id.lower() == stu_id.lower():
                choice = (
                    input(f"Ban co chac muon xoa sinh vien '{stu.name}' khong? (Y/N): ")
                    .strip()
                    .lower()
                )
                if choice == "y":
                    self.students.remove(stu)
                    print("Thong bao: Da xoa sinh vien thanh cong!")
                else:
                    print("Thong bao: Da huy bo thao tac xoa.")
                return

        print("Loi: Khong tim thay sinh vien co ma vua nhap.")

    def search_student(self):
        print("\n--- TIM KIEM SINH VIEN ---")
        name_input = input("Nhap ten can tim kiem: ").strip().lower()

        if not name_input:
            print("Loi: Vui long nhap tu khoa de tim kiem!")
            return

        # Tìm gần đúng và không phân biệt chữ hoa, chữ thường
        find_list = [stu for stu in self.students if name_input in stu.name.lower()]

        if not find_list:
            print("Thong bao: Khong tim thay sinh vien phu hop.")
        else:
            print(f"\nTim thay {len(find_list)} sinh vien phu hop:")
            self.show_all(find_list)


# --- CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN) ---
def main():
    manager = StudentManager()

    while True:
        print("\n================ MENU ================")
        print("1. Hien thi danh sach sinh vien")
        print("2. Them sinh vien moi")
        print("3. Cap nhat thong tin sinh vien")
        print("4. Xoa sinh vien")
        print("5. Tim kiem sinh vien theo ten")
        print("6. Thoat")
        print("=====================================")

        choice = input("Nhap lua chon cua ban (1-6): ").strip()

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_student()
            case "3":
                manager.update_student()
            case "4":
                manager.delete_student()
            case "5":
                manager.search_student()
            case "6":
                print("\nCam on ban da su dung he thong quan ly hoc tap!")
                break
            case _:
                print("Loi: Lua chon khong hop le! Vui long nhap lai tu 1 den 6.")


if __name__ == "__main__":
    main()
