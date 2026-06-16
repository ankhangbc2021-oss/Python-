def calculate_average(scores):
    valid_scores = [s for s in scores if isinstance(s, (int, float))]
    if not valid_scores:
        return 0
    return sum(valid_scores) / len(valid_scores)


def classify_student(average):
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
