import csv
from statistics import mean


def get_student_info():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    exam1_grade = int(input("Enter exam 1 grade: "))
    exam2_grade = int(input("Enter exam 2 grade: "))
    exam3_grade = int(input("Enter exam 3 grade: "))
    grades = [exam1_grade, exam2_grade, exam3_grade]
    return first_name, last_name, exam1_grade, exam2_grade, exam3_grade, mean(grades)


def write_student_record(file_name, student_info):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_info)


file_name = 'grades.csv'

while True:
    student_info = get_student_info()
    write_student_record(file_name, student_info)

    another_student = input("Do you want to enter another student? (yes/no): ").lower()
    if another_student != 'yes':
        break

print("Student records have been written to grades.csv.")
