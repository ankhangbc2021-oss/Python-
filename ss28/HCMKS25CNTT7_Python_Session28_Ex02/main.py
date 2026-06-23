from abc import ABC, abstractmethod

# =====================================================================
# 1. CÁC CỔNG DỊCH VỤ ĐÁM MÂY TRUNG GIAN (DUCK TYPING CLASSES)
# =====================================================================


class AWSS3StorageService:
    def upload_lesson(self, lesson):
        print("[Hệ thống AWS S3]: Đang khởi tạo luồng băng thông kết nối tới LMS...")
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
        print(
            f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.\n"
        )


class GoogleCloudStorageService:
    def upload_lesson(self, lesson):
        print(
            "[Hệ thống Google Cloud Storage]: Đang thiết lập kênh truyền tải dữ liệu mã hóa..."
        )
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
        print(
            f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.\n"
        )


# Hàm toàn cục áp dụng Duck Typing độc lập hoàn toàn với cấu trúc kế thừa
def sync_to_cloud(cloud_service, lesson):
    # Bẫy 4 — Sai lệch phương thức trong Duck Typing
    if not hasattr(cloud_service, "upload_lesson") or not callable(
        getattr(cloud_service, "upload_lesson")
    ):
        raise AttributeError(
            "Dịch vụ lưu trữ đám mây không hợp lệ hoặc chưa ký kết chứng chỉ API liên thông."
        )
    cloud_service.upload_lesson(lesson)


# =====================================================================
# 2. KIẾN TRÚC LỚP BÀI HỌC NỘI DUNG (CORE LMS CLASSES)
# =====================================================================


class BaseLesson(ABC):
    """
    Abstract Base Class (ABC) đóng vai trò khung mẫu chuẩn cho mọi bài học.
    """

    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10  # Điểm XP cơ bản hệ thống

    def __init__(self, lesson_code, title):
        self._lesson_code = lesson_code
        self.title = title  # Kích hoạt setter để chuẩn hóa chuỗi dữ liệu
        self.__duration_minutes = 0  # Private attribute đóng gói bảo vệ nghiêm ngặt

    # @property: Decorator tạo getter chỉ đọc, chặn đứng rủi ro thay đổi gián tiếp từ bên ngoài
    @property
    def duration_minutes(self):
        return self.__duration_minutes

    @property
    def lesson_code(self):
        return self._lesson_code

    @property
    def title(self):
        return self._title

    # @property.setter: Kiểm soát việc ghi dữ liệu, đồng thời tự động chuẩn hóa cấu trúc chuỗi
    @title.setter
    def title(self, value):
        self._title = " ".join(value.strip().split()).upper()

    def set_duration(self, minutes):
        """Phương thức nội bộ cấu hình thời lượng bài học"""
        if minutes <= 0:
            raise ValueError(
                "Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0."
            )
        self.__duration_minutes = minutes

    @abstractmethod
    def calculate_completion_score(self):
        """Phương thức trừu tượng tính điểm XP bắt buộc các lớp con phải ghi đè."""
        pass

    @abstractmethod
    def update_content(self, new_data):
        """Phương thức trừu tượng cập nhật nội dung bài học."""
        pass

    # @staticmethod: Hàm tiện ích kiểm tra tính hợp lệ của mã đầu vào không phụ thuộc trạng thái đối tượng
    @staticmethod
    def validate_lesson_code(lesson_code):
        return len(lesson_code) == 10 and lesson_code.startswith("LMS")

    # @classmethod: Phương thức tương tác ở cấp độ Lớp, thay đổi trạng thái toàn hệ thống
    @classmethod
    def update_base_points(cls, new_points):
        if new_points <= 0:
            raise ValueError("Điểm cơ sở hệ thống phải lớn hơn 0.")
        cls.base_completion_points = new_points

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        # Bẫy 3 — Lỗi kiểu dữ liệu khi Overloading toán tử cộng
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes

    # Operator Overloading: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        # Bẫy 3 — Lỗi kiểu dữ liệu khi Overloading toán tử so sánh
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes


class VideoLesson(BaseLesson):
    """Subclass quản lý phân hệ Bài học Lý thuyết Video"""

    def __init__(self, lesson_code, title, video_quality="1080p"):
        super().__init__(lesson_code, title)
        self.video_quality = video_quality
        self.view_count = 0

    def calculate_completion_score(self):
        return self.base_completion_points + (self.duration_minutes * 0.5)

    def update_content(self, new_data):
        if "video_quality" in new_data:
            self.video_quality = new_data["video_quality"]
        if "title" in new_data:
            self.title = new_data["title"]
        print("[Hệ thống] Đã cập nhật thành công thông tin nội dung Video Lesson.")

    def play_video(self):
        """Giả lập học viên click xem bài giảng lý thuyết"""
        self.view_count += 1


