"""Ôn tập cuối môn"""


def display_menu() -> str | int:
    """Hiển thị menu"""
    print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
=====================================""")
    return input("Nhập lựa chọn của bạn: ")


def get_input_validate(prompt: str, _type: str = "text") -> str | int:
    """Kiểm tra giá trị

    Args:
        prompt (str): câu hỏi
        _type (str, optional): loại exemple(int, quantity). Defaults to "text".

    Returns:
        str | int: Trả về số hoặc chữ
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Dữ liệu không được để trống")

            if _type == "int":
                if not user_input.isdigit():
                    raise ValueError("Dữ liệu phải là số và không được âm")

                value_num = int(user_input)
                return value_num

            if _type == "quantity":
                if not user_input.isdigit():
                    raise ValueError("Dữ liệu phải là số và không được âm")

                value_num = int(user_input)
                if value_num > 1000:
                    raise ValueError("Số lượng tồn đang quá chỉ chứa được (0-1000)")

            return user_input
        except ValueError as e:
            print(f"[Lỗi]: {e}. Vui lòng nhập lại")


class Product:
    """Lớp sản phẩm"""

    def __init__(self, uid, name, import_price, quantity, storage_fee):
        self.__id = uid
        self.__name = name
        self.__import_price = import_price
        self.__quantity = quantity
        self.__storage_fee = storage_fee
        self.__total_value = 0
        self.__stock_status = ""

    @property
    def id(self):
        """Hiển thị"""
        return self.__id

    @property
    def name(self):
        """Hiển thị"""
        return self.__name

    @property
    def import_price(self):
        """Hiển thị"""
        return self.__import_price

    @property
    def quantity(self):
        """Hiển thị"""
        return self.__quantity

    @property
    def storage_fee(self):
        """Hiển thị"""
        return self.__storage_fee

    @property
    def total_value(self):
        """Hiển thị"""
        return self.__total_value

    @property
    def stock_status(self):
        """Hiển thị"""
        return self.__stock_status

    @id.setter
    def cusmer_id(self):
        """id chỉnh"""
        self.__id = self.__id.upper().strip()

    @name.setter
    def cusmer_name(self):
        """Tên chỉnh"""
        self.__name = self.__name.title().strip()

    def calculate_total_value(self):
        """Cập nhật và tính tổng giá trị tồn kho"""
        self.__total_value = (
            self.__import_price * self.__quantity
        ) + self.__storage_fee

    def classify_stock_status(self):
        """Phân loại và cập nhật trạng thái stock_status"""
        if self.__total_value > 30000000:
            self.__stock_status = "Rất cao (Rủi ro ứ đọng vốn)"
        elif self.__total_value > 15000000:
            self.__stock_status = "Cao (Cần chú ý)"
        elif self.__total_value > 9000000:
            self.__stock_status = "Trung bình"
        else:
            self.__stock_status = "Thấp (An toàn)"


class ProductManager:
    """Quản lý danh sách sản phẩm"""

    def __init__(self):
        self.products = []

    def add_product(self):
        """Thêm sản phẩm"""
        while True:
            p_id = get_input_validate("Nhập Mã SP: ")
            for product in self.products:
                if getattr(product, "id") == p_id:
                    print("Mã sản phẩm đã tồn tại")
                    continue
            break
        p_name = get_input_validate("Nhập tên sản phẩm: ")
        p_price = get_input_validate("Nhập giá: ", "int")
        p_store_fee = get_input_validate("Nhập phí kho: ", "int")
        p_quantity = get_input_validate("Nhập số lượng sản phẩm (0-1000): ", "quantity")

        new_product = Product(
            uid=p_id,
            name=p_name,
            import_price=p_price,
            quantity=p_quantity,
            storage_fee=p_store_fee,
        )
        new_product.calculate_total_value()
        new_product.classify_stock_status()
        self.products.append(new_product)
        print("Đã thêm thành công")

    def show_all(self, target: list = None):
        """Hiển thị sản phẩm"""
        if target is None:
            list_show = self.products
        else:
            list_show = target
        if not list_show:
            print("Danh sách rỗng")
            return
        title = (
            f"|{"Mã SP":<10} | {"Tên sản phẩm":<20} | "
            + f"{"Giá nhập":<20} | {"Số lượng":<10} | "
            + f"{"Chi phí kho":<20} | {"Tổng giá trị":<20} | "
            + f"{"Trạng thái tồn":<15}|"
        )
        print("=" * len(title))
        print(f"{"Danh sách sản phẩm".upper():^135}")
        print("=" * len(title))
        for product in list_show:
            print(
                f"|{getattr(product, "id"):<10} | {getattr(product, "name"):<20} | "
                + f"{getattr(product, "import_price"):<20,} | "
                + f"{getattr(product, "quantity"):<10,} | "
                + f"{getattr(product, "storage_fee"):<20,} | "
                + f"{getattr(product, "total_value"):<20,} | "
                + f"{getattr(product, "stock_status "):<15}|"
            )

    def update_product(self):
        """Cập nhật sp theo id"""
        p_id = get_input_validate("Nhập mã sản phẩm cần cập nhật: ")
        for product in self.products:
            if getattr(product, "id") == p_id:
                print(f"Đã tìm thấy sản phẩm có mã: {getattr(product, "id")}")
                

    def delete_product(self):
        """Xóa SP"""
        p_id = get_input_validate("Nhập mã sản phẩm cần xóa: ")
        for product in self.products:
            if getattr(product, "id") == p_id:
                print(f"Đã tìm thấy sản phẩm có mã: {getattr(product, "id")}")
                while True:
                    choice_update = get_input_validate(
                        "Bạn có chắc muốn xóa sản phẩm này khỏi hệ thống không? (Y/N): "
                    )
                    if choice_update.lower() == "y":
                        self.products.remove(product)
                        print("Đã xóa thànhc công")
                        return
                    elif choice_update.lower() == "n":
                        print("Hủy bỏ thao tác")
                        return
                    else:
                        print("Vui lòng nhập (Y/N)")
        print("Không tìm thấy")

    def search_product(self):
        """Tìm SP theo tên"""


def main():
    """Thực thi"""
    products = ProductManager()
    while True:
        choice = display_menu()

        match choice:
            case "1":
                products.show_all()
            case "2":
                products.add_product()
            case "3":
                products.update_product()
            case "4":
                products.delete_product()
            case "5":
                products.search_product()
            case "6":
                print("Đã thoát")
                break
            case _:
                print("Vui lòng chọn 1-6")


if __name__ == "__main__":
    main()
