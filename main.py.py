
# Student Marks Analyzer

def calculate_average(marks):
    return sum(marks) / len(marks)

def main():
    print("STUDENT MARKS ANALYZER")

    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)

    print("\n--- Student Result ---")
    print("Student Name:", name)
    print("Total Marks:", sum(marks))
    print("Average Marks:", round(average, 2))

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    main()