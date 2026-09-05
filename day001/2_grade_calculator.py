"""Calculate averages and grades for a few students."""

students = {
    "Aarav": [85, 90, 78],
    "Isha": [55, 60, 40],
    "Rohan": [95, 92, 98],
    "Meera": [30, 45, 50],
}

def calculate_average(marks_list):
    total = 0
    for mark in marks_list:
        total += mark
    return total / len(marks_list)


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F (Fail)"


print("Student Report Card")
print("=" * 40)

for name, marks in students.items():
    avg = calculate_average(marks)
    grade = get_grade(avg)
    status = "Pass" if grade != "F (Fail)" else "Fail"

    print(f"{name:<8} | Marks: {marks} | Avg: {avg:.1f} | Grade: {grade} | {status}")

print("=" * 40)
