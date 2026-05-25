# (1) Phân tích lỗi
# Toán tử logic bị sử dụng sai:
# Trong code gốc, điều kiện kiểm tra là:

# if donor_age >= 18 or donor_weight >= 50:
# Toán tử or được dùng sai. Theo quy định y khoa, người hiến máu phải đồng thời thỏa mãn cả hai điều kiện (tuổi ≥ 18 và cân nặng ≥ 50).
# Trace code với test case donor_age = 16, donor_weight = 55:
# donor_age >= 18 → sai (16 < 18).
# donor_weight >= 50 → đúng (55 ≥ 50).

# Với toán tử or, chỉ cần một điều kiện đúng → kết quả là ELIGIBLE.
# Đây là sai logic, vì người 16 tuổi chưa đủ điều kiện hiến máu.
# Sự khác biệt giữa and và or:
# and: yêu cầu cả hai điều kiện đều đúng → mới trả về True.
# or: chỉ cần một trong hai điều kiện đúng → trả về True.
# Trong bài toán này, phải dùng and để đảm bảo bệnh nhân đủ cả tuổi và cân nặng.
# (2) Sửa lỗi
# Code đã sửa:

print("---- BLOOD DONOR SCREENING SYSTEM ----")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight: "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE.")
    if donor_age < 18:
        print("- Reason: Age requirement not met (must be ≥ 18).")
    if donor_weight < 50:
        print("- Reason: Weight requirement not met (must be ≥ 50 kg).")
