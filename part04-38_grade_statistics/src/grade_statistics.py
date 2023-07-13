# Write your solution here
def calculate_exercise_points(exercises_completed):
    return int(exercises_completed / 10)

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points

    if exam_points < 10:
        return 0
    elif total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

def print_statistics(results):
    num_students = len(results)
    total_points = 0
    pass_count = 0
    grade_counts = [0] * 6

    for result in results:
        exam_points, exercises_completed = result
        exercise_points = calculate_exercise_points(exercises_completed)
        grade = calculate_grade(exam_points, exercise_points)

        total_points += exam_points + exercise_points
        grade_counts[grade] += 1

        if grade > 0:
            pass_count += 1

    if num_students == 0:
        print("No statistics available.")
        return

    average_points = total_points / num_students
    pass_percentage = (pass_count / num_students) * 100

    print("Statistics:")
    print(f"Points average: {average_points:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")

    print("Grade distribution:")
    for grade, count in enumerate(grade_counts):
        print(f"{grade}: {'*' * count}")


def main():
    results = []
    while True:
        line = input("Exam points and exercises completed: ")
        if line.strip() == "":
            break

        exam_points, exercises_completed = map(int, line.split())
        results.append((exam_points, exercises_completed))

    print_statistics(results)


if __name__ == "__main__":
    main()
