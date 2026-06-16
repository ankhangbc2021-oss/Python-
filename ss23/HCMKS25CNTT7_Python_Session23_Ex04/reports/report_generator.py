# rikkei_learning_tools/reports/report_generator.py
from utils.score_utils import calculate_average, classify_student
import datetime
from colorama import Fore, Style


def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for idx, student in enumerate(records, start=1):
        avg = calculate_average(student["scores"])
        classification = classify_student(avg)
        print(
            f"{idx}. [{student['student_id']}] {student['name']} | Điểm: {student['scores']} | "
            f"ĐTB: {avg:.2f} - {classification}"
        )
    print("---------------------------------")


def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    passed = sum(1 for s in records if calculate_average(s["scores"]) >= 5.0)
    failed = total - passed
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write("--- BÁO CÁO HỌC TẬP ---\n")
        f.write(f"Thời gian tạo: {now}\n")
        f.write(f"Tổng số sinh viên: {total}\n")
        f.write(f"Số sinh viên đạt yêu cầu: {passed}\n")
        f.write(f"Số sinh viên cần cải thiện: {failed}\n")
    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số sinh viên đạt yêu cầu: {passed}")
    print(f"Số sinh viên cần cải thiện: {failed}")
    print(
        Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt" + Style.RESET_ALL
    )