class CodingChallenge(BaseLesson):
    """Subclass quản lý phân hệ Bài tập Thực hành Code"""

    def __init__(
        self, lesson_code, title, number_of_testcases=5, difficulty_multiplier=1.5
    ):
        super().__init__(lesson_code, title)
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        return (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )

    def update_content(self, new_data):
        if "number_of_testcases" in new_data:
            testcases = new_data["number_of_testcases"]
            if testcases <= 0:
                raise ValueError(
                    "Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0."
                )
            self.number_of_testcases = testcases
        if "difficulty_multiplier" in new_data:
            self.difficulty_multiplier = new_data["difficulty_multiplier"]


class HybridAssessment(VideoLesson, CodingChallenge):
    """Multiple Inheritance Subclass tích hợp đa kế thừa tuân thủ cấu trúc định tuyến MRO"""

    def __init__(self, lesson_code, title):
        # Khởi tạo chuỗi kế thừa theo sơ đồ MRO
        super().__init__(lesson_code, title)
        # Đồng bộ và nạp cấu hình các thuộc tính của nhánh CodingChallenge
        self.number_of_testcases = 5
        self.difficulty_multiplier = 1.5

    def calculate_completion_score(self):
        # Tích hợp thuật toán tính điểm kép từ cả hai nhánh cha
        video_score = self.base_completion_points + (self.duration_minutes * 0.5)
        coding_score = (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )
        return video_score + coding_score

    def update_content(self, new_data):
        if "number_of_testcases" in new_data:
            testcases = new_data["number_of_testcases"]
            if testcases <= 0:
                raise ValueError(
                    "Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0."
                )
            self.number_of_testcases = testcases
        if "video_quality" in new_data:
            self.video_quality = new_data["video_quality"]


# =====================================================================
# 3. GIAO DIỆN ĐIỀU KHIỂN DÒNG LỆNH TẬP TRUNG (CLI MENU SYSTEM)
# =====================================================================


