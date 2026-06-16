import datetime

def parse_and_inspect_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"[WARNING] Ngày upload '{date_str}' không hợp lệ.")
        return None