def main():
    lessons = []
    current_lesson = None

    # Khởi tạo một bài học mẫu hệ thống dùng để demo cho chức năng đối chứng so sánh (Chức năng 5)
    sample_lesson = VideoLesson("LMS0099999", "Khoi tao Framework")
    sample_lesson.set_duration(60)
    lessons.append(sample_lesson)

    while True:
        print("\n===== RIKKEI ACADEMY LMS SIMULATOR PRO =====")
        print("1. Khởi tạo bài học mới (Chọn loại bài học nội dung)")
        print("2. Xem thông tin bài học & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Cập nhật thời lượng & Nội dung bài học (Tính đa hình)")
        print("4. Xem chi tiết điểm thưởng hoàn thành bài học")
        print("5. Kiểm tra gộp thời lượng & So sánh độ dài bài học (Overloading)")
        print("6. Đồng bộ bài giảng lên Nền tảng Đám mây (Duck Typing)")
        print("7. Thoát chương trình")
        print("=============================================")

        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == "1":
            print("\n--- CHỌN LOẠI BÀI HỌC KHỞI TẠO ---")
            print("1. Video Lesson (Bài học Video Lý Thuyết)")
            print("2. Coding Challenge (Bài tập Thực Hành Code)")
            print("3. Hybrid Assessment (Bài Kiểm Tra Tổng Hợp)")
            lesson_type = input("Chọn loại bài học (1-3): ").strip()

            code = input("Nhập mã bài học 10 ký tự: ").strip()
            # Thẩm định tĩnh thông qua lớp cha
            if not BaseLesson.validate_lesson_code(code):
                print(
                    "Mã bài học không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng LMS."
                )
                continue

            title_input = input("Nhập tiêu đề bài học: ")

            try:
                if lesson_type == "1":
                    current_lesson = VideoLesson(code, title_input)
                    print("Khởi tạo bài học Video thành công!")
                elif lesson_type == "2":
                    current_lesson = CodingChallenge(code, title_input)
                    print("Khởi tạo bài tập lập trình thành công!")
                elif lesson_type == "3":
                    current_lesson = HybridAssessment(code, title_input)
                    print("Khởi tạo bài kiểm tra tổng hợp Hybrid thành công!")
                else:
                    print("Lựa chọn phân loại bài học không hợp lệ.")
                    continue

                # Cấu hình thời lượng mặc định nền 45 phút cho bài học mới tạo để chạy luồng demo dữ liệu
                current_lesson.set_duration(45)
                lessons.append(current_lesson)
                print(f"Tiêu đề bài học: {current_lesson.title}")

            except TypeError as e:
                # Bẫy 1 — Khởi tạo lớp trừu tượng trực tiếp
                print(
                    f"[LỖI KIẾN TRÚC]: Thao tác bị nghiêm cấm từ thiết kế hệ thống! Chi tiết: {e}"
                )

        elif choice == "2":
            if not current_lesson:
                print(
                    "Lỗi: Hệ thống chưa ghi nhận dữ liệu bài học. Vui lòng chạy Chức năng 1 trước."
                )
                continue

            print("\n--- THÔNG TIN BÀI HỌC HIỆN TẠI ---")
            print(f"Loại bài học: {type(current_lesson).__name__}")
            print(f"Nền tảng: {current_lesson.platform_name}")
            print(f"Mã bài học: {current_lesson.lesson_code}")
            print(f"Tiêu đề bài học: {current_lesson.title}")
            print(f"Thời lượng bài học: {current_lesson.duration_minutes} phút")

            if isinstance(current_lesson, VideoLesson):
                print(f"Chất lượng video: {current_lesson.video_quality}")
                print(f"Số lượt học viên đã xem: {current_lesson.view_count} lượt")
            if isinstance(current_lesson, CodingChallenge):
                print(
                    f"Số lượng testcase lập trình: {current_lesson.number_of_testcases} bài"
                )
                print(f"Hệ số nhân độ khó: {current_lesson.difficulty_multiplier}")

            print(f"\n[MRO CHECK] Thứ tự chuỗi định tuyến tìm kiếm phương thức (MRO):")
            for cls in type(current_lesson).__mro__:
                print(f" -> {cls.__name__}")

        elif choice == "3":
            if not current_lesson:
                print("Lỗi: Chưa chọn hoặc tạo bài học hoạt động.")
                continue

            print("\n--- CẬP NHẬT NỘI DUNG & THỜI LƯỢNG ---")
            print("1. Giả lập học viên tăng lượt xem video (Chỉ dành cho Video/Hybrid)")
            print("2. Cập nhật thông số bài học (Thời lượng, testcase...)")
            task = input("Chọn tác vụ (1-2): ").strip()

            try:
                if task == "1":
                    if isinstance(current_lesson, VideoLesson):
                        current_lesson.play_video()
                        print("Ghi nhận thành công! Học viên đã xem video bài học.")
                        print(
                            f"Tổng số lượt xem hiện tại: {current_lesson.view_count} lượt."
                        )
                    else:
                        print(
                            "Lỗi hệ thống: Bài học hiện tại không hỗ trợ hình thức xem phát Video."
                        )
                elif task == "2":
                    # Bẫy 2 — Nhập sai số liệu thời lượng hoặc thông số kỹ thuật (Số âm hoặc sai kiểu)
                    new_duration = int(
                        input(
                            "Nhập thời lượng phút mới (Nhập 0 nếu không đổi): "
                        ).strip()
                    )
                    if new_duration > 0:
                        current_lesson.set_duration(new_duration)

                    if isinstance(current_lesson, CodingChallenge) or isinstance(
                        current_lesson, HybridAssessment
                    ):
                        new_tc = int(
                            input(
                                "Nhập số lượng testcase kiểm thử mới bổ sung (Nhập 0 nếu không đổi): "
                            ).strip()
                        )
                        if new_tc > 0:
                            # Đa hình qua phương thức update_content()
                            current_lesson.update_content(
                                {"number_of_testcases": new_tc}
                            )
                            print("Cập nhật thông số thành công!")
                            print(
                                f"Số lượng testcase hiện tại trên hệ thống: {current_lesson.number_of_testcases} testcases."
                            )
                    else:
                        print("Cập nhật thời lượng hoàn tất.")
                else:
                    print("Lựa chọn tác vụ không nằm trong danh mục.")
            except ValueError as e:
                print(f"[LỖI ĐẦU VÀO]: {e}")

        elif choice == "4":
            if not current_lesson:
                print("Lỗi: Vui lòng khởi tạo dữ liệu cấu trúc bài học trước.")
                continue

            # Đa hình động tự nhận biết thuật toán của thực thể tương ứng để gọi hàm
            score = current_lesson.calculate_completion_score()
            print("\n--- CHI TIẾT ĐIỂM THƯỞNG HOÀN THÀNH ---")
            print(
                f"Bài học: {current_lesson.title} (Loại: {type(current_lesson).__name__})"
            )
            print(f"Điểm cơ sở hệ thống: {current_lesson.base_completion_points} XP")
            print(f"Thời lượng tích lũy: {current_lesson.duration_minutes} phút")
            if hasattr(current_lesson, "number_of_testcases"):
                print(
                    f"Số lượng testcase cấu hình: {current_lesson.number_of_testcases} bài"
                )
            print(f"Tổng điểm kinh nghiệm (XP) nhận được khi hoàn thành: {score} XP")

        elif choice == "5":
            if not current_lesson:
                print("Lỗi: Không tìm thấy bài học active để kiểm toán tải.")
                continue

            print("\n--- ĐỒNG BỘ & SO SÁNH THỜI LƯỢNG (OPERATOR OVERLOADING) ---")
            print(
                f"Bài học hiện tại (A): {current_lesson.title} (Thời lượng: {current_lesson.duration_minutes} phút)"
            )
            print("Danh sách kho dữ liệu các bài học đối ứng có trên LMS:")

            for idx, les in enumerate(lessons):
                print(
                    f" [{idx}] {les.lesson_code} ({les.title} - Thời lượng: {les.duration_minutes} phút)"
                )

            try:
                target_idx = int(
                    input(
                        "Chọn số chỉ mục bài học đối ứng (B) từ danh sách trên: "
                    ).strip()
                )
                if target_idx < 0 or target_idx >= len(lessons):
                    print("Chỉ mục vượt quá phạm vi tìm kiếm.")
                    continue

                lesson_b = lessons[target_idx]

                # Thực thi toán tử so sánh Overloading __lt__
                is_shorter = current_lesson < lesson_b
                if is_shorter == NotImplemented:
                    print(
                        "[LỖI NGOẠI LỆ]: Không hỗ trợ so sánh kiểu dữ liệu không tương thích."
                    )
                else:
                    res_str = "NGẮN HƠN" if is_shorter else "KHÔNG NGẮN HƠN"
                    print(
                        f"[Kết quả So sánh (__lt__)]: Thời lượng bài học A {res_str} thời lượng bài học B."
                    )

                # Thực thi toán tử toán học Overloading __add__
                total_time = current_lesson + lesson_b
                if total_time == NotImplemented:
                    print("[LỖI NGOẠI LỆ]: Thao tác cộng gộp không thể thực thi.")
                else:
                    print(
                        f"[Kết quả Tổng hợp (__add__)]: Tổng thời lượng học tập của cả 2 bài học là: {total_time} phút."
                    )
            except Exception as e:
                print(f"Phát hiện lỗi không hợp lệ: {e}")

        elif choice == "6":
            if not current_lesson:
                print("Lỗi: Yêu cầu bài học dữ liệu không được trống.")
                continue

            print("\n--- ĐỒNG BỘ BÀI GIẢNG LÊN NỀN TẢNG ĐÁM MÂY ---")
            print("1. Đồng bộ lên máy chủ AWS S3 Storage")
            print("2. Đồng bộ lên máy chủ Google Cloud Storage")
            print("3. Giả lập lỗi API liên thông truyền dữ liệu (Kiểm thử Bẫy dữ liệu)")
            cloud_choice = input("Chọn dịch vụ lưu trữ (1-3): ").strip()

            if cloud_choice == "1":
                service = AWSS3StorageService()
            elif cloud_choice == "2":
                service = GoogleCloudStorageService()
            elif cloud_choice == "3":
                service = "Một chuỗi thuần văn bản không định hình kiến trúc API"
            else:
                print("Dịch vụ hạ tầng cloud chọn lựa không hợp lệ.")
                continue

            try:
                # Kích hoạt thực thi đồng bộ qua Duck Typing độc lập
                sync_to_cloud(service, current_lesson)
            except AttributeError as e:
                print(f"[HỆ THỐNG PHÁT HIỆN LỖI BẢO MẬT API]: {e}")

        elif choice == "7":
            print(
                "\nCảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!"
            )
            break
        else:
            print(
                "Vui lòng nhập chính xác số thứ tự chức năng điều hướng tự chọn (1-7)."
            )


if __name__ == "__main__":
    main()
